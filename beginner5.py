time = int(input("What time is it?"))

if time in range(0, 12):
    print("Good morning")
elif time in range(12, 18):
    print("Good afternoon")
elif time in range(18, 24):
    print("Sleep, NOW!")
