from phan_so import PhanSo
import pathlib

class DanhSachPhanSo:
    def __init__(self) -> None:
        self.ds = []

    def xuat(self):
        for ps in self.ds:
            print(ps, end = '\t')
    
    def them(self, ps):
        self.ds.append(ps)

    def docTuFile(self, tenfile:str): 
        duong_dan = pathlib.Path(__file__).parent
        duong_dan_file = (duong_dan / tenfile).resolve()
        with open(duong_dan_file, 'r', encoding='utf-8') as f:
            for hang in f:
                data = hang.split('/')
                self.them(PhanSo(int(data[0]), int(data[1])))
    
    def demPSAm(self):
        kq = 0
        for ps in self.ds:
            if ps.laPSAm():
                kq += 1
        return kq
    
    def timPSDuongMin(self):
        kq = PhanSo(10000000000,1)
        for ps in self.ds:
            if kq > ps:
                kq = ps

        return kq
    
    def TongPhanSoAm(self):
        tong = PhanSo()

        for ps in self.ds:
            if ps.tu < 0 or ps.mau < 0:
                tong += ps
        return tong
    
    def XoaPhanSo(self, ps: PhanSo):
        if ps in self.ds:
            self.ds.remove(ps)
        else:
            print(f"Phân số {ps} không tồn tại trong mảng.")
    
    def XoaPhanSoTheoTu(self, x):
        self.ds = [ps for ps in self.ds if ps.tu != x]
    
    def SapXepTangTrenTu(self):
        self.ds.sort(key=lambda ps: ps.tu)

    def SapXepGiamTrenTu(self):
        self.ds.sort(key=lambda ps: ps.tu, reverse=True)

    def SapXepTangTrenMau(self):
        self.ds.sort(key=lambda ps: ps.mau)

    def SapXepGiamTrenMau(self):
        self.ds.sort(key=lambda ps: ps.mau, reverse=True)
    
    
