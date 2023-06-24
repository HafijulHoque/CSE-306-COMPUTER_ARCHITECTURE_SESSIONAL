
# **CSE 306 `Computer Architecture_SESSIONAL`**
 
# **`Offline 1`** : **Arithmetic Logic Unit (ALU)**
In this assignment there was two part.At first ,we had to design a ALU using logisim and simulate it and later we had to implement
it on the hardware level. 

Here is the assignment specification 

[Assignment specification](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_1/SPEC)

Our logisim design is here 

[Logisim circ file ](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_1/DESIGN)

Here is the truth table and block diagram

![](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/blob/master/OFFLINE_1/pics/block.png)

Here is the list of IC we used to implement the ALU

  ![](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/blob/master/OFFLINE_1/pics/pic1.jpg) 

  This is a picture of the ALU we made

  ![](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/blob/master/OFFLINE_1/pics/319613619_3327326460850252_154286502914802511_n.jpg)

  
# **`Offline 2`** : Floating Point Adder

Here is the Assignment specification

[Assignment specification](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_2/spec)

Here is the logisim design of our floating point adder.This was limited to only software simulation.

[Logisim design](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_2/design)


# **`Offline 3`** : 4 Bit MIPS Processor

In this assignment we at first designed a 4 bit mips using logisim and later we implemented it on the hardware level just like offline1.

Here is the assignment specification in case you need

[Assignment specification](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_3/spec)

However the actual implementation differs from the logisim design because we used ATmega32 for ROM.

Here is the logisim design of the mips 

[Logisim design](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_3/A1_GROUP6_Submission/A1_GROUP6_Simulation)

To actually simulate the design you have to at first calculate the machine code of the instruction and then the hexa decimal value of the

insturction has to be loaded on the ROM(IN logisim design just go the mycontrol sub section of the design and there write to hex value of 
the instruction).

However to make things easy ,we have written a assembler that taken assembly code as input and returns the hex value of the instruction that
you can use

Here is the assembler 

[Assembler](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_3/A1_GROUP6_Submission/A1_GROUP6_Necessary_Content)

The input.asm file is the input file where you can write assembly code(a subset of x86) and it will generate an output .hex file

Here is our report which contains all the necessary calculation and information.

[report](https://github.com/Nabidbhai12/CSE-306-COMPUTER_ARCHITECTURE_SESSIONAL/tree/master/OFFLINE_3/A1_GROUP6_Submission/report)



## `A1 Group 6`

- Hafijul Hoque Chowdhury : `1905013` 
- Tanhiat Fatema Afnan : `1905014` 
- Syeda Rifah Tasfia : `1905019` 
- Rakib Ahsan : `1705024`
- Wasif Hamid : `190526`


  
