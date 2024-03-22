def fact(x):
    if x == 0 or x == 1:
        x = x * 1
        return x
    else:
        x = x * fact(x-1)
        return x

a = int(input("Enter a number"))
print(fact(a))
