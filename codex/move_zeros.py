'''
Problem Set: MOVE ZEROS
Given an array of random integers, move all the zeros to the back of the array 
> Uses a while loop
'''

def move_zeros(lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        if lst[left] == 0 and lst[right] == 0:
            right -= 1
        elif lst[left] == 0 and lst[right] != 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1  
        else:
            left += 1
    return lst

def main():
    lst = [0,1,0,3,12]

    print(move_zeros(lst))

if __name__ == "__main__":
    main()