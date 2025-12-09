'''
Bài 5: Viết hàm kiem_tra_so_doi_xung(n) nhận vào một số nguyên dương n. Hàm sẽ
trả về True nếu n là số đối xứng (khi đọc xuôi hay ngược đều giống nhau, ví dụ: 121,
353) và False nếu không.
'''

def kiem_tra_so_doi_xung(n):
    con_ca_vang = str(n)
    def chuoi_nguoc(s):
        xyz = ""
        for abc in s:
            xyz = abc + xyz
        return xyz
    con_ca = chuoi_nguoc(con_ca_vang)
    return con_ca_vang == con_ca
    
n = int(input("Nhập n: "))
a = kiem_tra_so_doi_xung(n)
print(a)