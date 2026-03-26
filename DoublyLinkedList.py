class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None


class DoublyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

    # Insert at beginning
    def InsertFirst(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = newn
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.iCount += 1

    # Insert at end
    def InsertLast(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = newn
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next

            temp.next = newn
            newn.prev = temp

        self.iCount += 1

    # Insert at position
    def InsertAtPos(self, no, pos):
        if pos < 1 or pos > self.iCount + 1:
            print("Invalid Position")
            return

        if pos == 1:
            self.InsertFirst(no)
        elif pos == self.iCount + 1:
            self.InsertLast(no)
        else:
            newn = Node(no)
            temp = self.first

            for i in range(1, pos - 1):
                temp = temp.next

            newn.next = temp.next
            newn.prev = temp
            temp.next.prev = newn
            temp.next = newn

            self.iCount += 1

    # Delete first node
    def DeleteFirst(self):
        if self.first is None:
            return

        if self.first.next is None:
            self.first = None
        else:
            self.first = self.first.next
            self.first.prev = None

        self.iCount -= 1

    # Delete last node
    def DeleteLast(self):
        if self.first is None:
            return

        if self.first.next is None:
            self.first = None
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next

            temp.prev.next = None

        self.iCount -= 1

    # Delete at position
    def DeleteAtPos(self, pos):
        if pos < 1 or pos > self.iCount:
            print("Invalid Position")
            return

        if pos == 1:
            self.DeleteFirst()
        elif pos == self.iCount:
            self.DeleteLast()
        else:
            temp = self.first

            for i in range(1, pos):
                temp = temp.next

            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            self.iCount -= 1

    # Display forward
    def Display(self):
        temp = self.first
        while temp is not None:
            print("|", temp.data, "|<->", end=" ")
            temp = temp.next
        print("None")

    # Display reverse
    def DisplayReverse(self):
        temp = self.first

        if temp is None:
            return

        while temp.next is not None:
            temp = temp.next

        while temp is not None:
            print("|", temp.data, "|<->", end=" ")
            temp = temp.prev
        print("None")

    def Count(self):
        return self.iCount


# Main function
def main():
    dobj = DoublyLL()

    dobj.InsertFirst(30)
    dobj.InsertFirst(20)
    dobj.InsertFirst(10)

    print("Forward:")
    dobj.Display()
    print("Reverse:")
    dobj.DisplayReverse()

    dobj.InsertLast(40)
    dobj.InsertLast(50)

    print("\nAfter InsertLast:")
    dobj.Display()

    dobj.InsertAtPos(25, 3)

    print("\nAfter InsertAtPos:")
    dobj.Display()

    dobj.DeleteFirst()
    dobj.DeleteLast()

    print("\nAfter DeleteFirst & DeleteLast:")
    dobj.Display()

    dobj.DeleteAtPos(2)

    print("\nAfter DeleteAtPos:")
    dobj.Display()

    print("\nCount:", dobj.Count())


if __name__ == "__main__":
    main()