# binary search through an array

def binary_search(array_lst, target):
    target = target;
    start, stop = 0, len(array_lst) - 1

    while (start <= stop):
        midpoint = (start+stop) // 2
        
        if array_lst[midpoint] == target:
            return midpoint
        elif array_lst[midpoint] > target:
            stop = midpoint - 1
        else: 
            start = midpoint + 1
    return "Not found"

def main():
    array_lst = [1,2,3,4,5,6,7,8,9]
    target = 4
    target2 = 15
    print(binary_search(array_lst, target))
    print(binary_search(array_lst, target2))


if __name__ == "__main__":
    main()