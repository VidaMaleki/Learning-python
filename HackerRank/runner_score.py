# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
#  You are given  scores. Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains n . The second line contains an array A[] of n integers each separated by a space.

arr = [2, 3, 6, 6, 5]
n = 5

def runner_score(arr):
    runner_list = sorted(list(set(arr)))
    for i in range(1):
        print(runner_list[-2])
    
runner_score(arr)
