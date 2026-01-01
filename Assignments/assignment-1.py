# Example: 

# Task 1: Take Inputs (All Data Types)

# int
followers = int(input("Enter Followers Count: "))
following = int(input("Enter Following Count: "))

# float
avg_watch_time = float(input("Enter Average Watch Time per Reel (seconds): "))

# str
username = input("Enter Username: ")
name = input("Enter Name: ")

# list
twitter_features = list(input("Enter twitter Features (comma-separated): ").split(","))

# tuple
content_details = tuple(map(int, (input("Enter Number of Posts: "), input("Enter Number of videos: "))))

# set
interaction_types = set(input("Enter Interaction Types (comma-separated): ").split(","))

# dict
twitter_user = {
    "username": input("Enter your username: "),
    "full_name": input("Enter your full name: "),
    "age": int(input("Enter your age: ")),
    "followers": int(input("Enter number of followers: ")),
    "following": int(input("Enter number of following: ")),
    "posts_count": int(input("Enter number of posts: ")),
    "video_count": int(input("Enter number of videos: ")),
}

# bool
is_verified = bool(input("Is the account verified? (yes/no): "))


# Task 2: Display Output Using Formatting Methods
print("\n--- Twitter Account Details ---\n")

# 1️ Comma Separation (sep=',')
print("Username, Name, Followers, Following:",
      username, name, followers, following, sep=", ")

# 2️ Percentage Formatting (% operator)
# Example: Reel watch completion percentage
watch_completion = 75
print("Reel Watch Completion: %d%%" % watch_completion)

# 3️ f-strings (f"")
print(f"Username: {username}")
print(f"Name: {name}")
print(f"Followers: {followers}")
print(f"Following: {following}")
print(f"Average Watch Time per video: {avg_watch_time} seconds")
print(f"Instagram Features: {twitter_features}")
print(f"Content Details (Posts, video): {content_details}")
print(f"Interaction Types: {interaction_types}")
print(f"Verified Account: {is_verified}")

# 4️ .format() method
print("User Profile: Username - {}, Full Name - {}, Age - {}".format(
    twitter_user["username"],
    twitter_user["full_name"],
    twitter_user["age"]
))

print("Account Stats: Followers - {}, Following - {}, Posts - {}, video - {}".format(
    twitter_user["followers"],
    twitter_user["following"],
    twitter_user["posts_count"],
    twitter_user["video_count"]
))


# Output:

# Enter Followers Count: 350
# Enter Following Count: 400
# Enter Average Watch Time per Reel (seconds): 3.7
# Enter Username: raju_31
# Enter Name: raju
# Enter Instagram Features (comma-separated): post,messages,reels
# Enter Number of Posts: 5
# Enter Number of Reels: 2
# Enter Interaction Types (comma-separated): message, post, reels
# Enter your username: raju_31
# Enter your full name: raju
# Enter your age: 25
# Enter number of followers: 350
# Enter number of following: 400
# Enter number of posts: 6
# Enter number of reels: 2
# Is the account verified? (yes/no): yes

# --- Instagram Account Details ---

# Username, Name, Followers, Following:, raju_31, raju, 350, 400
# Reel Watch Completion: 75%
# Username: raju_31
# Name: raju
# Followers: 350
# Following: 400
# Average Watch Time per Reel: 3.7 seconds
# Instagram Features: ['post', 'messages', 'reels']
# Content Details (Posts, Reels): (5, 2)
# Interaction Types: {'message', ' reels', ' post'}
# Verified Account: True
# User Profile: Username - raju_31, Full Name - raju, Age - 25
# Account Stats: Followers - 350, Following - 400, Posts - 6, Reels - 2
