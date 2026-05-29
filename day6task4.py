text=input("Enter the sentence:")

# 1. Convert to uppercase
print("Uppercase:", text.upper())
# 2. Convert to lowercase
print("Lowercase:", text.lower())
# 3. Capitalize first letter
print("Capitalized:", text.capitalize())
# 4. Title Case (first letter of each word)
print("Title Case:", text.title())
# 5. Strip whitespace
print("Stripped:", text.strip())
# 6. Replace 'a' with '@'
print("Replaced 'a' with '@':", text.replace('a', '@'))
# 7. Check if all characters are alphabetic
print("Is Alphabetic:", text.isalpha())
# 8. Check if alphanumeric
print("Is Alphanumeric:", text.isalnum())
# 9. Check if digits only
print("Is Digit:", text.isdigit())
# 10. Count how many times 'e' appears
print("Count of 'e':", text.count('e'))
# 11. Check if string ends with "ing"
print("Ends with 'ing':", text.endswith("ing"))
