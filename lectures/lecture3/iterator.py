#generator demo
def generate():
    iterating = 18
    yield iterating 
    yield iterating + 2

#generator demo
def main(): 
    # iterator demo
    nums = [19, 24, 17, 98]
    nums_iterator = iter(nums)

    for i in nums:
        print(next(nums_iterator), end=" ") # 19 24 17 98

    '''
    for i in range(len(nums) + 1): 
        print(next(nums_iterator), " ", end='")
    # this code will give you an error since we are trying to 
    # iterate even though we have no more items in the list
    '''

    print("\n")

    # generator demo
    gen = generate()
    print(next(gen), end=" ")
    print(next(gen), end=" ")
    
    '''
    print(next(gen), end=" ")
    # this code would return an error since we don't have another 
    # yield statement to make, giving us a: StopIteration Error
    '''

if __name__ == "__main__":
    main()