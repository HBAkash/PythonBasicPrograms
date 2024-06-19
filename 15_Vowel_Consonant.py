def alpha(char):
    char = char.lower()
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char =='u':
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")

alpha('a')
alpha('m')
alpha("O")
alpha("H")