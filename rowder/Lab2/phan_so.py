import math
class PhanSo:
    def __init__(self, tu_so=1, mau_so=1) :
        self.tu = tu_so
        self.mau = mau_so

    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
    def __add__(self, other):
        ps = PhanSo()
        if not isinstance (other, PhanSo):
            other = PhanSo(other)
        ps.tu = self.tu*other.mau + self.mau*other.tu
        ps.mau = self.mau * other.mau
        return ps.rutGon()

    def rutGon(self):
        ps = PhanSo()
        ucln = math.gcd(self.tu, self.mau)
        ps.tu = self.tu//ucln
        ps.mau = self.mau//ucln
        return ps

class DsPhanSo:
    def __init__(self):
        self.ds = []
    
    def them(self, ps: PhanSo):
        self.ds.append(ps)

    def xuat(self):
        for ps in self.ds:
            print(ps, end = " ")

    def docTuFile(self, tenFile):
        with open(tenFile, 'r', encoding = 'utf-8') as file:
            for hang in file:
                du_lieu = hang.split('/')
                self.them(PhanSo(int(du_lieu[0]), int(du_lieu[1])))
ds = DsPhanSo()
ds.docTuFile("E:\\2110092_Python_L2\\dsps.txt")
ds.xuat()