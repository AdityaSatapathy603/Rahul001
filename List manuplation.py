mylist = [22,44,88,4,16,38,13]
choice = 0
while True:
    print('List your operation Program by...')
    print('1. Append an Element.')
    print('2. Insert an Element at desired position.')
    print('3. Append a list to the given list.')
    print('4. Modify an existing Element.')
    print('5. Delete an existing Element by position.')
    print('6. Delete an existing Element by value.')
    print('7. Sort List in ascending order.')
    print('8. Sort list in descending order.')
    print('9. Display List.')
    print('10. Exit.')
    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        Element = int(input("Enter Element to append: "))
        print('Element has be Appended.')
        mylist.append(Element)
    elif choice == 2:
        Element = int(input("Enter Element to be inserted: "))
        pos = int(input("Enter position: "))
        mylist.insert(Element,pos)
        print('Element has been inserted in designated position.')
    elif choice == 3:
        Element = int(input("How many element do you want to enter in list: "))
        for i in range(0,Element):
            n = int(input("Enter the list of elements : "))
            mylist.append(n)
    elif choice == 4:
        i = int(input("Enter the position of elements to be Modify: "))
        if i<len(mylist):
            newElement = int(input("Enter the new Element: "))
            oldElement = mylist[i]
            mylist[i] = newElement
            print('The old element',oldElement,'has been replaced by new value',newElement)
        else:
            print('Position of the element is more the length of the list')
    elif choice == 5:
        i = int(input("Enter the position of the element to be deleted : "))
        if i<len(mylist):
            Element = mylist.pop[i]
            print('The element ',Element, ' has been deleted.')
        else:
            print('Position of the element is more the length of the list')
    elif choice == 6:
        element = int(input("Enter the element to be deleted: "))
        if element in mylist:
            mylist.remove(element)
            print('The element',element,'has been removed.')
        else:
            print('Position of the element is more the length of the list')
    elif choice == 7:
        mylist.sort()
        print('The list has been sorted.')
    elif choice == 8:
        mylist.sort(reverse=True)
        print('List has been sorted in reverse order.')
    elif choice == 9:
        print('The list is___',mylist)
    elif choice == 10:
        exit()
    else:
        print("Command not valid!")