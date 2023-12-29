import csv
def main():
    file = open("students.csv", "a")
    writer = csv.writer(file)
    for i in 55:
        first = input("first name: ")
        last = input("last name: ")
        x = (input("grade level: ")
        if x == 'k' or x == 'K':
          grade = ord(x) - ord(x)
        elif x == '1' or x == '2' or x == '3' or x == '4' or x == '5' or x == '6' or x == '7' or x == '8' or x == '9' or x == '10' or x == '11' or x = '12':
          grade = int(x)
        else:
          x = (input("grade level: ")
        writer.writerow([first, last, grade])
main()
