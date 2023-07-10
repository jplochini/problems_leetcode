class Solution:
     def isPalindrome(self, x):
          number_str = str(x)
          
          reverse_number = number_str[::-1]
          
          if number_str == reverse_number:
               return True
          else:
               return False

Solution().isPalindrome(121)
