'''
Bài 10: Viết hàm đệ quy tim_so_fibonacci(n) để tìm số Fibonacci thứ n trong dãy số.
'''

n = int(input("Nhập n: "))

def tim_so_fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)

so_fibonacci_thu_n = tim_so_fibonacci(n)
print(f"Số fibonacci thứ {n} là: {so_fibonacci_thu_n}")