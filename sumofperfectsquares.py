# Python3 program for the above approach

# Store perfect squares
# less than or equal to N
psquare = []

# Utility function to calculate perfect
# squares less than or equal to N
def calcPsquare(N):
	
	for i in range(1, N):
		if i * i > N:
			break
		
		psquare.append(i * i)

# Function to find the number
# of ways to represent a number
# as sum of perfect squares
def countWays(index, target):
	
	# Handle the base cases
	if (target == 0):
		return 1

	if (index < 0 or target < 0):
		return 0

	# Include the i-th index element
	inc = countWays(index, target - psquare[index])

	# Exclude the i-th index element
	exc = countWays(index - 1, target)

	# Return the result
	return inc + exc

# Driver Code
if __name__ == '__main__':
	
	# Given Input
	N = 9

	# Precalculate perfect
	# squares <= N
	calcPsquare(N)

	# Function Call
	print (countWays(len(psquare) - 1, N))

# This code is contributed by mohit kumar 29
