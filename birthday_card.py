from datetime import datetime

# Get current year
current_year = datetime.now().year

# 1. User inputs
print("Enter the recipient's name:")
recipient_name = input()

print("Enter the year of birth:")
birth_year = int(input())

print("Write a short personalized message:")
personal_message = input()

print("Enter the sender's name:")
sender_name = input()

# 2. Calculate age
age = current_year - birth_year

# 3. Generate birthday card
print("\n" + "=" * 20)
print(f"{recipient_name}, let's celebrate your {age} years of awesomeness!")
print(f"Wishing you a day filled with joy and laughter as you turn {age}!\n")

print(personal_message + "\n")

print(f"With love and best wishes,\n{sender_name}")
print("=" * 20)