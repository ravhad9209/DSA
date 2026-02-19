import array as arr

ar = None

while True:
    try:
        choice = int(input(
            "\n1) Create an Array"
            "\n2) Insert Element at Position"
            "\n3) Append Elements (Multiple)"
            "\n4) Delete Element from Position"
            "\n5) Search Element"
            "\n6) Display Array"
            "\n7) Exit"
            "\nEnter your choice: "
        ))

        if choice == 1:
            ar = arr.array('i')
            print("Array Created Successfully!\n")

        elif choice == 2:
            if ar is None:
                print("Please create array first!")
                continue

            data = int(input("Enter element to insert: "))
            pos = int(input("Enter position: "))

            if pos < 0 or pos > len(ar):
                print("Invalid Position!")
            else:
                ar.insert(pos, data)
                print("Element inserted successfully!\n")

        elif choice == 3:
            if ar is None:
                print("Please create array first!")
                continue

            elements = input("Enter multiple elements separated by space: ")
            nums = list(map(int, elements.split()))

            for num in nums:
                ar.append(num)

            print("Elements appended successfully!\n")

        elif choice == 4:
            if ar is None or len(ar) == 0:
                print("Array is empty!")
                continue

            pos = int(input("Enter position to delete: "))

            if pos < 0 or pos >= len(ar):
                print("Invalid Position!")
            else:
                ar.pop(pos)
                print("Element deleted successfully!\n")

        elif choice == 5:
            if ar is None or len(ar) == 0:
                print("Array is empty!")
                continue

            key = int(input("Enter element to search: "))
            if key in ar:
                print("Element found at index:", ar.index(key))
            else:
                print("Element not found!")

        elif choice == 6:
            if ar is None or len(ar) == 0:
                print("Array is empty!")
            else:
                print("Array Elements:")
                for i in ar:
                    print(i, end=" ")
                print()

        elif choice == 7:
            print("Thanks for using the program!")
            break

        else:
            print("Invalid option!")

    except ValueError:
        print("Please enter valid numeric input!")
