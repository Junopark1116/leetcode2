class Solution:
  def sumOddLengthSubarrays(self, arr: list[int]) -> int:
    ans = 0
    prevEvenSum = 0 
    prevOddSum = 0 
    for i, a in enumerate(arr):
      currEvenSum = prevOddSum + ((i + 1) // 2) * a
      currOddSum = prevEvenSum + (i // 2 + 1) * a
      ans += currOddSum
      prevEvenSum = currEvenSum
      prevOddSum = currOddSum
    return ans