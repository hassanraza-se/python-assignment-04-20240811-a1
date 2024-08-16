# Python Programming Assignment 04

def number_to_ordinal(num: int) -> str:
    """ convert number to ordinal """
    if 11 <= num % 100 <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return f"{num}{suffix}"

def is_prime(num: int) -> bool:
    """ check if number is prime """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():

    name: str = input("Enter your name: ")
    numbers: [int] = []

    for x in range(1, 4):
        numbers.append(int(input(f"Enter your {number_to_ordinal(x)} favorite number: ")))

    print(f"\nHello, {name}! Let's explore your favorite numbers!")

    even_odd = [(num, 'even' if num % 2 == 0 else 'odd') for num in numbers]
    for num, status in even_odd:
        print(f"The number {num} is {status}.")

    number_square = [(num, num**2) for num in numbers]
    for num, square in number_square:
        print(f"The number {num} and its square: ({num}, {square}).")

    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}.")

    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number, but it's still a cool number!")

if __name__ == '__main__':
    main()
