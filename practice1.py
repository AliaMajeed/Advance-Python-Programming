# Example 1
# # Take integer inputs till the user enters 0 and print the largest number from all.
numbers = []  # start with an empty list

while True:
    num = int(input("Enter any number : "))
    if num == 0:
        break
    numbers.append(num)  # add the number to the list

print("Largest number is", max(numbers))

#Example 2
# Given an integer array nums of length n, you want to create an array ans of length 2n where
#  ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed). Specifically, ans 
# is the concatenation of two nums arrays.Return the array ans.

def getConcatenation(nums):
    ans = nums + nums  # Concatenate nums with itself
    return ans

# Call the function and print the result
nums = [1, 2, 3, 4]
result = getConcatenation(nums)
print(result) 


#Example 3
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums
def runningSum(nums):
    running_sum = []
    current_sum = 0
    for num in nums:
        current_sum += num
        running_sum.append(current_sum)
    return running_sum

# Call the function and print the result
nums = [1, 2, 3, 4]
result = runningSum(nums)
print(result)  





