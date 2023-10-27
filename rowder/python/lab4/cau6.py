import openpyxl
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

mon_hoc = [
    "Lập Trình Python",
    "Lập Trình Java",
    "Công nghệ phần mềm",
    "Phát triển ứng dụng web",
]


def register():
    mssv = mssv_entry.get()
    ten = ten_entry.get()
    ngay_sinh = ngay_sinh_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    hoc_ky = hoc_ky_var.get()
    nam_hoc = nam_hoc_var.get()

    selected_mon_hoc = []

    for mon, var in mon_hoc_vars.items():
        if var.get():
            selected_mon_hoc.append(mon)

    save_to_excel(mssv, ten, ngay_sinh, email, phone, hoc_ky, nam_hoc, selected_mon_hoc)
    messagebox.showinfo("Thông báo", "Đăng ký thành công!")


def save_to_excel(mssv, ten, ngay_sinh, email, phone, hoc_ky, nam_hoc, mon_hoc):
    file_path = "D:\\third year\\python programing\\lab4\\excel.xlsx"

    if file_path:
        try:
            wb = openpyxl.load_workbook(file_path)
        except FileNotFoundError:
            wb = openpyxl.Workbook()

        sheet = wb.active
        sheet.append(
            [
                "Mã số sinh viên",
                "Họ Tên",
                "Ngày sinh",
                "Email",
                "Số điện thoại",
                "Học kỳ",
                "Năm học",
            ]
            + mon_hoc
        )
        sheet.append([mssv, ten, ngay_sinh, email, phone, hoc_ky, nam_hoc] + mon_hoc)
        wb.save(file_path)
        messagebox.showinfo("Thông báo", f"Đã lưu vào {file_path}")
    else:
        messagebox.showinfo("Thông báo", "Không tìm thấy file")


root = tk.Tk()
root.title("Đăng ký học phần")

main_frame = tk.Frame(root)
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


padding = 20

main_label = ttk.Label(
    main_frame,
    text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN",
)
main_label.grid(row=0, column=1, padx=5, pady=1, sticky=tk.W)

mssv_label = ttk.Label(main_frame, text="Mã số sinh viên:")
mssv_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
mssv_entry = ttk.Entry(main_frame, width=51)
mssv_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

ten_label = ttk.Label(main_frame, text="Họ Tên:")
ten_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
ten_entry = ttk.Entry(main_frame, width=51)
ten_entry.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

ngay_sinh_label = ttk.Label(main_frame, text="Ngày sinh:")
ngay_sinh_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
ngay_sinh_entry = ttk.Entry(main_frame, width=51)
ngay_sinh_entry.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

email_label = ttk.Label(main_frame, text="Email:")
email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
email_entry = ttk.Entry(main_frame, width=51)
email_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

phone_label = ttk.Label(main_frame, text="Số điện thoại:")
phone_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)
phone_entry = ttk.Entry(main_frame, width=51)
phone_entry.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

hoc_ky_label = ttk.Label(main_frame, text="Học kỳ :")
hoc_ky_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
hoc_ky_var = tk.StringVar()
hoc_ky_var.set("1")
hoc_ky_entry = ttk.Entry(main_frame, width=51, textvariable=hoc_ky_var)
hoc_ky_entry.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

nam_hoc_label = ttk.Label(main_frame, text="Năm học:")
nam_hoc_label.grid(row=7, column=0, padx=10, pady=5, sticky=tk.W)
nam_hoc_options = ["2022-2023", "2023-2024", "2024-2025"]
nam_hoc_var = tk.StringVar()
nam_hoc_combobox = ttk.Combobox(
    main_frame, textvariable=nam_hoc_var, values=nam_hoc_options, width=48
)
nam_hoc_combobox.grid(row=7, column=1, padx=5, pady=5, sticky=tk.W)
nam_hoc_combobox.set(nam_hoc_options[0])

mon_hoc_label = ttk.Label(main_frame, text="Chọn môn học:")
mon_hoc_label.grid(row=8, column=0, padx=10, pady=5, sticky=tk.W)

mid = len(mon_hoc) // 2
mon_hoc_col1 = mon_hoc[:mid]
mon_hoc_col2 = mon_hoc[mid:]

mon_hoc_vars = {}

for i, mon in enumerate(mon_hoc_col1):
    var = tk.BooleanVar()
    mon_hoc_vars[mon] = var
    mon_hoc_checkbutton = tk.Checkbutton(
        main_frame,
        text=mon,
        variable=var,
    )
    mon_hoc_checkbutton.grid(
        row=8 + i, column=1, padx=1, pady=2, columnspan=2, sticky=tk.W
    )

for i, mon in enumerate(mon_hoc_col2):
    var = tk.BooleanVar()
    mon_hoc_vars[mon] = var
    mon_hoc_checkbutton = tk.Checkbutton(
        main_frame,
        text=mon,
        variable=var,
    )

    mon_hoc_checkbutton.grid(row=8 + i, column=2, padx=1, pady=2, sticky=tk.W)


register_button = tk.Button(
    main_frame,
    text="Đăng ký",
    command=register,
    width=10,
    height=1,
)
register_button.grid(row=10 + len(mon_hoc), column=0, columnspan=4)

thoat_button = tk.Button(
    main_frame,
    text="Thoát",
    command=root.quit,
    width=10,
    height=1,
)
thoat_button.grid(row=10 + len(mon_hoc), column=2, columnspan=4)

root.mainloop()
