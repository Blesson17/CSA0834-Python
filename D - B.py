# Function to convert decimal to binary
def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

# Example usage
decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print(f"Binary equivalent: {binary_number}")
