password = input("Enter a password :")
cap = int(0)
small = int(0)
dig = int(0)
spec = int(0)
for i in range(0,len(password)):
    if password[i].isupper():
        cap += 1
    elif password[i].islower():
        small += 1
    elif password[i].isdigit():
        dig+=1
    elif password[i] == '$' or password[i] == '#' or password[i] == '@':
        spec += 1

yo = bool(cap and small and spec and len(password) > 5 and len(password)<17)

if yo :
    print("Valid password")
else:
    print("Invalid password")