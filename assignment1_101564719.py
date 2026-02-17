"""
Author: Sanzida Islam
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton"      # str
preferred_weight_kg = 20.5       # float
highest_reps = 25                # int
membership_active = True         # bool

# Step c: Create a dictionary named workout_stats
# Dictionary where keys are friend names and values are tuples of minutes spent on three activities
workout_stats = {
    "Alex": (30, 45, 20),      # (yoga, running, weightlifting)
    "Jamie": (20, 50, 30),
    "Taylor": (25, 40, 35),
    "Morgan": (15, 60, 25)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
for friend, activities in workout_stats.copy().items():
    total_minutes = sum(activities)
    workout_stats[f"{friend}_Total"] = total_minutes

# Step e: Create a 2D nested list called workout_list
# 2D list: each row = friend, each column = activity minutes
workout_list = [list(activities) for friend, activities in workout_stats.items() if not friend.endswith("_Total")]

# Step f: Slice the workout_list
# Extract and print yoga and running minutes for all friends
yoga_running = [row[:2] for row in workout_list]
print("Yoga and running minutes for all friends:", yoga_running)

# Extract and print weightlifting minutes for last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]
print("Weightlifting minutes for last two friends:", weightlifting_last_two)

# Step g: Check if any friend's total >= 120
for friend in workout_stats:
    if friend.endswith("_Total") and workout_stats[friend] >= 120:
        original_name = friend.replace("_Total", "")
        print(f"Great job staying active, {original_name}!")

# Step h: User input to look up a friend
friend_name = input("Enter a friend's name to look up: ")
if friend_name in workout_stats:
    activities = workout_stats[friend_name]
    total = workout_stats[f"{friend_name}_Total"]
    print(f"{friend_name}'s workout minutes:")
    print(f"  Yoga: {activities[0]}")
    print(f"  Running: {activities[1]}")
    print(f"  Weightlifting: {activities[2]}")
    print(f"  Total: {total}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
totals = {friend.replace("_Total", ""): minutes for friend, minutes in workout_stats.items() if friend.endswith("_Total")}
max_friend = max(totals, key=totals.get)
min

