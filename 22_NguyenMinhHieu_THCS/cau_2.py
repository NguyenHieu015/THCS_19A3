'''
Bài 2: Viết hàm giai_phuong_trinh_bac_nhat(a, b) nhận vào hai hệ số a và b của
phương trình ax+b=0. Hàm sẽ in ra nghiệm của phương trình hoặc thông báo vô
nghiệm/vô số nghiệm.
'''

def giai_phuong_trinh_bac_nhat(a, b):

    if(a == 0):
        if(b == 0):
            print("phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        x = -b / a
        print(f"Nghiệm của phương trình {a}x + {b} là: {x}")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
adc = giai_phuong_trinh_bac_nhat(a, b)
print(adc)