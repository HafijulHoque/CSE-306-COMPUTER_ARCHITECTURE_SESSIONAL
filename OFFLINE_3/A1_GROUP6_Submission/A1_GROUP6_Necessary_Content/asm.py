from audioop import add


inst_type = {
    "bneq": ("I", "0000"),
    "sll": ("S", "0001"),
    "nor": ("R", "0010"),
    "add": ("R", "0011"),
    "sw": ("I", "0100"),
    "j": ("J", "0101"),
    "and": ("R", "0110"),
    "andi": ("I", "0111"),
    "or": ("R", "1000"),
    "srl": ("S", "1001"),
    "sub": ("R", "1010"),
    "lw": ("I", "1011"),
    "ori": ("I", "1100"),
    "beq": ("I", "1101"),
    "subi": ("I", "1110"),
    "addi": ("I", "1111"),
}
reg_map = {
    "$zero": "0000",
    "$t0": "0111",
    "$t1": "0001",
    "$t2": "0010",
    "$t3": "0011",
    "$t4": "0100", 
    "$sp": "0110"
}
labels=dict()

def bin_to_hex(*argv):
    res=''
    for arg in argv:
        res += hex(int(arg, 2))[2:]
    return res

def handle_IRS_type(inst_sep, fmt, i)->str:
    inst_name, r1 = inst_sep[0].split(' ')
    inst_name = inst_name.strip()
    if inst_name == 'lw' or inst_name == 'sw':
        return handle_lwsw(inst_sep)

    opcode = inst_type.get(inst_name)[1]
    r1 = reg_map.get(r1.strip())
    r2 = reg_map.get(inst_sep[1].strip())
    r3 = inst_sep[2].strip()

    if fmt == 'R':
        r3 = reg_map.get(r3)
        return bin_to_hex(opcode, r2, r3, r1)
    if inst_name == 'beq' or inst_name == 'bneq':
        jmp_to = labels.get(r3)
        if i < jmp_to:
            r3 = jmp_to - i - 1
        else:
            r3 = i - jmp_to + 1
            r3 = (1 << 4) - r3 #twos complement
    r3 = int(r3)
    r3 = ((1<<4) + r3) if r3<0 else r3
    r3 = bin(r3)[2:].zfill(4)

    return bin_to_hex(opcode, r2, r1, r3)

def handle_lwsw(inst_sep)->str:
    inst_name, r2 = inst_sep[0].split(' ')
    inst_name = inst_name.strip()

    opcode = inst_type.get(inst_name)[1]
    r2 = reg_map.get(r2.strip())
    r1 = inst_sep[1].strip()
    start = r1.find('(')
    end = r1.find(')')
    shmt = int(r1[:start])
    shmt = bin(shmt)[2:].zfill(4)
    r1 = reg_map.get(r1[start+1:end])
    return bin_to_hex(opcode, r1, r2, shmt)

def handle_J_type(inst_sep, i)->str:
    inst_name, jmpaddr = inst_sep[0].split(' ')[:2]
    inst_name = inst_name.strip()
    jmpaddr = labels.get(jmpaddr.strip())

    opcode = inst_type.get(inst_name)[1]
    # jmpaddr = bin(jumpaddr)[2:].zfill(8)
    return bin_to_hex(opcode) + hex(jmpaddr)[2:].zfill(2) + '0'

def handle_push_pop(inst):
    inst = inst.split(' ')
    # inst[0]=inst[0].strip()
    inst[1]=inst[1].strip()
    return inst[1]
    # if inst[0]=='push':
    #     sw = "sw " + inst[1] +  ", 0($sp)"
    #     subsp = "subi $sp, $sp, 1"
    #     print(sw+"\n"+subsp)
    #     return mips_to_machine(sw) +"\n" + mips_to_machine(subsp)
    # else:
    #     addsp = "addi $sp, $sp, 1"
    #     lw = "lw " + inst[1] + ", 0($sp)"
    #     print(addsp + "\n" +lw)
    #     return mips_to_machine(addsp)+"\n"+mips_to_machine(lw)



def mips_to_machine(inst:str, i=-1)->str:
    comma_sep = inst.split(',')
    inst_name = comma_sep[0].split(' ')[0].strip()
    if inst_name in ['push', 'pop']:
        return handle_push_pop(inst)
    if inst_name not in inst_type:
        print('Invalid instruction: ' + inst_name)
        exit(1)
    fmt, opcode = inst_type.get(inst_name)
    if fmt=='R' or fmt=='I' or fmt=='S':
        return handle_IRS_type(comma_sep, fmt, i)
    else:
        return handle_J_type(comma_sep, i)


try:
    asm_input = open('input.asm', 'r')
except:
    print('\033[91m' + "input.asmh file not found" + '\033[0m')
    exit(1)
 
fout = open('nabid.hex', 'w')
fout.write('v2.0 raw\n')
mips_code = asm_input.readlines()

#replace push_pop
count=0
for line in mips_code:
    if 'push' in line:
        reg = handle_push_pop(line)
        mips_code.insert(count, 'sw {}, 0($sp)\n'.format(reg))
        count = count + 1
        mips_code[count]='subi $sp, $sp, 1\n'
        continue
    elif 'pop' in line:
        reg = handle_push_pop(line)
        mips_code.insert(count, 'addi $sp, $sp, 1\n')
        count = count + 1
        mips_code[count]='lw {}, 0($sp)\n'.format(reg)
        continue
    count=count+1

#save push_pop parsed code     
intermediate = open('intermediate.asm', 'w')
intermediate.writelines(mips_code)
intermediate.close()
#find labels
for i, line in enumerate(mips_code):
    if line=="":
        continue
    line = line.strip()
    colon = line.find(':')
    if colon!=-1:
        labels[line[:colon]] = i

for i, line in enumerate(mips_code):
    cmnt = line.find(';') # strip comments
    if cmnt!=-1:
        line = line[:cmnt].strip()

    print(line, end= '' if line.endswith('\n') else '\n')

    #check if any labels
    colon_start = line.find(':')
    if colon_start != -1:
        line = line[colon_start+1:].strip() # strip label

    if line=="": # if no instruction after label, then exit
        xcode = '0000'    
    else: # else convert inst to xcode
        xcode = mips_to_machine(line, i)

    print("Machine code: " + xcode, end='\n\n')
    fout.write(xcode + '\n')
fout.close()
asm_input.close()
