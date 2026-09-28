def job_scheduling(jobs):
    """
    jobs: list of tuples (job_id, deadline, profit)
    Returns: (scheduled_jobs, total_profit)
    """
    # Step 1: Sort by profit descending
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Step 2: Find max deadline
    max_deadline = max(job[1] for job in jobs)

    # Step 3: Create slots
    slots = [None] * (max_deadline + 1)   # 1-indexed
    total_profit = 0
    scheduled = []

    # Step 4: Assign jobs to latest free slot before deadline
    for job_id, deadline, profit in jobs:
        for t in range(min(max_deadline, deadline), 0, -1):
            if slots[t] is None:
                slots[t] = job_id
                total_profit += profit
                scheduled.append((job_id, t, profit))
                break

    return scheduled, total_profit


# Example
if __name__ == "__main__":
    jobs = [
        ("J1", 2, 100),
        ("J2", 1, 19),
        ("J3", 2, 27),
        ("J4", 1, 25),
        ("J5", 3, 15),
    ]

    scheduled, profit = job_scheduling(jobs)
    print("Scheduled Jobs:")
    for jid, slot, p in sorted(scheduled, key=lambda x: x[1]):
        print(f"  Time Slot {slot}: {jid} (profit={p})")
    print(f"Total Profit = {profit}")





    # Online Python compiler (interpreter)
# Write and run Python online using this editor.

def fractional_knapsack(weights, values, capacity):
    """
    Solves the fractional knapsack problem using a greedy approach.
    
    Args:
        weights: list of item weights
        values: list of item values
        capacity: maximum weight the knapsack can hold
    
    Returns:
        maximum total value (float)
    """
    n = len(weights)
    
    # Create list of (value/weight ratio, weight, value) tuples
    items = []
    for i in range(n):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))
    
    # Sort items by ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for ratio, weight, value in items:
        if remaining_capacity >= weight:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take a fraction of the item
            fraction = remaining_capacity / weight
            total_value += value * fraction
            remaining_capacity = 0
            break
    
    return total_value


# Example usage
if __name__ == "__main__":
    weights = [10, 20, 30]
    values  = [60, 100, 120]
    capacity = 50
    
    max_value = fractional_knapsack(weights, values, capacity)
    print(f"Maximum value in knapsack = {max_value}")







def interval_scheduling(activities):
   
    if not activities:
        return []
    
    # Step 1: Sort by finish time
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    # Step 2: Pick the first activity
    selected = [sorted_activities[0]]
    last_finish = sorted_activities[0][1]
    
    # Step 3: Greedily pick compatible activities
    for start, finish in sorted_activities[1:]:
        if start >= last_finish:   # no overlap
            selected.append((start, finish))
            last_finish = finish
    
    return selected


# Example usage
if __name__ == "__main__":
    activities = [
        (1, 4), (3, 5), (0, 6), (5, 7),
        (3, 9), (5, 9), (6, 10), (8, 11),
        (8, 12), (2, 14), (12, 16)
    ]
    
    result = interval_scheduling(activities)
    print(f"Maximum number of activities: {len(result)}")
    print(f"Selected activities: {result}")





import heapq
def earliest_start_time_first_fast(lectures):
    sorted_lec = sorted(
        [(s, f, i) for i, (s, f) in enumerate(lectures, start=1)],
        key=lambda x: x[0]
    )

    heap = []
    schedule = []
    d = 0

    for start, finish, lec_id in sorted_lec:
        if heap and heap[0][0] <= start:
            _, room = heapq.heappop(heap)
        else:
            d += 1
            room = d

        heapq.heappush(heap, (finish, room))
        schedule.append((lec_id, room))

    return d, schedule

if __name__ == "__main__":
    lectures = [
        (1, 4),
        (2, 5),
        (7, 9),
        (3, 7),
        (6, 10),
        (8, 11),
    ]

d, schedule = earliest_start_time_first_fast(lectures)




from collections import deque

def stable_matching(men_prefs, women_prefs):
    n = len(men_prefs)

    women_rank = {
        w: {m: i for i, m in enumerate(women_prefs[w])}
        for w in women_prefs
    }

    free_men = deque(men_prefs.keys())
    next_proposal = {m: 0 for m in men_prefs}

    engaged_to = {}
    partner_of_woman = {}

    while free_men:
        m = free_men.popleft()

        if next_proposal[m] >= n:
            continue

        w = men_prefs[m][next_proposal[m]]
        next_proposal[m] += 1

        if w not in partner_of_woman:
            partner_of_woman[w] = m
            engaged_to[m] = w
        else:
            current = partner_of_woman[w]
            if women_rank[w][m] < women_rank[w][current]:
                partner_of_woman[w] = m
                engaged_to[m] = w
                del engaged_to[current]
                free_men.append(current)
            else:
                free_men.append(m)

    return engaged_to


if __name__ == "__main__":
    men_prefs = {
        "A": ["X", "Y", "Z"],
        "B": ["Y", "X", "Z"],
        "C": ["Y", "Z", "X"],
    }

    women_prefs = {
        "X": ["B", "A", "C"],
        "Y": ["A", "B", "C"],
        "Z": ["A", "B", "C"],
    }

    matching = stable_matching(men_prefs, women_prefs)

    print("Stable matching:")
    for m, w in sorted(matching.items()):
        print(f"  {m} -- {w}")







#--------------------------STABLE MATCHING----------------------------

"""
men=['A','B','C']
women=['q','r','s']

men_preference={'A':['q','s','r'],
                'B':['q','r','s'],
                'C':['s','r','q']}
women_preference={'q':['C','B','A'],
                  'r':['A','C','B'],
                  's':['A','B','C']}

matched_men={}
matched_women={}
free_men=men.copy() # ['A','B','C']

while free_men:
    m=free_men.pop(0)  # 'A'
    for w in men_preference[m]: #['q','s','r']
       if w not in matched_women:
           matched_women[w]=m
           matched_men[m]=w
           break
       else:
           current=matched_women[w]
           cur=women_preference[w].index(current)
           new=women_preference[w].index(m)
           if new < cur:
             matched_women[w]=m
             matched_men[m]=w
             matched_men.pop(current)
             free_men.append(current)
             break


for m in matched_men:
 print(m,"---->",matched_men[m])  """










"""men=["Xavier","Yancey","Zeus"]
women=["Amy","Bertha","Clare"]

men_preference={"Xavier":["Amy","Bertha","Clare"],
                "Yancey":["Bertha","Amy","Clare"],
                "Zeus":["Amy","Bertha","Clare"]}
women_preference={"Amy":["Yancey","Xavier","Zeus"],
                  "Bertha":["Xavier","Yancey","Zeus"],
                  "Clare":["Xavier","Yancey","Zeus"]}


matched_men={}
matched_women={}
free_men=men.copy() #["Xavier","Yancey","Zeus"]
while free_men:
    m=free_men.pop(0)    # Xavier
    for w in men_preference[m]: #["Amy","Bertha","Clare"]
        print(m,"proposes to",w)
        if w not in matched_women:
           print(w,"pair with",m,"because she is free")
           matched_women[w]=m
           matched_men[m]=w
           break

        else:
           current=matched_women[w]
           cur=women_preference[w].index(current)
           new=women_preference[w].index(m)
           if new < cur:
               print(w,"rejects",current,)
               matched_women[w]=m
               matched_men[m]=w
               matched_men.pop(current)
               free_men.append(current)
               break
           else:
               print(w,"rejects",m,"because she likes her current match",current,"more.")
               print(m,"remain free")


for m in matched_men:
    print(m,"---->",matched_men[m])"""










#------------------------------GREEDY ALGORITHM-------------------------------------------------------------------------
#-----------------------------1. ASSIGN COOKIES (O(n))------------------------------------------------------------------
"""
greed=[]
s=[]
n=int(input("Enter number of children : "))
for i in range(n):
    greed.append(int(input(f"Enter greed of {i+1} children :")))
m=int(input("Enter number of cookies : "))
for i in range(m):
    s.append(int(input(f"Enter cookie size of {i+1} cookie :")))
sorted_greed=sorted(greed)
sorted_s=sorted(s)

p=0
for i in sorted_s:
    if i >= sorted_greed[p]:
        p+=1

print(f"Number of satisfied children is {p}")
"""
#-----------------------------2. LEMONADE CHANGE (O(n))----------------------------------------------------------------
"""
bill=[]
n=int(input("Enter number of customers : "))
for i in range(n):
    bill.append(int(input(f"Enter bill of {i+1} customer :")))

sorted_bill=sorted(bill)

five=0
ten=0
twenty=0
flag = True
for i in sorted_bill:
    if i == 5:
        five+=1
    elif i == 10 and five != 0:
        ten +=1
        five -=1
    elif i == 20:
        if ten >= 1 and five != 0:
           five -=1
           ten -=1
        elif ten == 0 and five >= 3:
            five -=3
        else:
            flag = False
    else:
        flag = False
        break
if flag:
    print("Satisfied Every Customer")
else:
    print("Not Satisfied Every Customer")

"""



#------------------------------- 3. SHORTEST JOB FIRST (O(nlogn))-------------------------------------------------------
"""
burst=[]
n=int(input("Enter number of jobs : "))
for i in range(n):
  burst.append(int(input(f"Enter burst time of job no. {i+1} :")))

sum=0
sorted_burst=sorted(burst)
for i in sorted_burst:
    sum+=i
print(f"Average burst time is {int(sum/n)}")
"""

#-------------------------------- 4. JUMP GAME (O(n))-------------------------------------------------------------------
""""
arr=[]
n=int(input("Enter number of jumps : "))
for i in range(n):
    arr.append(int(input(f"Enter step size of jump no. {i+1} :")))

MaxIndex=0
for i in range(n):
    if i <= MaxIndex:
        MaxIndex=max(MaxIndex,i+arr[i])
    else:
        break

if MaxIndex >= n-1:
    print("Reached to the End")
else:
    print("Not Reached to the End")
"""
#--------------------------------- 5. JUMP GAME 2 (O(n^n)---------------------------------------------------------------
"""
def f(i, k):
    if i >= n-1:
        return k
    else:
        m = 9999
        for j in range(1, arr[i]+1):
            m = min(m, f(i+j,k+1))
    return m


arr=[]
n=int(input("Enter number of jumps : "))
for i in range(n):
    arr.append(int(input(f"Enter step size of jump no. {i+1} :")))

print(f"Minimum Number of jumps required :{f(0,0)}")

"""

#-------------------------------------- OPTIMIZATION--------------------------------------------------------------------

"""

def f(i, k):
    if i >= n-1:
        return k
    else:
        m = 9999
        for j in range(1, arr[i]+1):
            if F[i+j][k+1] != -1:
                m = min(m, F[i+j][k+1])
            else:
                F[i+j][k+1] = f(i+j,k+1)
                m = min(m, F[i + j][k + 1])
    return m


arr=[]
n=int(input("Enter number of jumps : "))
for i in range(n):
    arr.append(int(input(f"Enter step size of jump no. {i+1} :")))

F = [[-1 for i in range(n)] for j in range(n)]
print(f"Minimum Number of jumps required :{f(0,0)}")

"""



#-------------------------------------- OPTIMIZATION USING RANGE O(n) --------------------------------------------------
"""
arr=[]
n=int(input("Enter number of jumps : "))
for i in range(n):
    arr.append(int(input(f"Enter step size of jump no. {i+1} :")))


r = 0
l = 0
jump = 0
while r < n - 1:
    jump += 1
    x=l
    l=r+1
    for j in range(x, r + 1):
        r = max(r, j + arr[j])

print(f"Minimum Number of jumps required :{jump}")

"""

#-------------------------------------6. JOB SEQUENCING PROBLEM---------------------------------------------------------
"""
job=[]
n=int(input("Enter number of jobs: "))
for i in range(n):
    id = int(input(f"Enter id of job no. {i+1} :"))
    deadline = int(input(f"Enter deadline of job no. {i+1} :"))
    profit = int(input(f"Enter profit of job no. {i+1} :"))
    job.append((id, deadline, profit))

job.sort(key=lambda x: x[2], reverse=True)

slots = [-1]*(max(j[1] for j in job)+1)

for i in job:
    if slots[i[1]] == -1:
        slots[i[1]]=i[2]
    else:
        x=i[1]
        while x >=0 and slots[x] != -1:
            x -=1
        slots[x]=i[2]

print(slots)
"""
#-----------------------------------------ROUGH-------------------------------------------------------------------------
"""
a=0
x=[(1,2),(5,7),(4,6)]
m=max(i[1] for i in x)
print(m)
"""
#-------------------------------------7. N MEETING IN ONE ROOM----------------------------------------------------------
"""
n=int(input("Enter number of jobs : "))
job=[]
for i in range(n):
    start = int(input(f"Enter start time of job no. {i+1} :"))
    end = int(input(f"Enter end time of job no. {i+1} :"))
    job.append((i+1,start,end))

job.sort(key=lambda x: x[2])
result=[]
end=-1
for i in job:
    if i[1] >= end:
        result.append(i)
        end=i[2]

for i in result:
    print(f"{i[0]}: {i[1]}----->{i[2]}")

"""

#--------------------------------------8.NON-OVERLAPPING INTERVALS------------------------------------------------------
"""
n=int(input("Enter number of jobs : "))
job=[]
for i in range(n):
    start = int(input(f"Enter start time of job no. {i+1} :"))
    end = int(input(f"Enter end time of job no. {i+1} :"))
    job.append((start,end))

job.sort(key=lambda x: x[1])
result=[]
end=-1
for i in job:
    if i[0] >= end:
        result.append(i)
        end=i[1]

print(f"Number of Non-Overlapping Jobs: {len(job)-len(result)}")
"""
#--------------------------------------9. INSERT INTERVALS--------------------------------------------------------------

#-------------------------------------10. MINIMUM NUMBER OF PLATFORMS---------------------------------------------------
arrival=[]
departure=[]
n=int(input("Enter number of train : "))
for i in range(n):
    arrival.append(int(input(f"Enter arrival time of train no. {i+1} :")))
for i in range(n):
    departure.append(int(input(f"Enter departure time of train no. {i+1} :")))

sorted_departure=sorted(departure)
p=0
q=0
count=0
platform=-1
while p <= n-1:
    if arrival[p]<sorted_departure[q]:
        count +=1
        p +=1
        platform = max(platform, count)
    else:
        count -=1
        q +=1

print(f"Minimum number of platform needed : {platform}")



#----------------------------------- -11. FRACTIONAL KNAPSACK-----------------------------------------------------------

























































