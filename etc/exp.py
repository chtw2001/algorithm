import numpy as np

def time_penalty(days):
    return int(days * 0.1)

events = [
    ("Interview Prep", 10, 0.5, 1, 4),
    ("Project Work", 30, 0.6, 5, 15),
    ("Networking", 20, 0.8, 3, 16),
    ("Online Course", 40, 0.2, 14, 29)
]

n = len(events)
total_days = 30

# Initialize DP table and event tracking arrays
table = np.zeros((n + 1, total_days + 1))
event_indices = np.zeros((n + 1, total_days + 1))

# Loop through events
for i, event in enumerate(events):
    name, exp_reward, prob_success, start_day, end_day = event
    event_duration = end_day - start_day + 1
    event_penalty = time_penalty(event_duration)
    
    for day in range(total_days + 1):
        # Case 1: Do not choose the event
        not_chosen = table[i, day]
        
        # Case 2: Choose the event
        chosen_day = max(day - event_duration, 0)
        penalized_day = max(day - event_duration + event_penalty, 0)
        chosen = prob_success * (table[i, chosen_day] + exp_reward) + (1 - prob_success) * table[i, penalized_day]
        
        # Update DP table and event_indices
        if chosen > not_chosen and day >= start_day and day <= end_day:
            table[i + 1, day] = chosen
            event_indices[i + 1, day] = i + 1
        else:
            table[i + 1, day] = not_chosen
            event_indices[i + 1, day] = event_indices[i, day]

# Backtrack selected events
selected_events = []
day = total_days
for i in range(n, 0, -1):
    if event_indices[i, day] != event_indices[i - 1, day]:
        selected_events.append(events[int(event_indices[i, day] - 1)])
        day -= (events[int(event_indices[i, day] - 1)][4] - events[int(event_indices[i, day] - 1)][3] + 1)

print("최대 기대 경험치 (30일 동안): ", table[len(events), total_days])

print("\n선택한 이벤트:")
for choice in selected_events[::-1]:
    print(f"{choice[0]} (Day {choice[3]} - {choice[4]})")
