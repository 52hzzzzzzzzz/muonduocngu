from danh_sach_hinh_hoc import DanhSachHinhHoc

dshh = DanhSachHinhHoc()
ds = DanhSachHinhHoc()
dshh.docTuFile('D:\\third year\\python programing\\lab2\\HinhHoc\\dshinhhoc.txt')
dshh.xuat()

print('hinh co dien tich lon nhat', dshh.timHinhCoDienTichLonNhat())
print('hinh co dien tich nho nhat', dshh.TimHinhCoDienTichNhoNhat())

print('Sap giam theo dien tich')
dshh.SapGiamTheoDT()
dshh.xuat()


