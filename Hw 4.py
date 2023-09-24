# Sum and multiplication of even and odd numbers.
def sum_even_and_product_odd(arr: list):
    sum_even = 0
    product_odd = 1

    for num in arr:
        if num % 2 == 0:
            sum_even += num
        elif num % 2 != 0:
            product_odd *= num

    return [sum_even, product_odd]


result = sum_even_and_product_odd([1, 2, 3, 4])
print(result)


# 2 - Sum between range values
def sum_between_range(arr: list, min_val: int, max_val: int):
    total_sum = 0

    for num in arr:
        if min_val <= num <= max_val:
            total_sum += num
    return total_sum


arr = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
min_val = 3
max_val = 7
result = sum_between_range(arr, min_val, max_val)
print(result)

# 3 - Stock price 2
def buy_and_sell_stock(prices: list):
    # Initialize the variable 'maximum' to store the maximum profit, starting at 0
    maximum = 0

    # Loop through the list of prices; stop one element before the last to avoid index out-of-bounds
    for i in range(len(prices) - 1):
        # Check if the next day's price is higher than the current day's
        if prices[i + 1] > prices[i]:
            # If it is, add the difference between the two prices to 'maximum'
            maximum += prices[i + 1] - prices[i]

    # Return the calculated maximum profit after the loop ends
    return maximum


# Test the function with the example
prices = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock(prices)
print(result)  # Output should be 7

# 4 - Increment a Number

def plus_one(arr: list):
    # Add 1 to the last digit of the number
    arr[-1] += 1

    # Loop through the array in reverse, starting from the last element
    for i in reversed(range(1, len(arr))):
        # If the current digit is not 10, there's no carry-over, and we can break the loop
        if arr[i] != 10:
            break
        # Set the current digit to 0 because we have a carry-over
        arr[i] = 0
        # Add 1 to the preceding digit (i-1) to handle the carry-over
        arr[i - 1] += 1

    # Check if the most significant digit (first digit) has a carry-over
    if arr[0] == 10:
        # Set the first digit to 1
        arr[0] = 1
        # Append a 0 to the array to handle the carry-over from the most significant digit
        arr.append(0)


# Test the function with an example
number = [1, 2, 9]
plus_one(number)
print(number)  # Output should be [1, 3, 0]
