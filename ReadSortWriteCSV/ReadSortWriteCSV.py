import csv
from operator import itemgetter

peopleList = []

with open("PeopleList.txt") as file:
    reader = csv.reader(file)
    header = next(reader)
    assert header

    for row in reader:
        peopleList.append(row)

    def writeCSV():
        with open('srtPeopleList', 'w', newline="") as f:
            thewriter = csv.writer(f)
            thewriter.writerow(header)
            for i in range(len(sorted_list)):
                thewriter.writerow(sorted_list[i])

    def reverseList():
        print("\nWould You Like To Reverse The Sorted Information?")
        reverse = input("Enter: Y = Yes or N = No\n")

        if reverse.capitalize() == "N":
            writeCSV()
            print("\nYour File was Sorted in Increasing/Alphabetical Order")
        elif reverse.capitalize() == "Y":
            sorted_list.reverse()
            writeCSV()
            print("\nYour File Was Sorted in Reverse Order")
        else:
            print("Invalid Option")
            reverseList()

    need_continue = True
    while need_continue:
        options = ""
        for i in range(len(header)):
            print(options + str(i + 1) + " - " + str(header[i]))
        response = input("\nEnter The Column Number You Would You Like To Sort: ")

        if (int(response) <= len(header)) and (int(response) >= 1):
            sorted_list = sorted(peopleList, key=itemgetter(int(response) - 1))
            reverseList()
            need_continue = False
        else:
            need_continue = True
            print("Invalid Entry")
