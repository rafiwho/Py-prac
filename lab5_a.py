list  = []
word = " "
while len(word):
    word = input()
    if len(word):
        list.append(word)


for i in list:
    dec = int(i,2)
    if dec%5==0:
        print(i,end=" ")
    