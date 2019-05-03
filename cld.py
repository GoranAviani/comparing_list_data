def mainMenu():

    while True:
        userInput = input("What do you want to do:\n"
              "1 Import 2 lists and check their differences? or \n"
              "2 Check differences between lists from the cld file?\n"
              "----------------------------------------------------------\n"
              "Press X to Exit")

        # On exit show current stock and break
        if userInput.upper() == "X":

            print("Good bye !")
            break



def main():

    mainMenu()


    theirCustIDs = []
    ourCustIDs = []
    theirSubsIDs = []
    ourSubsIDs = []


    list415 = []
    list407 = []
    for x in ourCustIDs:
        if x not in theirCustIDs:
            print("Customer {} is not in their list" .format(x))
    print("------------------------------------------------------------------")

    for x in theirCustIDs:
        if x not in ourCustIDs:
            print("Customer {} is not in our list".format(x))
    print("------------------------------------------------------------------")



    for x in list415:
        if x not in list407:
            print("Customer {} is not in their list407" .format(x))
    print("------------------------------------------------------------------")





if __name__ == "__main__":
    main()


