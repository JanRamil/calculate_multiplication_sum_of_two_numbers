# Calculate the multiplication and sum of two numbers

def calculate_product_or_sum(input_1, input_2):
    # calculate the two input numbers
    product = input_1 * input_2
    
    # calculate the product that is less than 1000
    if product <= 1000:
        return product
    
    else:
        return input_1 + input_2

