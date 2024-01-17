import math

def calculate_basic_stats(xs: List[float]) -> (float, float, float, float):
  return (min(xs), 
          max(xs), 
          sum(xs)/len(xs), 
          math.sqrt(sum(x**2 for x in xs)/len(xs) - (sum(xs)/len(xs))**2))

# 1) implement this function with out modifying the top one
# a number is normal iff it is with in 1 standard deviation of the mean of xs
def is_number_normal(x: float, xs: List[float]):
  pass

# 2) now try make the top function returns something more civilize and write is_number_normal again.


