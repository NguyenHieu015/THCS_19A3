'''
Bài 9: Viết hàm đệ quy tinh_tong_chu_so(n) nhận vào một số nguyên dương n và trả
về tổng các chữ số của nó.
'''
def tinh_tong_chu_so(n):
    con_ca = str(n)
    tong = sum(int(i) for i in con_ca)
    return tong

n = int(input("Nhập số n: "))

if (n > 0):
    zzz = str(n)
    tong_chu_so = tinh_tong_chu_so(n,)
    print(f"Tổng của {zzz[0]}, {zzz[1]}, {zzz[2]} là:", tong_chu_so)
else:
    print(f"{n} không phải số nguyên dương!")