# linear search through an array

def linear_search(array_lst, target):
    for i in array_lst:
        if i == target:
            return f"Found \"{target}\" at index {i} of the array"
    return (f"{target} was not found in the array")

def main():
    array_lst = [1,2,3,4,5,6,7,8,9]
    target = 4
    target2 = 10

    print(linear_search(array_lst, target))
    print(linear_search(array_lst, target2))

if __name__ == "__main__":
    main()