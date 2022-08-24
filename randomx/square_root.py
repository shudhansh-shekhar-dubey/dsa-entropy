def square_root(number):
  start = 0
  end = 65536
  while start+1 < end:
    mid = start + (end-start)/2;
    mid_sqr = mid * mid
    if mid_sqr == number:
      return mid
    elif mid_sqr > number:
      end = mid
    else:
      start = mid
  return start