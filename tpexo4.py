def maximum(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Programme principal
a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))
c = float(input("Troisième nombre : "))
max_val = maximum(a, b, c)
print(f"Maximum : {max_val}")