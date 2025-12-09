'''
Bài 11: Viết một hàm lambda để tính tích của ba số bất kỳ.
'''
x, y, z = map(float,input("Nhập 3 số bất kỳ x, y, z(ngăn cách nhau bằng dấu ','): ").split(","))

def tich_ba_so_bat_ky():
    return lambda x, y, z: x*y*z

tich = tich_ba_so_bat_ky()

print(f"Tích của 3 số {x}, {y}, {z} là:", tich(x, y, z))