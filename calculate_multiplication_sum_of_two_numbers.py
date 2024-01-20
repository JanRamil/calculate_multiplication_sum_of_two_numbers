# Calculate the multiplication and sum of two numbers
# Exercise 1

# pseudocode

# Create a start by indicating the calculate_product_or_sum
def calculate_product_or_sum(input_1, input_2):
    # calculate the two input numbers
    product = input_1 * input_2
    
    # calculate the product that is less than 1000
    if product <= 1000:
        return product
    
    else:
        return input_1 + input_2
    
input_1 = int(input("Enter the first number: "))
input_2 = int(input("Enter the second number: "))

result = calculate_product_or_sum(input_1, input_2)
print("Result:", result)

