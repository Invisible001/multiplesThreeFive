# Author: Nguyen L
# Date:   April 23rd, 2020
# Purpose: Find the sum of multiples of 3 or 5 below 1000

# define a function to find sum of multiples of 3 or 5

	# declare some variables


	# loop through numbers to the end parameter
		
		# use if statement to test for condition
			#add to list

	# loop through the list and find sum
		# calculate sum here

	# return total

def multiplesThreeFive(start, end):

	total = 0
	my_list = []

	for i in range(start, end):
		
		if i % 3 == 0 or i % 5 == 0:
			my_list.append(i)

	for i in my_list:
		total = total + i

	return total

total = multiplesThreeFive(3, 1000)

print()
print("=====" * 10)
print("SUM: " + str(total))
print("=====" * 10)
print()
