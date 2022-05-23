def catalan(n):
    if (n == 0 or n == 1):
        return 1
 
    #store results of subproblems
    catalan =[0]*(n+1)
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j]* catalan[i-j-1]
 
    # Return last entry
    return catalan[n]
 
answer ='yes'
# Driver code
while answer=='yes':
    n=int(input('Enter n:'))
    print(catalan(n))
    answer=input('Try another number?(yes or no)')
