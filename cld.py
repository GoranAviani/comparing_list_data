def main():

    theirCustIDs = []

    ourCustIDs = [1,2,3,4]

    theirSubsIDs = []
    ourSubsIDs = []


    for x in ourCustIDs:
        if x not in theirCustIDs:
            print("Customer {} is not in their list" .format(x))
    print("------------------------------------------------------------------")

    for x in theirCustIDs:
        if x not in ourCustIDs:
            print("Customer {} is not in our list".format(x))
    print("------------------------------------------------------------------")


if __name__ == "__main__":
    main()