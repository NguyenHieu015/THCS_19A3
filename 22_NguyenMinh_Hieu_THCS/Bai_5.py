''''
Bài 5: Nhập số tiền gửi ban đầu và lãi suất hàng năm từ bàn phím. Tính số tiền lãi
nhận được sau 1 tháng, 2 quý, 3 năm (lãi đơn).
'''
a, b = map(float, input("Nhập số tiền gửi ban đầu và lãi suất hàng năm: ").split(","))
lai_suat = a*(1+(b/12))
print("Khoản lãi nhận được sau 1 tháng là", lai_suat - a)
lai_suat_1 = a*(1+(b/2))
print("Khoản lãi nhận được sau 2 quý là", lai_suat_1 - a)
lai_suat_2 = a*(1+(3*b))
print("Khoản lãi nhận được sau 3 năm là", lai_suat_2 - a)