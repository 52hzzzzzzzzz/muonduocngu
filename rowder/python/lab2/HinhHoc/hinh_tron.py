from hinh_hoc import HinhHoc
import math

class HinhTron(HinhHoc):
    def __init__(self, bk: float):
        super().__init__(bk)

    @property
    def banKinh(self):
        return self.canh
    
    def TinhDienTich(self) -> float:
        return math.pi * math.pow(self.banKinh,2)
    
    def __str__(self) -> str:
        return super().__str__() + f"tron co ban kinh {self.banKinh}, co dien tich {self.TinhDienTich()}"
    