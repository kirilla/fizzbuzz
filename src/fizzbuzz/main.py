import argparse

def main():
    parser = argparse.ArgumentParser(description = 'Prints the FizzBuzz sequence.',
                                     prog = 'fizzbuzz')
    
    parser.add_argument('algorithm', nargs='?', type=str, 
                        help='the fizzbuzz algorithm to use')

    args = parser.parse_args()

    if args.algorithm:
        if args.algorithm == 'basic':
            fizz_basic()
        elif args.algorithm == 'oneliner':
            fizz_oneliner()
        else:
            parser.print_usage()
    else:
        parser.print_usage()

def fizz_basic():
    print('Basic')
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
    print('Oneliner:')
    print('\n'.join("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or str(i) for i in range(1,16)))

if __name__ == "__main__":
    main()
