class Solution:

	# Method to find median
	def Median(self, A, B):
	
		# Assumption both A and B cannot be empty
		# n is the size of A and m is the size of B
		n = len(A)
		m = len(B)
		if (n > m):
			#Assume array A having the minimum number of elements
			#If A is not having minimum number of elements
		    #Swapping to make A smaller
			return self.Median(B, A) 

		start = 0
		end = n
		realmidinmergedarray = (n + m + 1) // 2

		#to find the median than we have to 
		#divide the whole merged array into two parts
		#namely left and right parts
		while (start <= end):
			mid = (start + end) // 2
			leftAsize = mid
			leftBsize = realmidinmergedarray - mid
			
			#Now we have 4 variables indicating four values 
			# two from array A and two from array B
			# checking overflow of indices
			leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
			leftB = B[leftBsize - 1] if (leftBsize > 0) else float('-inf')
			rightA = A[leftAsize] if (leftAsize < n) else float('inf')
			rightB = B[leftBsize] if (leftBsize < m) else float('inf')

			# if correct partition is done
			# and our answer depends on the total size of merged array
			if leftA <= rightB and leftB <= rightA:
				#max of left part is nearest to median 
				#and min of right part is nearest to medain
				if ((m + n) % 2 == 0):
					return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
				return max(leftA, leftB)

			elif (leftA > rightB):
				end = mid - 1
			else:
				start = mid + 1

# Driver code
ans = Solution()
arr1 = []
arr2 = []

#Input elemnts in array 1
arr1 = [int(item) for item in input("Enter the list items_1 : ").split()]
#sort arr1 and then output
arr1.sort()
print(arr1)


#Input elemnts in array 2
arr2 = [int(item) for item in input("Enter the list items_2 : ").split()]
#sort arr2 and then output
arr2.sort()
print(arr2)

#Add both arrays in one array arr3
arr3=arr1+arr2

#then sort the array to get the median
#of the two sorted arrays arr1 & arr2
arr3.sort()
print("The sorted array is",arr3)

#Output the median 
print("Median of the two arrays is {}".format(ans.Median(arr1, arr2)))
