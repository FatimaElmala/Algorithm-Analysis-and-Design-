
def PerfectSquare(N, start, last):
 
    # Find the mid value
    mid = int((start + last) / 2)
 
    #if the start is larger than the last value return error
    if (start > last):
        return -1
    # Check if we got the number which is square root of the perfect
    if (pow(mid, 2) == N):
        return mid

    # If the square(mid) is greater than N, check lower values of mid 
    elif (pow(mid, 2) > N):
        return PerfectSquare(N, start, mid - 1)
 
    # If the square(mid) is less than N, Check higher values of mid 
    else:
        return PerfectSquare(N, mid + 1, last)
 
answer = 'yes'
# Driver code
while answer=='yes':
    N = int(input("Enter number: "))
    print (PerfectSquare(N, 1, N))
    answer=input('Try another number?(yes or no)')





