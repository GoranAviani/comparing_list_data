def loadFromFile():
    with open('compare_lists.save', 'r') as file:
        data = json.load(file)

    file.close()
    return data

def checkFileDiff():
    lists = loadFromFile()
    pass

def checkCustomDiff():
    userList1 = input("Please enter a list with (,) between words or numbers and press enter to enter second list: \n")
    userList2 = input("Please enter a list with (,) between words or numbers and press enter: \n")

    for x in userList1.split(","):
        if x not in userList2.split(","):
            print("{} is not in second list".format(x))
    print("----------------------------------------------------------\n")

    for x in userList2.split(","):
        if x not in userList1.split(","):
            print("{} is not in first list".format(x))
    print("----------------------------------------------------------\n")


def mainMenu():
    while True:
        userInput = input("\n\nWhat do you want to do:\n"
              "1 Import 2 lists and check their differences? or \n"
              "2 Check differences between lists from the cld file?\n"
              "----------------------------------------------------------\n"
              "Press X to Exit\n")
        # On exit show current stock and break
        if userInput.upper() == "X":
            print("Good bye !")
            break
        elif userInput == '1':
            checkCustomDiff()
        elif userInput == '2':
            checkFileDiff()
        else:
            print("Unknown command, please try again.")
def main():

    mainMenu()

if __name__ == "__main__":
    main()


