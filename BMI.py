name = "kazim"
heigt_m = 1.8
weigt_kg = 81
bmi = weigt_kg / (heigt_m ** 2)
print("bmi: ")
print(bmi)
if bmi > 25:
    print(name)
    print("is overweigt")
else:
    if bmi > 18.5:
        print(name)
        print("weigt is ideal")
    elif bmi < 18.5:
        print(name)
        print("you are underweight")