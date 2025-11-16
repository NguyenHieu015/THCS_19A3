'''
Bài 4: Viết chương trình nhập vào n, tìm tất cả các số nguyên tố nhỏ hơn n
'''
n = int(input("Nhập n: "))
li = 0

if n <= 1:
    print(f"{n} không phải số nguyên tố!")

else:
    for i in range(4,n):
        for u in range (2,i):
            if(i%u==0):
                li += 1
        if li == 0:
            print(i)
        else:
            li = 0
