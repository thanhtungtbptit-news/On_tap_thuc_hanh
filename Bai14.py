n = int(input("Nhập số lượng phần tử: "))

count = 0  # Biến đếm số chẵn

for i in range(n):
    x = int(input(f"Nhập số thứ {i + 1}: "))
    if x % 2 == 0:      # Kiểm tra số chẵn
        count += 1

print("Có", count, "số chẵn trong dãy.")
