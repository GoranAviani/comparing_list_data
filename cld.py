def main():

    theirOrderIDs = [1,2,3]
    ourOrderIDs = [1,2,3,4]

    theirSubsIDs = []
    ourSubsIDs = []


    for x in ourOrderIDs:
        if x not in theirOrderIDs:
            print("Order {} is not in their list" .format(x))
    print("------------------------------------------------------------------")

    for x in theirOrderIDs:
        if x not in ourOrderIDs:
            print("Order {} is not in our list".format(x))
    print("------------------------------------------------------------------")


if __name__ == "__main__":
    main()