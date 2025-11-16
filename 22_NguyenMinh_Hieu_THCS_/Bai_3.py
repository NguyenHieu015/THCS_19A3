'''
Bài 3: Viết chương trình nhập vào mẫu số và tử số của một phân số, trả về kết quả
phân số đã tối giản
'''
a = int(input("Nhập phần tử: "))
b = int(input("Nhập mẫu số: "))

if b == 0:
    print(" Mẫu số phải khác 0!")
else:
    x, y = a, b 

    while b != 0:
        a, b = b, a % b
    
    tuso_gon = x // a
    mauso_gon = y // a

print(f"Phân số rút gọn là: {tuso_gon}/{mauso_gon}")