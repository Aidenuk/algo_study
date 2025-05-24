# we are given list of objects with job title, deadline and profit in the form of tumple
# Tasks
# 1. sort the jobs in descending order of profit 
# 2. Schedule jobs using the latests available slot <= deadline
# 3. Find scheduled jobs and the profit 
# Use greedy algoriths to get maximum profit 




def job_sequencing(jobs):
    total_profit = 0
    sorted_list = sorted(jobs, key=lambda x:x[2], reverse=True)
    
    max_slots = max(jobs, key=lambda m:m[1])[1]
    time_slots = [None] * max_slots  

    for job in sorted_list:
        deadline = job[1]
        for slot in range(deadline - 1,-1, -1):
            if time_slots[slot] is None:
                time_slots[slot] = job
                total_profit += job[2]
                return time_slots, total_profit



jobs = [
    ("J1", 4, 20),
    ("J2", 1, 10),
    ("J3", 1, 40),
    ("J4", 1, 30),
]



scheduled_jobs, total_profit = job_sequencing(jobs)
print("Scheduled Jobs:", scheduled_jobs)
print("Total Profit:", total_profit)


