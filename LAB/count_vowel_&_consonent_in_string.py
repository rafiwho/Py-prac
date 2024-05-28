def count_vowels_and_consonants(input_string):
    input_string = input_string.lower()

    vowel_count = 0
    consonant_count = 0

    vowels = set("aeiou")

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    print(f"Vowel count: {vowel_count}")
    print(f"Consonant count: {consonant_count}")

input_string = input("Enter a string: ")
count_vowels_and_consonants(input_string)
