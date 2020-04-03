age = 27

if age >= 18:
    print("You are adult an you can buy alcohol")
else:
    print("You are too young to buy alochol")

isDrunk = False

if age >= 18 and not isDrunk:
    print("You are adult an you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")

isRestrictedArea = False

if age >= 18 and not isDrunk and not isRestrictedArea:
    print("You are adult an you can buy alcohol")
else:
    print("Sorry, we cannot sell you alcohol")
