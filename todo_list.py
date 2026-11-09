from datetime import date
import json


def ask_duration(question):
    while True:
        try:
            text = input(question).strip().lower()
            number_text = text.rstrip("abcdefghijklmnopqrstuvwxyz ")
            unit = text.lstrip("1234567890. ")
            hours = float(number_text)
            if unit.startswith("m"):
                hours = hours / 60
            elif unit.startswith("h"):
                hours = hours
            else:
                print("please use minutes or hours!")
                continue
            if hours >= 0 and hours <= 24:
                break
            else:
                print("please write a number between 0 and 24")
        except ValueError:
            print("please type a number and a unit, like 30 min")
    return hours


def ask_whole_number(question, low, high):
    while True:
        try:
            number = int(input(question))
            if number >= low and number <= high:
                break
            else:
                print(f"please enter a number between {low} and {high}! ")
        except ValueError:
            print("please enter a whole number ")
    return number


name = input("enter your name:").strip().title()
print(f"welcome {name} how do you want to spend your day?")
categories = ["Faith", "Learning", "Career", "body", "Off time", "Sleep"]
for number, category in enumerate(categories, start=1):
    print(f"{number}.{category}")
plan = []
prayers_planned = ask_whole_number(
    "how many times you planned to pray?", 0, 10)
for category in categories:
    if category == "Sleep":
        activity = "Sleep"
        question = "how long do you plan to sleep? "
    else:
        activity = input(f"what will you do for {category}? ")
        question = f"how long for {activity}? "
    hours = ask_duration(question)
    entry = {
        "category": category,
        "activity": activity,
        "hours": hours
    }
    plan.append(entry)
for item in plan:
    print(f"{item['category']}: {item['activity']} for {item['hours']} hours")
total = 0
for item in plan:
    total += item['hours']
print(f"Total planned: {total} hours")

if total > 24:
    print("a day has only 24 hours!")
for item in plan:
    if item['category'] == "Sleep" and item['hours'] < 8:
        print("you sleep less than 8 hours!")

print("evening review".upper())
forgot = []
prayers_done = ask_whole_number("how many times did you pray today? ", 0, 10)
if prayers_done < prayers_planned:
    missed_prayers = prayers_planned - prayers_done
    print(f"you missed: {missed_prayers} prayers today! ")
else:
    print("you prayed all of your prayers")
done = 0
for item in plan:
    if item['category'] == "Sleep":
        slept = ask_duration("how long did you sleep? ")
        if slept < 8:
            print("you have to fix your sleep schedule! go to bed early")
        else:
            print("great you slept very well")
            done += 1
    else:
        review = input(
            f"did you: {item['activity']} (yes/no?) ").strip().lower()
        if review == "yes":
            done += 1
        else:
            forgot.append(item['activity'])
if len(forgot) > 0:
    print("=====what you forgot today=====".upper())
    for task in forgot:
        print(f"- {task}")
result = done / len(plan)
score = round(result * 100)
print(f"score:{score}% ")
if score >= 70:
    print(f"{name}, you were productive today!")
elif score >= 40:
    print(f"{name}, you were not that much productive ,you will improve tomorrow! ")
else:
    print(f"{name}, you were not productive today!!")
today = {
    "date": str(date.today()),
    "name": name,
    "score": score,
    "plan": plan,
    "forgot": forgot
}
try:
    with open("days.json", "r") as file:
        days = json.load(file)
except FileNotFoundError:
    days = []
if len(days) > 0 and days[-1]["date"] == today["date"]:
    days[-1] = today
else:
    days.append(today)
with open("days.json", "w") as file:
    json.dump(days, file, indent=4)
print("your last 5 days:".upper())
recent = days[-5:]
for day in recent:
    print(f"{day['date']}: {day['score']}%")
