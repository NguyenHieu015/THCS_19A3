'''
Bài 7: Viết hàm tinh_tong_so_hoan_hao(a, b) nhận vào hai số nguyên dương a và b
(với a <= b). Hàm sẽ tính và trả về tổng của tất cả các số hoàn hảo trong khoảng từ a
đến b.
'''

a = int(input("Enter the starting point(a): "))
b = int(input("Enter the end point(b): "))
if(a > b):
    print(f"Điểm bắt đầu phải nhỏ hơn điểm kết thúc (a < b)!")
else:

    def tim_so_hoan_hao(n):
        tong_uoc = 0

        for i in range(1, n):

            if (n % i == 0):
                tong_uoc += i

        return tong_uoc == n
    def tinh_tong_so_hoan_hao(a, b):
        tong = 0

        for n in range(a, b + 1):

            if(tim_so_hoan_hao(n)):

                tong += n

        return tong
    tong_so_hoan_hao = tinh_tong_so_hoan_hao(a, b)

    print(f"Tổng giá trị của các số hoàn hảo trong khoảng từ {a} đến {b} là:\n", tong_so_hoan_hao)
            