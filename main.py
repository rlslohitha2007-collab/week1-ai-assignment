import json
from datetime import datetime
with open("tips.json", "r") as file:
    data = json.load(file)
name = input("Enter your name: ")
print(f"\nHello, {name}! Welcome to Smart Student Assistant.")

print("\nMenu")
print("1. Generate Study Tip")
print("2. Generate Motivation Quote")
print("3. Display Current Date & Time")

choice = input("Enter your choice (1-3): ")

result = ""

if choice == "1":
    tip = data["study_tips"][0]
    result = f"Study Tip: {tip}"
    print(result)

elif choice == "2":
    quote = data["motivation_quotes"][0]
    result = f"Motivation Quote: {quote}"
    print(result)

elif choice == "3":
    current_time = datetime.now()
    result = f"Current Date & Time: {current_time}"
    print(result)

else:
    result = "Invalid Choice"
    print(result)

# Save output to file
with open("output.txt", "a") as file:
    file.write(result + "\n")

print("\nResult saved to output.txt")