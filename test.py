def first_unique_letter(s):
    letter_count = {}

    # Count the occurrences of each letter
    for letter in s:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    # Find the first unique letter
    for letter in s:
        if letter_count[letter] == 1:
            return letter

    return ""


# Take user input to test the function
input_string = input("Enter a string: ")
result = first_unique_letter(input_string)

if result:
    print(f"The first unique letter is: {result}")
else:
    print("xoxoxo")
