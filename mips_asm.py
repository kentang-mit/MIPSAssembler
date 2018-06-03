def get_bin(x,length=5):
    out = str(bin(x)[2:])
    out = '0'*(length-len(out))+out
    return out

class MIPS_Assembler:
    def __init__(self):
        pass

    def add_(self, rd, rs, rt):
        op = '000000'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = '00000'
        func = '100000'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def sub_(self, rd, rs, rt):
        op = '000000'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = '00000'
        func = '100010'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def and_(self, rd, rs, rt):
        op = '000000'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = '00000'
        func = '100100'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def or_(self, rd, rs, rt):
        op = '000000'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = '00000'
        func = '100101'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def xor_(self, rd, rs, rt):
        op = '000000'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = '00000'
        func = '100110'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def sll_(self, rt, rd, sa):
        op = '000000'
        rs_ = '00000'
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = get_bin(sa)
        func = '000000'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def srl_(self, rt, rd, sa):
        op = '000000'
        rs_ = '00000'
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = get_bin(sa)
        func = '000010'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans
    
    def sra_(self, rt, rd, sa):
        op = '000000'
        rs_ = '00000'
        rt_ = get_bin(rt)
        rd_ = get_bin(rd)
        sa = get_bin(sa)
        func = '000011'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def jr_(self, rs):
        op = '000000'
        rs_ = get_bin(rs)
        rt_ = '00000'
        rd_ = '00000'
        sa = '00000'
        func = '001000'
        ans = str(hex(int(op+rs_+rt_+rd_+sa+func,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def addi_(self, rt, rs, imm):
        op = '001000'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def andi_(self, rt, rs, imm):
        op = '001100'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def ori_(self, rt, rs, imm):
        op = '001101'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def xori_(self, rt, rs, imm):
        op = '001110'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def lw_(self, rt, rs, imm):
        op = '100011'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def sw_(self, rt, rs, imm):
        op = '101011'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def beq_(self, rs, rt, imm):
        #relative address to pc+4
        op = '000100'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def bne_(self, rs, rt, imm):
        op = '000101'
        rs_ = get_bin(rs)
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def lui_(self, rt, imm):
        op = '001111'
        rs_ = '00000'
        rt_ = get_bin(rt)
        if imm < 0:
            rd_ = get_bin(65536+imm,16)
        else:
            rd_ = get_bin(imm,16)
        ans = str(hex(int(op+rs_+rt_+rd_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def j_(self, addr):
        op = '000010'
        if addr < 0:
            addr_ = get_bin(67108864+addr,26)
        else:
            addr_ = get_bin(addr,26)
        ans = str(hex(int(op+addr_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def jal_(self, addr):
        op = '000011'
        if addr < 0:
            addr_ = get_bin(67108864+addr,26)
        else:
            addr_ = get_bin(addr,26)
        ans = str(hex(int(op+addr_,2)))[2:]
        ans = '0'*(8-len(ans))+ans
        return ans

    def parse(self, filename):
        f = open(filename,'r')
        instructions = f.readlines()
        f.close()
        parsed_binary = []
        for inst in instructions:
            inst = inst.replace('\n','')
            inst = inst.replace('$', '')
            inst = inst.replace(',',' ')
            inst = inst.replace('(', ' ')
            inst = inst.replace(')', '')
            inst = inst.split()
            inst_type = inst[0]

            if inst_type == 'add':
                rd = int(inst[1])
                rs = int(inst[2])
                rt = int(inst[3])
                parsed_binary.append(self.add_(rd,rs,rt))
            elif inst_type == 'sub':
                rd = int(inst[1])
                rs = int(inst[2])
                rt = int(inst[3])
                parsed_binary.append(self.sub_(rd,rs,rt))
            elif inst_type == 'and':
                rd = int(inst[1])
                rs = int(inst[2])
                rt = int(inst[3])
                parsed_binary.append(self.and_(rd,rs,rt))
            elif inst_type == 'or':
                rd = int(inst[1])
                rs = int(inst[2])
                rt = int(inst[3])
                parsed_binary.append(self.or_(rd,rs,rt))
            elif inst_type == 'xor':
                rd = int(inst[1])
                rs = int(inst[2])
                rt = int(inst[3])
                parsed_binary.append(self.xor_(rd,rs,rt))
            elif inst_type == 'sll':
                rd = int(inst[1])
                rt = int(inst[2])
                sa = int(inst[3])
                parsed_binary.append(self.sll_(rt,rd,sa))
            elif inst_type == 'srl':
                rd = int(inst[1])
                rt = int(inst[2])
                sa = int(inst[3])
                parsed_binary.append(self.srl_(rt,rd,sa))
            elif inst_type == 'sra':
                rd = int(inst[1])
                rt = int(inst[2])
                sa = int(inst[3])
                parsed_binary.append(self.sra_(rt,rd,sa))
            elif inst_type == 'jr':
                rs = int(inst[1])
                parsed_binary.append(self.jr_(rs))
            elif inst_type == 'addi':
                rt = int(inst[1])
                rs = int(inst[2])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[3], radix)                
                parsed_binary.append(self.addi_(rt,rs,imm))
            elif inst_type == 'andi':
                rt = int(inst[1])
                rs = int(inst[2])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[3], radix)

                parsed_binary.append(self.andi_(rt,rs,imm))
            elif inst_type == 'ori':
                rt = int(inst[1])
                rs = int(inst[2])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[3], radix)
                parsed_binary.append(self.ori_(rt,rs,imm))
            elif inst_type == 'xori':
                rt = int(inst[1])
                rs = int(inst[2])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[3], radix)
                parsed_binary.append(self.xori_(rt,rs,imm))
            elif inst_type == 'lw':
                rt = int(inst[1])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[2], radix)                
                rs = int(inst[3])
                parsed_binary.append(self.lw_(rt,rs,imm))
            elif inst_type == 'sw':
                rt = int(inst[1])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[2], radix)                
                rs = int(inst[3])
                parsed_binary.append(self.sw_(rt,rs,imm))
            elif inst_type == 'beq':
                rs = int(inst[1])
                rt = int(inst[2])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[3], radix)
                parsed_binary.append(self.beq_(rs,rt,imm))
            elif inst_type == 'bne':
                rs = int(inst[1])
                rt = int(inst[2])
                radix = 10 if '0x' not in inst[3] else 16
                imm = int(inst[3], radix)
                parsed_binary.append(self.bne_(rs,rt,imm))
            elif inst_type == 'lui':
                rt = int(inst[1])
                radix = 10 if '0x' not in inst[2] else 16
                imm = int(inst[2], radix)
                parsed_binary.append(self.lui_(rt,imm))
            elif inst_type == 'j':
                radix = 10 if '0x' not in inst[1] else 16
                imm = int(inst[1], radix)
                parsed_binary.append(self.j_(imm))
            elif inst_type == 'jal':
                radix = 10 if '0x' not in inst[1] else 16
                imm = int(inst[1], radix)
                parsed_binary.append(self.jal_(imm))

        return parsed_binary, instructions

    def write_mif(self, filename, mif_name):
        parsed_binary, instructions = self.parse(filename)
        f = open(mif_name, 'w')
        header = 'DEPTH = 64; % Memory depth and width are required %\n'+\
        'WIDTH = 32; % Enter a decimal number %\n'+\
        'ADDRESS_RADIX = HEX; % Address and value radixes are optional %\n'+\
        'DATA_RADIX = HEX; % Enter BIN, DEC, HEX, or OCT; unless %\n'+\
        '% otherwise specified, radixes = HEX %\n'+\
        'CONTENT\n'+\
        'BEGIN\n'
        f.write(header)
        for index in range(len(parsed_binary)):
            hexinst = parsed_binary[index]
            real_inst = instructions[index].replace('\n','')
            index_ = hex(index)[2:].upper()
            f.write(str(index_)+' : '+hexinst+'; % '+ real_inst+' %\n')
        f.write('END;\n')
        f.close()
if __name__ == '__main__':
    ASM = MIPS_Assembler()
    ASM.write_mif('test.txt','test.mif')
