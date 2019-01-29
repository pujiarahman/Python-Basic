a = [1,2,3,4,5,6]
b = ('anggur', 'sirsak', 'jambu')


print(a)
print(b)

print(a[5])
print(b[2])

a.append(7)
print(a)

# Tidak Bisa
# b.append('pepaya')
# print(b)

a.insert(7,8)
print(a)

# Tidak Bisa
# b.insert(8,9)
# print(b)

a.remove(1)
print(a)
print(a.index(6))
print(a.count(3))


