import array as arr
global ar


while True:
    choice = int(input("1)Create an Array\n2)Insert Element to array\n3)Append Element to a array\n4)Delete Element from array \n5)Search Element from array\n6)Display Array\n7)Exit\nEnter your choice :"))
    print("\n")
    if choice == 1:
        ar = arr.array('i')
        print("Array Created....\n")
    elif choice == 2:
        data = int(input("Enter ELement to Insert"))
        pos = int(input("Enter Location :"))

        ar.insert(pos,data)
        print("Element Inserted Successfully at ",pos,"\n")
    elif choice == 3:
        data = int(input("Enter ELement to Insert"))

        ar.append(data)
        print("Element Appended Successfully\n")

    elif choice == 4:
        data = int(input("Enter Position to delete :"))

        ar.pop(data)
        print("Element Deleted Successfully\n")
    


    
    elif choice ==5:
        print("Displaying Array :")
        for i in ar:
            print(i,end=" ")
        print("\n")

    elif choice ==6:
        print("Thanks For Using ...\n")
        break
    else:
        print("Invalid Option....\n")


