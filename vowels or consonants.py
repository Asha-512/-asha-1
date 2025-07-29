def print_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_list = []
    consonant_list = []
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_list.append(char)
            else:
                consonant_list.append(char)
    print("vowels:",''.join(vowel_list))    
    print("consonants:",''.join(consonant_list)) 
text = input("enter a string:")
print_vowels_consonants(text)   


