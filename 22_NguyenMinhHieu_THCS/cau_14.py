'''
Bài 14: Viết một hàm lambda để tính tổng của hai số.
'''

def tong_hai_so(a, b):
    return lambda a, b: a + b

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
tong = tong_hai_so(a, b)
print(f"Tổng của 2 số {a} và {b} là: {tong(a, b)}")