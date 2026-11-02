name = input("enter your name:").strip().title()
print(f"welcome {name} how do you want to spend your day?")
categories = ["Faith", "Learning", "Career", "body", "Off time", "Sleep"]
for number, category in enumerate(categories, start=1):
    print(f"{number}.{category}")
plan = []
for category in categories:
    activity = input(f"what will you do for {category}? ")
    while True:
        try:
            hours = float(input(f"how many hours a day for {activity}? "))
            break
        except ValueError:
            print("please enter a number")
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
done = 0
for item in plan:
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
