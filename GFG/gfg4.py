""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Name of Question: Number of Steps to Reduce a Number to Zero
Link of Question:https:https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/submissions/
""""""""""""""""""""""""""""""""""""""""""""""""""""""""
class Solution:
    def numberOfSteps (self, num: int) -> int:
        count=0
        while(num!=0):
                if(num%2==0):
                    num=num/2
                    count=count+1
                elif(num%2!=0):
                    num=num-1
                    count=count+1
        return count
