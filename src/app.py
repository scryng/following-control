# Defining the variables
initial_following = 4875  # number of profiles you are following today (01/12)
target_following = 940  # number of profiles you want to follow (10% of followers)
remaining_days = 31  # remaining days to reach the goal (from 01/12 to 31/12)

# Calculating the total number of profiles to unfollow
total_to_unfollow = initial_following - target_following  # total profiles to unfollow

# Calculating how many profiles to unfollow per day
unfollow_per_day = total_to_unfollow / remaining_days  # profiles to unfollow per day

# Generating the list of profiles followed per day
followed_per_day = []

for day in range(remaining_days):
    # Calculate the number of profiles followed by the end of each day
    # Round the result to avoid rounding errors over time
    followed_per_day.append(round(initial_following - (unfollow_per_day * (day + 1))))

def generate_following_schedule():
    """
    Generates the daily schedule of the number of profiles you will be following
    at the end of each day, starting from the initial number and gradually unfollowing
    to reach the target by 31st December.

    Returns:
        list: A list of the number of profiles followed at the end of each day.
    """
    return followed_per_day

# You can call the function to get the schedule of profiles followed per day
following_schedule = generate_following_schedule()

# Displaying the following schedule
print("Following schedule:", following_schedule)
print("Profiles to unfollow per day:", unfollow_per_day)