# Problem 8: Check if a string is palindrome
# Find and fix the error

def is_palindrome(text):
    clean_text = text.lower()
    return clean_text == clean_text[::-1]

word = "Racecar"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
