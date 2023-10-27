from datetime import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh


    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso


    @property
    def hoTen(self):
        return self.__hoTen
    
    @property
    def ngaySinh(self):
        return self.__ngaySinh

    @staticmethod
    def laMaSoHopLe(maso:int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi
    
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
