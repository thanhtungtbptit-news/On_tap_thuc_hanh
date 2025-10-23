import random 
so_bi_mat=random.randint(1,10)
doan = 0
while doan != so_bi_mat:
    doan=int(input("Mời bạn đoán số từ 1 đến 10 : "))
    if doan < so_bi_mat:
        print("Số bạn đoán nhỏ hơn số bí mật, mời bạn đoán lại ")
    elif doan > so_bi_mat:
        print("Số bạn đoán lớn hơn số bí mật, mời bạn đoán lại ")
    else:
        print("Chúc mừng bạn đã đoán đúng số bí mật !")