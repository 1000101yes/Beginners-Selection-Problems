IlikePesto = []
OtherFoods = []

for _ in range(8):
    favorite_foodyum = input("What type of food do you like the most?")
    if favorite_foodyum.lower() == "pesto":
        IlikePesto.append(favorite_foodyum)
    else:
        OtherFoods.append(favorite_foodyum)
print("Pesto is loved by", {len(IlikePesto)}, "people!")
for _ in range(len(IlikePesto)):
    print("Me too")
print(OtherFoods)
