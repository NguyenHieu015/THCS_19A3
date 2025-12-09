'''
Bài 12: Viết một hàm lambda để kiểm tra một số có phải là số chẵn hay không, trả về
True hoặc False.
'''

def Kiem_tra_so_chan():
    return lambda n : n % 2 == 0

n = int(input("Nhập số nguyên cần kiểm tra: "))
chekc = Kiem_tra_so_chan()

print(chekc(n))