a = open('Tulis.txt', 'r').read()
print(a)


b = open('Tulis.txt', 'r').readlines()
print(b)


c = open('Tulis.txt', 'r').read()
d = c.split('\n')
print(d)
