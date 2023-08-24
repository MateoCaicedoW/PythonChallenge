user_input = input("Enter a string: ")
print("The input is a palindrome." if user_input.lower() == user_input.lower()[::-1] else "The input is not a palindrome.")