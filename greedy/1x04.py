#백준 1931 회의실 배정 문제 

meetings = [
   [1, 4],
   [3, 5],
   [0, 6],
   [5, 7],
   [3, 8],
   [5, 9],
   [6, 10],
   [8, 11],
   [8, 12],
   [2, 13],
   [12, 14]
]


result = 0
last_end_meeting = -1

sorted_meetings = sorted(meetings, key =lambda x:x[1])

for meeting in sorted_meetings:
  start,end = meeting[0],meeting[1]
  
  if last_end_meeting<= start:
    result +=1
    last_end_meeting = end
print(result)

