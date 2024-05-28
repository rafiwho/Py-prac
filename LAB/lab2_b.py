list = []
n = int(input("How many number do you enter ?: "))
for i in range(0,n):
    x = int(input())
    list.append(x)

even = int(0)
odd = int(0)
for x in list:
   even += x&1==0
   odd += x&1

print("Number of even numbers : "+str(even))
print("Number of odd numbers : "+str(odd))
