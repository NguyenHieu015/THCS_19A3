'''
Bài 2: Nhập tổng số kẹo và số học sinh từ bàn phím. Tính số kẹo mỗi học sinh nhận
được và số kẹo còn thừa (biết số kẹo mỗi học sinh nhận đều như nhau).
'''
so_keo, so_hs = map(int, input("Tổng số kẹo và số học sinh là: ").split(","))

keo_tren_hs = so_keo // so_hs

keo_con_lai = so_keo % so_hs

print("Mỗi học sinh sẽ nhận được ", keo_tren_hs, "cái kẹo và còn dư ", keo_con_lai)