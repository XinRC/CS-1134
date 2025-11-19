def bubble_sort(lst):
  n = len(lst)

  for i in range(n - 1): #  n - 1 is to avoid going out of the bounds
    for j in range(n - i - 1): #  n - i is to avoid the sorted portion and the -1 is to go out of the bounds
      if lst[j] > lst[j + 1]:
        lst[j], lst[j + 1] = lst[j + 1], lst[j] #  swaps the elements
