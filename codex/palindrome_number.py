"""
Problem Set: PALINDROME_NUMBER
Given an array of integers, return the two index of the integers that calculate to the target
"""

def palindrome_number(number):
    number_str = str(number)
    left, right = 0, len(number_str) - 1
    while left <= right:
        if number_str[left] == number_str[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def main():
    number = 121
    print(palindrome_number(number))

if __name__ == "__main__":
    main()
    