def merge(srt_lst1, srt_lst2):
  merged_lst = []
  idx_1 = 0
  idx_2 = 0

  while idx_1 < len(srt_lst1) and idx_2 < len(srt_lst2):
    if srt_lst1[idx_1] < srt_lst2[idx_2]:
      merged_lst.append(srt_lst1[idx_1])
      idx_1 += 1
    else:
      merged_lst.append(srt_lst2[idx_2])
      idx_2 += 1

  return merged_lst


def merge_sort(lst):
  if len(lst) == 0:
    return
  elif len(lst) == 1:
    return
  else:
    mid = len(lst) // 2
    left_lst = lst[:mid]
    right_lst = lst[mid:]

    merge_sort(left_lst)
    merge_sort(right_lst)

    merged = merge(left_lst, right_lst)

    for i in range(len(merged)):
      lst[i] = merged[i]