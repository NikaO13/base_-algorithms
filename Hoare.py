def partition_hoare(a: list[int], lo: int, hi : int) -> int:
  pivot = a[lo]
  i = lo - 1
  j = hi + 1
  
  while True:
    i += 1
    while a[i] < pivot:
      i += 1
      
    j -= 1 
    while a[j] > pivot:
      j -= 1
    
    if i >= j:
      return j
    
    a[i], a[j] = a[j], a[i]
    
def quick_sort_hoare(a: list[int] -> list[int]):
  def sort(lo: int, hi: int) -> None:
    if lo >= hi:
      return
    p = partition_hoare(a, lo, hi)
    sort(lo, p)
    sort(p + 1, hi)
    
  sort(0, len(a) - 1)
  return a

      