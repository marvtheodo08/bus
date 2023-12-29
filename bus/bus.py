import csv
def main():
    file = open("students.csv", "a")
    writer = csv.writer(file)
    for i in 55:
        first = input("first name: ")
        last = input("last name: ")
        grade = int(input("grade level: ")
        if (grade == 'K' || grade == 'k'):
          grade = 0
main()
