def multiply(x):
    product = 1
    for i in x:
        product *= i
    return product

x = (3, 4, 5, 9, 2)
print(f"The product of values from tuple: {x} equals:", multiply(x))
