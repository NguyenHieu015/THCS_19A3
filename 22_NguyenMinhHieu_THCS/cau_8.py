'''
Bài 8: Viết hàm tim_so_le_lon_nhat(a, b, c) nhận vào ba số nguyên. 
Hàm sẽ trả về số lẻ lớn nhất trong ba số đó. 
Nếu không có số lẻ nào, hàm trả về một giá trị đặc biệt (ví dụ: -1) để báo hiệu.
'''
a = int(input("Nhập số a cần so sánh: "))
b = int(input("Nhập số b cần so sánh: "))
c = int(input("Nhập số c cần so sánh: "))

def tim_so_le_lon_nhat(a, b, c):
    return list(filter(lambda x: x % 2 != 0, [a, b, c]))

so_le = tim_so_le_lon_nhat(a, b, c)
if(a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
    print("-1")
else:    
    print("Số lẻ lớn nhất là:", max(so_le))