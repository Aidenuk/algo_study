
meetings = [(1,4), (3,5), (0,6), (5,7), (3,8), (5,9), (6,10), (8,11), (8,12), (2,13), (12,14)]

result = 0

earliest_ends = sorted(meetings,key=lambda x:x[1])
nextIndex= 0
for i in range(len(earliest_ends)):
    # print(earliest_ends[i][1])
    # print(earliest_ends[i][0])
    while (nextIndex < len(earliest_ends)):
        nextIndex = i + 1

        if (earliest_ends[i][1] < earliest_ends[nextIndex][0]):
            result + 1

