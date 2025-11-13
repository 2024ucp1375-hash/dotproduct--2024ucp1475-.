# Dot product of two vectors

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("Vectors must be of same length")

    result = 0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result

# Example usage
a = [1, 2, 3]
b = [4, 5, 6]

print("Dot product:", dot_product(a, b))

