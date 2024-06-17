def is_palindrome(strings):
    strings = strings.lower() #capitalization is neglected
    old = strings
    new = strings[::-1]
    if old == new:
        print("Palindrome")
    else:
        print("Not palindrome")

is_palindrome("abba")
is_palindrome("Hridoy")
is_palindrome("madam")