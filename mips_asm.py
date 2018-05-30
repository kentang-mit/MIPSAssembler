def get_bin(x):
    out = str(bin(x)[2:])
    out = '0'*(5-len(out))+out
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

    
if __name__ == '__main__':
    ASM = MIPS_Assembler()
    print(ASM.or_(6,10,9))
