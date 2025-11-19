def swap(lst, curr, min_idx):
  temp = lst[curr]
  lst[curr] = lst[min_idx]
  lst[min_idx] = temp
  # the whole thing is θ(1)

def selection_sort(lst):
  n = len(lst)

  for curr in range(n):
    min_idx = curr

    for j in range(curr + 1):
      if lst[j] < lst[min_idx]:
        min_idx = j
    swap(lst, curr, min_idx)