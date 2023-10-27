from hinh_chu_nhat import HinhChuNhat
from hinh_hoc import HinhHoc

class HinhVuong(HinhHoc):
    def __init__(self, canh: float):
        super().__init__(canh)
    
    def TinhDienTich(self):
        return self.canh*self.canh

    def __str__(self) -> str:
        return super().__str__() + f"vuong co canh {self.canh}, co dien tich = {self.TinhDienTich()}"