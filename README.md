# MIPSAssembler
A MIPS32 Assembler in Python.

Sample input: in `test.txt`

Sample output: in `test.mif`

Currently, label in `j`, `jal`, `beq`, `bne` etc. are not supported. Also, you should write `jr $31` instead of `jr $ra` at least now.

Note that the `beq` / `bne` address is the relative address corresponding to PC+4.