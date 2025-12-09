'''
Bài 6: Viết hàm la_so_nguyen_to(n) nhận vào một số nguyên n và trả về True nếu n là số nguyên tố, 
ngược lại trả về False. 
Viết hàm in_so_nguyen_to_trong_khoang(a,b) nhận vào hai số nguyên a và b. 
Sử dụng hàm la_so_nguyen_to để in ra tất cả các số nguyên tố trong khoảng từ a đến b.
'''

def la_so_nguyen_to(n):
    if(n < 2):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
n = int(input("Nhập số cần kiểm tra: "))
snt = la_so_nguyen_to(n)
print(snt)

def in_so_nguyen_to_trong_khoang():
    a = int(input("Nhập số khởi đầu(a): "))
    b = int(input("Nhập số kết thúc(b): "))
    for number in range(a, b+1):
        if(la_so_nguyen_to(number)):
            print(number, "\n")
    
jet_bien_hoa = in_so_nguyen_to_trong_khoang()
print(jet_bien_hoa)