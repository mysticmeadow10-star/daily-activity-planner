homework_time = int(input("Enter homework time in minutes: "))
free_time = int(input("Enter free time in minutes: "))

if homework_time > free_time:
    print("Plan: Finish homework first before relaxing.")
else:
    print("Plan: You have enough time to relax and do homework.")

if free_time > 120:
    print("Bonus: You have plenty of open time today!")