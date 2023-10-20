#!/usr/bin/python3
import sys


def factorize(number):
    factors = []
    for i in range(2, int(number**0.5) + 1):
        while number % i == 0:
            factors.append(i)
            number //= i
    if number > 1:
        factors.append(number)
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                print(f"{number}={'*'.join(map(str, factors))}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print(f"Invalid number in file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
