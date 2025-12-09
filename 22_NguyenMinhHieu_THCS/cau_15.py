'''
Bài 15: Nhập vào một số nguyên dương n, viết hàm kiểm tra xem n có phải là số
nguyên tố hay không? Sau đó in ra các số nguyên tố trong khoảng [100, 500].
'''
n = int(input("Nhập số cần kiểm tra n: "))

def kiem_tra_so_nguyen_to(n):
    if(n < 2):
        return False
    for i in range(2, n):
        if(n % i == 0):
            return False
    return True
    
check = kiem_tra_so_nguyen_to(n)
print(check * "Là số nguyên tố" + "Không phải số nguyên tố" * (not check))

def in_ra_so_nguyen_to():
    for i in range(100, 501):
        if(kiem_tra_so_nguyen_to(i)):
            print(i)

in_ra_snt = in_ra_so_nguyen_to()
print(in_ra_snt)