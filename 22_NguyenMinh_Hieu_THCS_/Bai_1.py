'''
Bài 1: Viết chương trình nhập vào một số kiểm tra xem số đó có phải số chính phương
hay không?
'''
n = int(input("Nhập số cần kiểm tra: "))

abc = n ** 0.5

if abc.is_integer():
    print(f"{n} Là số chính phương!")
    
else:
    print(f"{n} Không là số chính phương!")