with open('day1/aoc-day1-data.txt') as f:
    data = f.read().splitlines()
data = list(map(int, data))
is_two_nums = False
is_three_nums = False
for x in data:
    for y in data:
        addNum = x + y
        if (addNum == 2020) & (not is_two_nums):
            print("2 nums multipled: ", str(x*y))
            is_two_nums = True
        if (addNum < 2020) & (not is_three_nums):
            third_sum = 2020 - addNum
            if third_sum in data:
                print("3 nums multipled: ", str(x*y*third_sum))
                is_three_nums = True
# This can be done better to not show the matching numbers twice.
# Can be more efficient:
#  - sort the data
#  -
# This doesn't consider the fact that the number could add 1010 if it was in there to not be considered if there's only 1 number.
