def first_last6(nums):
    if nums[0] == 6 or nums[len(nums)-1] == 6:
        print True
    else:
        print False
first_last6([1, 2, 6])
first_last6([6, 1, 2, 3])
first_last6([13, 6, 1, 2, 3])

def same_first_last(nums):
    if len(nums) > 1 and nums[0] == nums[len(nums)-1]:
        print True
    else:
        print False
same_first_last([1, 2, 3])
same_first_last([1, 2, 3, 1])
same_first_last([1, 2, 1])

