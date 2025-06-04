'''
# Python code to print pattern G
'''

def print_g(height):
    width = height // 2 + 1  # Calculate width based on height to make it proportionate

    for i in range(height):
        for j in range(width):
            # Conditions to print the 'G' shape
            if j == 0:  # Left vertical line
                print("*", end="")
            elif i == 0 and j != width - 1:  # Top horizontal line
                print("*", end="")
            elif i == height - 1 and j != width - 1:  # Bottom horizontal line
                print("*", end="")
            elif i == height // 2 and j >= width // 2:  # Middle horizontal line extending to the right
                print("*", end="")
            elif j == width - 1 and i != 0 and i != height - 1 and i >= height // 2:  # Right vertical curve
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line after each row


# Get the height of the 'G' from the user
height = int(input("Enter the height of the 'G' pattern (odd number): "))
print_g(height)

