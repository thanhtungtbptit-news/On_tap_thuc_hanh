a=int(input("Nhập một năm : "))
if a%400==0 or a%4==0 and a%100!=0:
   print("Năm nhuận ")
else:
   print("Năm không nhuận ")