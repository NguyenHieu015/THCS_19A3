'''
Bài 2: Viết chương trình nhập vào 2 số bất kì, tìm ước chung lớn nhất của 2 số đó
'''
a, b = map(int, input("Nhập 2 số bất kì: ").split(" "))

x, y = a, b 

while b != 0:
    a, b = b, a % b

print(f"UCLN của {x} và {y} là: {a}")
