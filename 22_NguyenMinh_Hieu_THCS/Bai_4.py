'''
Bài 4: Nhập một số tiền bằng VNĐ từ bàn phím. Chuyển đổi số tiền đó sang USD (tỷ
giá 1 USD = 24.500 VNĐ) và in kết quả, làm tròn đến 2 chữ số thập phân.
'''
abc = float(input("Nhập số tiền cần đổi: "))
xyz = (abc / 24500)
c = " %.2f " %(xyz)
print(c)