#taking no. of intervals from the user  
N = int(input("Enter the number of intervals:"))
intervals = []
#input intervals from the user
for i in range(N):
    row = list(map(int, input().split()))
    intervals.append(row)

#sort intervals depend on the second number of the interval
intervals.sort(key=lambda x: (x[1], x[0]))
count=0
visited= []

end= -1
for interval in intervals:
    if end<= interval[0]:
        end = interval[1]
        count += 1
        visited.append(interval)
        
#Output the number of maximum events scheduled in seqeuence
#and the events scheduled 
print('Max number of events is ',count,'\n Events:' ,visited)
