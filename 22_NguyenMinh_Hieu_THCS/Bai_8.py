'''
Bài 8: Nhập cân nặng (kg) và chiều cao (mét). Tính chỉ số BMI theo công thức BMI
= cân nặng / (chiều cao * chiều cao). In kết quả BMI ra màn hình, làm tròn đến 2 chữ
số thập phân.
'''
a, b = map(float, input("Nhập cân nặng(kg) và chiều cao(m): ").split(","))
BMi = a / (b * b)
BMI = "%.2f" %(BMi)
print(BMI)
