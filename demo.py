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