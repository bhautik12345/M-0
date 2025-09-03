def palindrome(text):
    new_text = "".join(char for char in text if char.isalnum()).lower()
    print(new_text)
    return new_text == new_text[::-1]

print(palindrome("Was it a car or a cat I saw?"))
print(palindrome("Don't nod."))