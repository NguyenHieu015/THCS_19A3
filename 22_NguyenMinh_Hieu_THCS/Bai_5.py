'''
Bài 5:
'''

n = int(input("Nhập n: "))
S1 = 0

for x in range(0,n+1,1):
    S1 += x
print(S1)

""""""

S2 = 1

for i in range(1,n):
    S2 = S2 * i
print(S2)

""""""

S3 = 0
for i in range(1, n+1):
    S3 += ((-1)**(i+1)) / i

print(S3)

""""""

S4 = 0

for k in range(1,n+1):
    S4 += k / (k+2)

print(S4)