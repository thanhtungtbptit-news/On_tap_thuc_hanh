a=float(input("Nhập vào số kWh tiêu thụ : "))
if a<0:
   print("Giá trị không hợp lệ, vui lòng nhập lại")
if 0<a<50 :
   print("Tổng tiền là : ",1.800*a)
if 51<=a<=100:
   print("Tổng tiền là : " ,1.800*50+a*2000)
if a>100:
    print("Tổng tiền là : " , 1800*50+2000*100+a*2500)
