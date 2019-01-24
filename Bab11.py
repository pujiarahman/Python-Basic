x = 10

def contoh():
    a = 8
    print(a)

# can do this
# print(a)
contoh()

def contoh1():
    a = 8
    print(a)
    #can do this
    # x += 1
    y = x + 1
    print(y)

contoh1()

def contoh2():
    a = 8
    print(a)
    y = x + 1
    print(y)
    return y

y = contoh2()
print(y)

def contoh3():
    global x
    x += 1
    print(x)

contoh3()
