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


name = input("enter your name:").strip().title()
print(f"welcome {name} how do you want to spend your day?")
categories = ["Faith", "Learning", "Career", "body", "Off time", "Sleep"]
for number, category in enumerate(categories, start=1):
    print(f"{number}.{category}")
plan = []
while True:
    try:
        prayers_planned = int(input("how many times will you pray today? "))
        if prayers_planned >= 0 and prayers_planned <= 10:
            break
        print("please enter a number between 0 and 10!")
    except ValueError:
        print("please enter a number!")


for category in categories:
    if category == "Sleep":
        activity = "Sleep"
        question = "how long do you plan to sleep "
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
while True:
    try:
        prayers_done = int(input("how many times did you pray today? "))
        if prayers_done >= 0 and prayers_done <= 10:
            break
        print("please enter a number between 0 and 10 !")
    except ValueError:
        print("please enter a number!")
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
        review = input(
            f"did you: {item['activity']} (yes/no?) ").strip().lower()
    else:
        review = input(
            f"did you: {item['activity']} (yes/no?) ").strip().lower()
        if review == "yes":
            done += 1
result = done / len(plan)
score = round(result * 100)
print(f"score:{score}% ")
if score >= 70:
    print(f"{name}, you were productive today!")
elif score >= 40:
    print(f"{name}, you were not good not bad you will improve tomorrow! ")
else:
    print(f"{name}, you were not productive today!!")
