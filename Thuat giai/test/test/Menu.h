void XuatMenu();
void XuLyMenu(int menu, int a[MAX], int& n);
int ChonMenu(int soMenu);

void XuatMenu()
{
	cout << "\n-------------------Chuc Nang----------------\n";
	cout << "0.Thoat chuong trinh\n";
	cout << "1.Tao cau truc du lieu\n";
	cout << "2.Tao nut moi\n";
	cout << "3.Tao danh sach lien ket rong\n";
	cout << "4. Kiem tra danh sach rong\n";
}
int ChonMenu(int soMenu)
{
	int stt;
	for (;;)
	{
		system("CLS");
		XuatMenu();
		cout << "\nNhap 1 so (0 <=so<" << soMenu << ")de chon menu,stt =";
		cin >> stt;
		if (0 <= stt && stt <= soMenu)
			break;
	}
	return stt;
}
void XuLyMenu(int menu, Data arr[], int& n)
{
	switch (menu)
	{
		LIST l;
		int x, kq;
	case 0:
		system("CLS");
		cout << "Thoat khoi chuong trinh\n";
		break;
	case 1:
		system("CLS");
		cout << "Tao cau truc du lieu\n";
		NhapDS(l);
		Xuat_DSSV(l);
		
		break;
	case 2:
		system("CLS");
		cout << " Tao nut moi\n";
		break;
	case 3:
		system("CLS");
		cout << " Tao danh sach lien ket rong\n";
		break;
	case 4:
		system("CLS");
		cout << " Kiem tra danh sach rongn";
		break;
	}
	_getch();
}