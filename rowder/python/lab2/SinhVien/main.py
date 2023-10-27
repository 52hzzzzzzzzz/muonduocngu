from datetime import datetime
from sinh_vien import SinhVien
from danh_sach_sinh_vien import DanhSachSV

sv1 = SinhVien(1957698, "Trần Văn A", datetime.strptime("23/6/1999", "%d/%m/%Y"))
sv2 = SinhVien(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"))
sv3 = SinhVien(1957692, "Thái Thị Thu",datetime.strptime("15/8/1998", "%d/%m/%Y"))
sv4 = SinhVien(2999324, "Trần Thanh Tâm", datetime.strptime("27/8/2009", "%d/%m/%Y"))
sv5 = SinhVien(2884544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2888", "%d/%m/%Y"))
sv6 = SinhVien(2894567, "Nguyễn Thành Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"))
sv7 = SinhVien(2884545, "Nguyễn Thanh Thanh", datetime.strptime("29/8/1999", "%d/%m/%Y")) 
sv8 = SinhVien(2894679, "Võ Hoài Nam", datetime.strptime("4/1/2888", "%d/%m/%Y"))

danhsach = DanhSachSV()
danhsach.themSinhVien(sv1)
danhsach.themSinhVien(sv2)
danhsach.themSinhVien(sv3)
danhsach.themSinhVien(sv4)
danhsach.themSinhVien(sv5)
danhsach.themSinhVien(sv6)
danhsach.themSinhVien(sv7)
danhsach.themSinhVien(sv8)
danhsach.xuat()
danhsach.xoaSvTheoMssv(2884545)
danhsach.xuat()
# danhsach.timSvTheoTen('Nam')
'''
danhsach = DanhSachSV()

f = open("bt1/sv.txt", "r")
print(f.readline())
f.close()
'''
print(danhsach.timVTSvTheoMssv(1957691))
# print(danhsach.timSvTheoTen('Nam'))
# print(danhsach.timSvSinhTruocNgay(datetime.strptime("28/6/1999", "%d/%m/%Y")))
# newlist.xuat()
# danhsach.xuat()

# newlist = danhsach.timSvTheoMssv(1957691)
# newlist = danhsach.timSvTheoTen('Nam')
# newlist = danhsach.timSvSinhTruocNgay(datetime.strptime("28/6/1999", "%d/%m/%Y"))
# for sv in newlist:
#     print(sv)