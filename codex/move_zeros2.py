'''
Problem Set: MOVE ZEROS
Given an array of random integers, move all the zeros to the back of the array.
> Uses a for loop 
'''

def move_zeros(lst):
    left = 0
    for right in range(len(lst)):
        if lst[right] != 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
    return lst

def main():
    lst = [0,1,0,3,12]

    print(move_zeros(lst))

if __name__ == "__main__":
    main()