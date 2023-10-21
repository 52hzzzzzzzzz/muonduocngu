

#define MAX 100

struct SinhVien
{
	char maSV[10];
	char hoTen[25];
	int namSinh;
	float dTB;

};

typedef SinhVien Data;
struct Node
{
	Data info;
	Node* pNext;

};
struct LIST
{
	Node* pHead;
	Node* pTail;

};

Node* GetNode(Data x);
void CreateList(LIST& l);
void InsertTail(LIST& l, Data x);
void Nhap1SV(Data& x);
void Xuat1SV(Data sv);
void Xuat_DSSV(LIST l);
void HoanVi(Data& a, Data& b);
void SelectionSortDTB(LIST& l);

Node* GetNode(Data x) {
	Node* p;
	p = new Node;
	if (p != NULL)
	{
		p->info = x;
		p->pNext = NULL;
			
	}
	return p;
}

void CreateList(LIST& l)
{
	l.pHead = l.pTail = NULL;

}
void InsertTail(LIST& l,Data x ) {
	Node* new_ele = GetNode(x);
	if (new_ele == NULL)
	{
		cout << "Loi cap nhat";
		return;

	}
	if (l.pHead == NULL)
	{
		l.pHead = new_ele;
		l.pTail = l.pHead;
		return;
	}
	l.pTail->pNext = new_ele;
	l.pTail = new_ele;
}
void Nhap1SV(Data& x) {
	cout << "Nhap Ma Sinh vien: ";
	cin >> x.maSV;
	cin.ignore();
	cout << endl << "Nhap Ho va ten: ";
	gets_s(x.hoTen, 25);

	cout << endl << "Nhap nam sinh: ";
	cin >> x.namSinh;
	cout << endl << "Nhap diem trung binh: ";
	cin >> x.dTB;
}
void NhapCD(LIST& l, Data a[MAX], int n) {
	CreateList(l);
	for (int i = 0; i < n; i++)
	{
		InsertTail(l, a[i]);
	}
}
void NhapDS(LIST& l)
{
	Data sv;
	int soSV;
	CreateList(l);
	cout << "Nhap so sinh vien:";
	cin >> soSV;
	for (int i = 0; i < soSV; i++)
	{
		Nhap1SV(sv);
		InsertTail(l, sv);
	}
}
void Xuat1SV(Data sv)
{
	cout << "\n:";
	cout << setiosflags(ios::left)
		<< setw(15) << sv.maSV
		<< setw(25) << sv.hoTen
		<< setw(8) << sv.namSinh
		<< setw(6) << sv.dTB << ":";
}
void Xuat_DSSV(LIST l)
{
	for (Node* p = l.pHead; p != NULL; p = p->pNext)
	{
		cout << "\n";
		Xuat1SV(p->info);
	}
}

int Dem_SV(LIST l)
{
	int dem = 0;
	Node* p = l.pHead;
	while (p != NULL)
	{
		if (p->info.dTB >= 5.5)
			dem++;
		p = p->pNext;
	}
	return dem;
}
float TimDTBMAX(LIST l)
{
	Node* p;
	float diemtbmax;
	diemtbmax = 0;
	for (p = l.pHead; p != NULL; p = p->pNext)
	{
		if (diemtbmax < p->info.dTB)
			diemtbmax = p->info.dTB;
	}
	return diemtbmax;


}
LIST DanhSachSVMax(LIST l) {
	float dtbMax = TimDTBMAX(l);
	LIST kq;
	CreateList(kq);
	for (Node* p = l.pHead; p != NULL; p = p->pNext)
	{
		if (p->info.dTB == dtbMax)
			InsertTail(kq, p->info);
	}
	return kq;
}
void DanhSachSVMax_C2(LIST l) {
	float dtbMax = TimDTBMAX(l);

	for (Node* p = l.pHead; p != NULL; p = p->pNext)
	{
		if (p->info.dTB == dtbMax)
			Xuat1SV(p->info);
	}
	return;
}
void HoanVi(Data& a, Data& b)
{
	Data temp = a;
	a = b;
	b = temp;


}

void SelectionSortDTB(LIST& l)
{
	Node* p, * q, * min;
	p = l.pHead;
	while (p != NULL) {
		q = p;
		min = q;
		while (q != l.pTail) {
			if (q->info.dTB < min->info.dTB)
				min = q;
			q = q->pNext;
		}
		HoanVi(p->info, min->info);

		p = p->pNext;
	}
}
