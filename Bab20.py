try:
    print('try...')
    # Name Error
    print(m)
    
    # Type Error
    print(5+'10')
    
except TypeError as t:
    print('Type Error')
    print(str(t))

except NameError as n:
    print('Name Error')
    print(str(n))

except Exception as e:
    print('General Exception')
    print(str(e))

