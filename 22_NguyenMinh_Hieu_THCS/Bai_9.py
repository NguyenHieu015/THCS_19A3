'''
Bài 9: Nhập số kWh điện đã tiêu thụ từ bàn phím. Sau đó, tính và in ra tổng số tiền
điện phải trả dựa trên công thức sau:
• Bậc 1 (0 - 100 kWh): 1.678 VNĐ/kWh
• Bậc 2 (101 - 200 kWh): 1.734 VNĐ/kWh
• Bậc 3 (201 - 300 kWh): 2.014 VNĐ/kWh
'''
kwh = float(input("Nhập số kWh điện đã tiêu thụ: "))
bac1 = min(kwh, 100)
bac2 = min(max(kwh - 100, 0), 100)
bac3 = max(kwh - 200, 0)
#tong_tien = bac1 * 1678 + bac2 * 1734 + bac3 * 2014
#print("Số tiền điện phải trả là: ", tong_tien)
tien = bac2 * 1734
print(tien)