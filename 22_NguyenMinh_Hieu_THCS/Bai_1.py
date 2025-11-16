'''
Bài 1: Nhập giá sản phẩm và số lượng mua từ bàn phím. Tính tổng chi phí và thuế
VAT (10%). In tổng tiền phải trả, làm tròn đến 2 chữ số thập phân.
'''
sp, sl = map(float, input("Giá sản phẩm và số lượng: ").split(","))
abc = ((sp*sl) + (sp*sl)*0.1)
xyz = " %.2f "%(abc)
print("Số tiền cần phải trả là", xyz)