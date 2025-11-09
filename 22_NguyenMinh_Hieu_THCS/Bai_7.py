'''
Bài 7: Nhập tên đăng nhập và mật khẩu từ bàn phím. Kiểm tra quyền truy cập nếu
tên đăng nhập là "admin" và mật khẩu không phải "password123" (chỉ sử dụng kiến
thức đã học).
'''
a = input("Tên đăng nhập: ")
b = input("Vui lòng nhập mật khẩu: ")

dang_nhap = (a == "admin") and (b != "password123")

print("Đăng nhập thành công"*dang_nhap + "Đăng nhập không thành công"*(not dang_nhap))