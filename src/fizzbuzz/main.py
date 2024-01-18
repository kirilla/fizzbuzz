import argparse
import itertools as its

def main():
    parser = argparse.ArgumentParser(description='Prints the FizzBuzz sequence.',
                                     prog='fizzbuzz',
                                     epilog="""
                                     Algorithms: 
                                     basic, oneliner, recursive, functional, itertools
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
        elif args.algorithm == 'functional':
            print(fizz_functional(15))
        elif args.algorithm == 'itertools':
            print(fizz_itertools(15))
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

def fizz_functional(n):
    return [
            "Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i for i in range(1, n+1)
            ]

def fizz_itertools(n):
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    return [word or i for i, word in zip(its.count(1), fizzes_buzzes)][:n]


if __name__ == "__main__":
    main()
