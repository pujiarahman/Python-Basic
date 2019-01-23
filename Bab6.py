a = 1
b = 2
c = 3

if a < b:
    print(a," Lebih Kecil Dari ", b)
if a > b:
    print(a," Lebih Besar Dari ", b)
if a == b:
    print(a, " Sama Dengan ", b)
if a <= b:
    print(a," Lebih Kecil Dari / Sama dengan ", b)

if a == '2':
    print(a,"Sama Dengan 2")

# Tidak Bisa int() < str()
if a < '2':
    print(a,"Lebih Kecil Dari 2")
