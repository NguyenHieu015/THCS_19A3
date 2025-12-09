'''
Bài 13: Viết một hàm lambda để kiểm tra một số có phải là số dương hay không, trả
về True hoặc False.
'''

def kiem_tra():
    return lambda n : n > 0

n = float(input("Nhập số cần kiểm tra: "))
check = kiem_tra()
print(check(n))