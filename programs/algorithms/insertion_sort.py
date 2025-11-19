def insertion_sort(lst):
  for idx in range(1, len(lst)):
    curr = lst[idx]
    j = idx

    while j >= 1 and lst[j - 1] > curr:
      lst[j] = lst[j-1]
      j -= 1

    lst[j] = curr
     