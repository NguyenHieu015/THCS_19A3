'''
Bài 3: Viết hàm kiem_tra_so_armstrong(n) nhận vào một số nguyên dương n. Hàm
này sẽ trả về True nếu n là số Armstrong (tổng các lũy thừa bậc 3 của các chữ số của
nó bằng chính nó, ví dụ: 153) và False nếu không.
'''
def kiem_tra_so_armstrong(n):
    con_ca_vang = str(n)
    check_so_armstrong = sum(int(con_ca)**3 for con_ca in con_ca_vang)
    return check_so_armstrong == n

n = int(input("Nhập n: "))
check = kiem_tra_so_armstrong(n)
print(check)