import matplotlib.pyplot as plt

print("                ")
print("   SMART MOOD & PRODUCTIVITY")
print("       ANALYZER")
print("                ")

name= input("Enter your name:!")

print()
print("Hello", name, "!")
print("let's analyze your day.")

sleep = float(input("How many hours did you sleep today?"))

if sleep < 6:
    sleep_advice = "Your sleep is low. Try to improve your sleep routine."
elif sleep <= 9:
    sleep_advice ="Your sleep duration looks good."
else:
    sleep_advice ="You slept a lot today. Try to maintain a balanced sleep routine."


study = float(input("How many hours did you study today?"))

screen_time = float(input("How many hours did you spend on your phone today?"))

water = float(input("How many liters of water did you drink today? "))

exercise = float(input("How many minutes did you exercise today?"))

if exercise < 20:
    exercise_advice = "Try to include some physical activity today."
elif exercise <= 60:
    exercise_advice = "Good job! Your activity level looks good."
else:
    exercise_advice = "Great activity! Remember to balance exercise with rest."

if water < 1.5:
    water_advice = "Try to drink more water today."
elif water <= 3:
    water_advice = "Your water intake looks good."
else:
    water_advice ="You drank a lot of water today. keep your intake balanced." 

mood = input("How are you feeling today? ")

if mood.lower()=="happy":
   mood_message = "Great! Keep enjoying your positive mood."
elif mood.lower()=="excited":
    mood_message = "Awesome! Use your excitement for something productive."
elif mood.lower()=="stressed":
    mood_message ="Take a short break, relax your mind, and give yourself some time to recharge."
elif mood.lower()== "overthinking":
    mood_message = "Take a short break and your mind some calm time."
else:
    mood_message = "Thanks for sharing your mood.keep checking in with yourself."

sleep_score = 0

if 6 <= sleep <=9:
    sleep_score =25
elif sleep >= 5:
    sleep_score = 15
else:
    sleep_score = 5

study_score = 0

if study >= 4:
    study_score = 25
elif study >= 2:
    study_score = 15
else:
    study_score = 5

screen_score = 0

if screen_time <=4:
    screen_score = 20
elif screen_time <= 6:
    screen_score = 15
else:
    screen_score = 5

water_score = 0

if 1.5 <= water <= 3:
    water_score = 15
elif water >= 1:
    water_score = 10
else:
    water_score = 5

exercise_score = 0

if 20 <= exercise <= 60:
    exercise_score = 15
elif exercise > 60:
    exercise_score = 15
else:
    exercise_score = 5

wellness_score = sleep_score + study_score + screen_score + water_score + exercise_score

if study >= 4 and screen_time <= 6:
    productivity = "High"
elif study >= 2:
    productivity = "Moderate"
else:
    productivity = "Low"

print()
print("      YOUR RESULT       ")
print("Name:", name)
print("sleep:", sleep, "hours")
print("water:", water, "liters")
print("Exercise:", exercise, "minutes")
print("Exercise Advice:", exercise_advice)
print("Water Advice:", water_advice)
print("study:", study, "hours")
print("screen time:", screen_time, "hours")
print("mood:", mood)
print("Mood Analysis:", mood_message)
print("productivity Level:", productivity)
print("Wellness Score:", wellness_score, "/100")

if wellness_score >= 80:
    print("Overall Status: Excellent")
elif wellness_score >= 60:
    print("Overall status: Good")
else:
    print("Overall Status: Needs Improvement")

if sleep_score < 25:
    print("Tip: Try to improve your sleep routine.")
elif study_score < 25:
    print("Tip: Try to increase your study time.")
elif screen_score < 20:
    print("Tip: Try to reduce your screen time.")
elif water_score < 15:
    print("Tip:Try to improve your water intake.")
elif exercise_score < 15:
    print("Tip: Try to include more physical activity.")
else:
    print("Tip: Great balance! keep it up.")

if productivity =="High":
    print("Great job! keep maintaining your healthy routine.")
elif productivity =="Moderate":
    print("Good effort! Try to increase your study time and reduce screen time.")
else:
    print("Take small steps today. Try to improve your sleep, study time, and screen habits.")

with open("daily_data.txt", "a") as file:
    file.write(f"Name: {name}, sleep: {sleep}, study: {study}, Screen Time: {screen_time}, Water: {water}, Exercise:{exercise}, Mood: {mood}, wellness score:{wellness_score}\n")

plt.bar(["wellness score"], [wellness_score])
plt.text(0, wellness_score + 2, str(wellness_score), ha="center")
plt.ylim(0,100)
plt.title("My Wellness Score")
plt.ylabel("score")
plt.show()
categories = ["Sleep","Study","Screen Time"]
values = [sleep, study, screen_time]
plt.bar(categories, values)

for i, value in enumerate(values):
    plt.text(i, value + 0.5, str(value), ha="center")
plt.ylabel("hours")
plt.title("Daily Time Analysis")
plt.show()
categories = ["Water","Exercise"]
values = [water,exercise]

plt.bar(categories, values)
plt.title("Daily Water & Exercise")
plt.ylabel("Liters / Minutes")
plt.show()
