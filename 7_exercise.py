result = []


def FB():
    b = input("Zadej B: ")
    if b == "*":
        FA()
        b = input ("Zadej B: ")
    else: 
        FB()
        b = input ("Zadej B: ")
        result.append(b)

    




def FA():
    a = input ("Zadej A: ")
    if  a == "*":
        result.append(a)
    else:
        if a == "+":
            FB ()
            a = input ("Zadej A: ")
            result.append(a)
        else:
            FA()
            result.append(a)

FA()
print(result)




