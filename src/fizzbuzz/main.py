import argparse

def main():
    parser = argparse.ArgumentParser(description='Prints the FizzBuzz sequence.',
                                     prog='fizzbuzz',
                                     epilog="""
                                     Algorithms: 
                                     basic, oneliner, recursive
                                     """)
    
    parser.add_argument('algorithm', type=str, nargs='?', 
                        help='the fizzbuzz algorithm to use')

    args = parser.parse_args()

    if args.algorithm:
        if args.algorithm == 'basic':
            fizz_basic()
        elif args.algorithm == 'oneliner':
            fizz_oneliner()
        elif args.algorithm == 'recursive':
            print(fizz_recursive_descending(15))
        else:
            parser.print_usage()
    else:
        parser.print_usage()

def fizz_basic():
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def fizz_oneliner():
    print('\n'.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,16)))

def fizz_recursive_descending(n):
    if n == 0:
        return []

    if n % 3 == 0 and n % 5 == 0:
        result = "FizzBuzz"
    elif n % 3 == 0:
        result = "Fizz"
    elif n % 5 == 0:
        result = "Buzz"
    else:
        result = n

    return fizz_recursive_descending(n - 1) + [result]


if __name__ == "__main__":
    main()
