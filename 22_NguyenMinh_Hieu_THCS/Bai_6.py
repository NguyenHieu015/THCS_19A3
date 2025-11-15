'''
Bài 6: Nhập một năm từ bàn phím. Kiểm tra xem năm đó có phải là năm nhuận không
(chia hết cho 400 hoặc chia hết cho 4 nhưng không chia hết cho 100) (chỉ sử dụng
kiến thức đã học).
'''
a = int(input("Nhập năm cần kiểm tra: "))

nam = (a % 400 == 0) or ((a % 4 == 0) and (a % 100 != 0))

print("Năm nhuận" * nam + "Năm không nhuận" * (not nam))
