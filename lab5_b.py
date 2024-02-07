word = input("Enter a string :")
dig= int(0)
letter = int(0)

for ch in range(0,len(word)):
    dig += word[ch].isdigit()
    letter += word[ch].isalpha()

print("digits = "+str(dig))
print("letters = "+str(letter))