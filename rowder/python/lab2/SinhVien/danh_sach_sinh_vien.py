import datetime
from sinh_vien import SinhVien

class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.maSo == mssv]
    
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].maSo == mssv:
                return i
        return -1

    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen.split(' ')[-1] == ten]
    
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]
 

        



