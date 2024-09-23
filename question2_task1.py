import random

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["Morning", "Afternoon", "Evening"]
moods = ["happy", "sad", "angry", "excited", "anxious", "frustrated", "grateful", "content", "depressed", "calm", "bored", "guilty", "fearful"]

for i in range(7):
    for j in range(3):
        random_mood = random.choice(moods)
        print(f"On {days[i]} {time_of_day[j]} you were {random_mood}.")


