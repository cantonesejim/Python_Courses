age = int(input("What is your age?: "))
months = age * 12
days = age * 365 + (age // 4)
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
output = f"""
You have lived for:
{months} months
{days} days
{hours} hours
{minutes} minutes
or {seconds} seconds
"""
print(output)