'''
Bài 10: Nhập mức lương cơ bản và số ngày công trong tháng từ bàn phím.
• Lương một ngày được tính bằng lương_cơ_bản / 22.
• Tiền thưởng là 10% nếu số ngày công trên 22 ngày.
• Tiền phạt là 5% nếu số ngày công dưới 22 ngày.
Tính và in ra tổng tiền lương thực nhận của nhân viên
'''
luong_co_ban = float(input("Nhập mức lương cơ bản: "))
ngay_cong = int(input("Nhập số ngày công: "))
luong_mot_ngay = luong_co_ban / 22
luong_chinh = luong_mot_ngay * ngay_cong
thuong = luong_co_ban * 0.10 * (ngay_cong > 22)
phat   = luong_co_ban * 0.05 * (ngay_cong < 22)
tong_luong = luong_chinh + thuong - phat
print(f"Lương thực nhận của nhân viên là: ", tong_luong)
