from phan_so import PhanSo
from danh_sach_phan_so import DanhSachPhanSo

# ps1 = PhanSo(-1,2)
# ps2 = PhanSo(7,4)
# ps3 = PhanSo(2,-3)
# ps4 = PhanSo(5,2)

dsps = DanhSachPhanSo()
ds = DanhSachPhanSo()
dsps.docTuFile("test.txt")
print("Danh sach phan so:")
dsps.xuat()
# dsps.them(ps1)
# dsps.them(ps2)
# dsps.them(ps3)
# dsps.them(ps4)

# dsps.xuat()
print(dsps.demPSAm())
print("PS duong nho nhat: " ,dsps.timPSDuongMin())
print("Sap phan so giam tren mau: ")
dsps.SapXepGiamTrenMau()
dsps.xuat()

dsps.SapXepTangTrenTu()
dsps.xuat()

print("\nTong phan so am: ", dsps.TongPhanSoAm())