import math

class PhanSo:
    def __init__(self, tu=1, mau=1) -> None:
        self.tu = tu if mau >= 0 else -tu
        self.mau = mau if mau > 0 else -mau if mau < 0 else 1
    def __str__(self) -> str:
        return f"{self.tu}/{self.mau}"
    
    def rutGon(self):
        ucln = math.gcd(self.tu, self.mau)
        self.tu = self.tu // ucln
        self.mau = self.mau // ucln
        return self
        
    def __add__(self, other):
        kq = PhanSo()
        if not isinstance(other, PhanSo):
            other = PhanSo()
        kq.tu = self.tu*other.mau + self.mau*other.tu
        kq.mau = self.mau*other.mau
        return kq.rutGon()
    
    def __sub__(self, other):
        kq = PhanSo()
        kq.tu = self.tu*other.mau - self.mau*other.tu
        kq.mau = self.mau*other.mau
        return kq.rutGon()
    
    def __mul__(self, other):
        kq = PhanSo()
        kq.tu = self.tu * other.tu
        kq.mau = self.mau * other.mau
        return kq.rutGon()
    
    def __truediv__(self, other):
        pass

    def laPSAm(self):
        return self.tu*self.mau < 0
    
    def __lt__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu < other.tu
        else:
            return self.tu * other.mau < self.mau * other.tu
        
    
    def __gt__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu > other.tu
        else:
            return self.tu * other.mau > self.mau * other.tu
        
        
    def __eq__(self, other):
        if not isinstance(other, PhanSo):
            other = PhanSo(other)
        if self.mau == other.mau:
            return self.tu < other.tu
        else:
            return self.tu * other.mau == self.mau * other.tu
        
        

a = PhanSo(2,5)
b = PhanSo(1,2)

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

