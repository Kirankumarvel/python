current_hour = 14  # 2 PM
if (current_hour >= 9 and current_hour <= 17) or (current_hour >= 19 and current_hour <= 21):
    print("Within working hours.")
else:
    print("Outside working hours.")