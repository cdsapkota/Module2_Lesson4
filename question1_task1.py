import random

moods = ["Happy", "Sad", "Energetic", "Calm"]
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


for i in range(7):
    random_mood = random.choice(moods)
    print(f"On {days[i]}, you were feeling {random_mood}")


