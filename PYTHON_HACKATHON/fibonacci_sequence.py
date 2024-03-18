def fibonacci(n):
    """Generate n terms of the fibonacci sequence."""
    sequence = []
    for i in range(n):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            # Add the sum of the last two elements to generate the next element
            next_element = sequence[i-1] + sequence[i-2]
            sequence.append(next_element)
    return sequence

# Ask the user for the number of terms they want
n = int(input("Enter the number of terms you want in the Fibonacci sequence: "))

# Generate and print the Fibonacci sequence
fib_sequence = fibonacci(n)
print("The first", n, "terms of the Fibonacci sequence are:", fib_sequence)
