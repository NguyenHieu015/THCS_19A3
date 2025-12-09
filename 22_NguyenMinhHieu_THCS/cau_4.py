'''
Bài 4: Viết hàm tinh_trung_binh_cong(a, b, c) nhận vào ba số. 
Hàm sẽ tính và trả về giá trị trung bình cộng của chúng.
'''

def tinh_trung_binh_cong(a, b, c):
    return sum([a, b, c]) / len([a, b, c])

a, b, c = map(int, input("Nhập 3 số a, b, c (cách nhau bằng dấu phẩy): ").split(","))
ket_qua = tinh_trung_binh_cong(a, b, c)
print(f"Giá trị trung bình của {a}, {b}, {c} là:", ket_qua)