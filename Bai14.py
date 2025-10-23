n=int(input("Nhập một số nguyên dương n: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count +=1
print(f"Dãy {n} có {count} số chẵn ")