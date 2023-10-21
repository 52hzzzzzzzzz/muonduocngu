#include <iostream>
#include <conio.h>
#include <cstddef>
#include <string>
#include<iomanip>

using namespace std;

#include "Thuvien.h"
#include "Menu.h"

void ChayChuongTrinh();


int main() {
	ChayChuongTrinh();
	return 1;

}

void ChayChuongTrinh() {
	LIST l, kq;
	int soMenu = 5,

		menu;
	Data a[MAX]={ 
		{"182222", "Nguyen Van Anh", 2003, 8.5},
		{"231111", "Tran Van Anh", 2000, 5.5},
		{"231112", "Nguyen Lan Huong", 2003, 8.5},
		{"200111", "Ngo Van Tung", 2000, 3.5},
		{"192222", "Tran Hung", 2010, 8.5}
	}; 
	int	n = 5;
	do
	{
		system("CLS");
		menu = ChonMenu(soMenu);
		XuLyMenu(menu, a, n);
	} while (menu>0);
	
	_getch();
}