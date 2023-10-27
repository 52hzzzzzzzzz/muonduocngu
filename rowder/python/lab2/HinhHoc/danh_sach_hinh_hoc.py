from hinh_hoc import HinhHoc
import sys
from loai_hinh import LoaiHinh
from hinh_tron import HinhTron
from hinh_vuong import HinhVuong
from hinh_chu_nhat import HinhChuNhat

class DanhSachHinhHoc():
    def __init__(self) -> None:
        self.ds = []

    def themHinh(self, hh: HinhHoc):
        self.ds.append(hh)
    
    def xuat(self):
        for hh in self.ds:
            print(hh)
            print()

    def docTuFile(self, fileName: str):
        f = open(fileName, 'r', encoding="utf8")
        lines = f.readlines()

        for line in lines:
            items = line.split(",")
            if (int(items[0]) == LoaiHinh.HinhVuong.value):
                hv = HinhVuong(float(items[1]))
                self.themHinh(hv)
            elif (int(items[0]) == LoaiHinh.HinhChuNhat.value):
                hcn = HinhChuNhat(float(items[1]), float(items[2]))
                self.themHinh(hcn)
            elif (int(items[0]) == LoaiHinh.HinhTron.value):
                ht = HinhTron(float(items[1]))
                self.themHinh(ht)
        return self.ds
    
    def timHinhCoDienTichLonNhat(self):
        max = 0
        result = HinhHoc(0)
        for hh in self.ds:
            if (hh.TinhDienTich() > max):
                max = hh.TinhDienTich()
                result = hh
        return result

    def TimHinhCoDienTichNhoNhat(self):
        min = sys.maxsize
        kq = HinhHoc(0)
        for hh in self.ds:
            if (hh.TinhDienTich() < min):
                min = hh.TinhDienTich()
                kq = hh
        return kq
    
    def TimHinhTronNhoNhat(self):
        pass
    def SapGiamTheoDT(self):
        return self.ds.sort(key=lambda x: x.TinhDienTich(), reverse=True)
    def DemSoLuongHinh(self, loai: LoaiHinh):
        result = []
        if (loai == LoaiHinh.HinhTron):
            result = [hh for hh in self.ds if isinstance(hh, HinhTron)]
        elif (loai == LoaiHinh.HinhVuong):
            result = [hh for hh in self.ds if isinstance(hh, HinhVuong)]
        elif (loai == LoaiHinh.HinhChuNhat):
            result = [hh for hh in self.ds if isinstance(hh, HinhChuNhat)]
        return f"Co {len(result)} {loai}"
    
    def TinhTongDT(self):
        sum = 0
        for hh in self.ds:
            hh = HinhHoc(hh)
            sum += hh.TinhDienTich()
        return sum
    def TimViTriCuaHinh(self, h: HinhHoc):
        for hh in self.ds:
            if (isinstance(hh, h) and hh.canh == h.canh):
                return hh
    def TimHinhTheoDTich(self, dt: float):
        return [hh for hh in self.ds if (hh.TinhDienTich() == dt)]
    def XoaHinh(self, hh: HinhHoc):
        self.ds.remove(hh)
    


    