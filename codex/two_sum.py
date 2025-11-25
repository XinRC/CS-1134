"""
Problem Set: TWO SUM
Given an array of integers, return the two index of the integers that calculate to the target
"""
def two_sum(lst, target):
    left, right = 0, len(lst) - 1 

    while left <= len(lst) - 1 and right >= 0:
        if lst[left] + lst[right] == target:
            return [left, right]
        elif lst[left] + lst[right] > target:
            right -= 1
        elif lst[left] + lst[right] < target:
            left += 1

def main():
    array_lst = [4,6,7,3,5,9]
    target = 11
    print(two_sum(array_lst, target))

if __name__ == "__main__":
    main()