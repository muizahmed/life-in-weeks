age = input("What is your current age?")
age_as_int = int(age)

days_left = (75 - age_as_int) * 365
weeks_left = (75 - age_as_int) * 52
months_left = (75 - age_as_int) * 12
message = (f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
print(message)
