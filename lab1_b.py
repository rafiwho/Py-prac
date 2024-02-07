def c_to_f(cel):
    return (cel * 9/5) + 32

def f_to_c(fahr):
    return (5/9) * (fahr - 32)

num = input("Enter a temp: ")

if num[-1].upper() != 'C' or num[-1].upper() != 'F'
    print("Invalid input")

if num[-1].upper() == 'C':
    num = int(num[:-1])
    print(str(num)+" cel is "+str(c_to_f(num))+" in Farhenheit")
else:
    num = int(num[:-1])
    print(str(num)+" cel is "+str(f_to_c(num))+" in Celsius")

    
