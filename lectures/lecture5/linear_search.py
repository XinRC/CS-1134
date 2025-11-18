# linear search through an array

def linear_search(array_lst, target):
    found = False
    for i in array_lst:
        if i == target:
            print(f"Found \"{target}\" at index {i} of the array")
            found = True
    if found == False:
        print(f"{target} was not found in the array")

def main():
    array_lst = [1,2,3,4,5,6,7,8,9]
    target = 4
    target2 = 10

    linear_search(array_lst, target)
    linear_search(array_lst, target2)

if __name__ == "__main__":
    main()