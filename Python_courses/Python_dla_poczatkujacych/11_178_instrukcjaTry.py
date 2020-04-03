import sys

tasksPerPerson = 0

try:
    tasks = 32
    personsStr = input("How many persons are there in the team? ")
    persons = int(personsStr)

    tasksPerPerson = tasks / persons

except:
    print("Something went wrong...", sys.exc_info()[0])

print("Every person should have around", tasksPerPerson, "tasks")
