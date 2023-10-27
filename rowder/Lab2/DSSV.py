import datetime
class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime.date) -> None:
        self.maSo = maSo
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo

    @maSo.setter
    def maSo(self, maso):
        if SinhVien.laMaSoHopLe(maso):
            self.__maSo = maso

    @staticmethod
    def laMaSoHopLe(maso: int):
        return len(str(maso)) == 7

    @classmethod
    def doiTenTruong(cls, tenmoi):
        SinhVien.truong = tenmoi

    def __str__(self) -> str:
        return f"MS: {self.maSo}\tHọ tên: {self.hoTen}\tNgày sinh: {self.ngaySinh}"

    def xuat(self):
        print(f"MS: {self.maSo}\tHọ tên: {self.hoTen}\tNgày sinh: {self.ngaySinh}")

    def getHoTen(self):
        return self.hoTen

    def getNgaySinh(self):
        return self.ngaySinh

class DanhSachSv:
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
        return [sv for sv in self.dssv if ten.lower() in sv.getHoTen().lower()]

    def timSvSinhTruocNgay(self, ngay: datetime.date):
        return [sv for sv in self.dssv if sv.getNgaySinh() < ngay]

    def getDSSV(self):
        return self.dssv

    def docTuFile(self, ten_file):
        try:
            with open(ten_file, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split('\t')
                    if len(parts) == 3:
                        maSo = int(parts[0])
                        hoTen = parts[1]
                        ngaySinh = datetime.datetime.strptime(parts[2], "%Y-%m-%d").date()
                        sv = SinhVien(maSo, hoTen, ngaySinh)
                        self.themSinhVien(sv)
            print("Đã đọc danh sách sinh viên từ tệp", ten_file)
        except FileNotFoundError:
            print("Không tìm thấy tệp", ten_file)

    def sapXepSvTheoHoTen(self, giam_dan=False):
        """Sắp xếp danh sách sinh viên theo họ tên tăng/giảm dần."""
        self.dssv.sort(key=lambda sv: sv.getHoTen(), reverse=giam_dan)
    

# Tạo danh sách sinh viên và thêm vào một số sinh viên
dssv = DanhSachSv()


while True:
    print("\n-------- Menu --------")
    print("1. In danh sách sinh viên")
    print("2. Tìm sinh viên theo tên")
    print("3. Tìm sinh viên sinh trước một ngày cụ thể")
    print("4. Đọc danh sách sinh viên từ tệp")
    print("5. Sắp xếp danh sách sinh viên theo Họ và Tên")
    print("6. Thoát")
    choice = input("Chọn tùy chọn (1/2/3/4/5/6): ")
    
    if choice == '1':
        print("Danh sách sinh viên:")
        dssv.xuat()
    elif choice == '2':
        ten = input("Nhập tên sinh viên cần tìm: ")
        sinh_vien_theo_ten = dssv.timSvTheoTen(ten)
        if sinh_vien_theo_ten:
            print(f"Sinh viên có tên '{ten}':")
            for sv in sinh_vien_theo_ten:
                sv.xuat()
        else:
            print(f"Không tìm thấy sinh viên có tên '{ten}'.")

    elif choice == '3':
        ngay_tim_kiem = input("Nhập ngày cần tìm (yyyy-mm-dd): ")
        try:
            ngay_tim_kiem = datetime.datetime.strptime(ngay_tim_kiem, "%Y-%m-%d").date()
            sinh_vien_sinh_truoc_ngay = dssv.timSvSinhTruocNgay(ngay_tim_kiem)
            if sinh_vien_sinh_truoc_ngay:
                print(f"Sinh viên sinh trước ngày {ngay_tim_kiem}:")
                for sv in sinh_vien_sinh_truoc_ngay:
                    sv.xuat()
            else:
                print(f"Không tìm thấy sinh viên sinh trước ngày {ngay_tim_kiem}.")
        except ValueError:
            print("Ngày không hợp lệ. Vui lòng nhập lại theo định dạng 'yyyy-mm-dd'.")

    elif choice == '4':
        ten_tep = input("Nhập tên tệp chứa danh sách sinh viên (vd: dssv.txt): ")
        dssv.docTuFile(ten_tep)

    elif choice == '5':
        giam_dan = input("Sắp xếp giảm dần? (y/n): ").lower()
        if giam_dan == 'y':
            dssv.sapXepSvTheoHoTen(True)
        else:
            dssv.sapXepSvTheoHoTen()

    elif choice == '6':
        break
    else:
        print("Tùy chọn không hợp lệ. Vui lòng chọn lại.")