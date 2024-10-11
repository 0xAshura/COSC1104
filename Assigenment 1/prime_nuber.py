10# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Function to get a positive whole number from the user
def get_positive_number():
    while True:
        try:
            num = int(input("Enter a positive whole number: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to find the previous prime number
def previous_prime(number):
    for i in range(number - 1, 1, -1):
        if is_prime(i):
            return i
    return None

# Function to find the next prime number
def next_prime(number):
    i = number + 1
    while True:
        if is_prime(i):
            return i
        i += 1

# Main function to drive the program
def main():
    num = get_positive_number()
    
    prev_prime_num = previous_prime(num)
    if prev_prime_num:
        print(f"The prime number before {num} is {prev_prime_num}.")
    else:
        print(f"There is no prime number before {num}.")
    
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        print(f"{num} is not a prime number. Divisors: {divisors}")
    
    next_prime_num = next_prime(num)
    print(f"The next prime number after {num} is {next_prime_num}.")
    
if __name__ == "__main__":
    main()
