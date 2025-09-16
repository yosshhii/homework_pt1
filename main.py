def main():
    print("Hello Boris Ulitin! Print two integer numbers:")
    a = int(input())
    b = int(input())
    print(f'Sum of numbers: {sum(a, b)}')
    print(f'Product of numbers: {product(a, b)}')
    

def sum(a, b):
    return a + b


def product(a, b):
    return a * b


if __name__ == "__main__":
    main()
