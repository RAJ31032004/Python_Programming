class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class SinglyLL:
    def __init__(self):
        self.first = None
        self.iCount = 0

    def InsertFirst(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = newn
        else:
            newn.next = self.first
            self.first = newn

        self.iCount += 1

    def InsertLast(self, no):
        newn = Node(no)

        if self.first is None:
            self.first = newn
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next

            temp.next = newn

        self.iCount += 1

    def InsertAtPos(self, no, pos):
        if pos < 1 or pos > (self.iCount + 1):
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
            temp.next = newn
            self.iCount += 1

    def DeleteFirst(self):
        if self.first is None:
            return

        temp = self.first
        self.first = self.first.next
        del temp

        self.iCount -= 1

    def DeleteLast(self):
        if self.first is None:
            return

        if self.first.next is None:
            del self.first
            self.first = None
            self.iCount = 0
        else:
            temp = self.first
            while temp.next.next is not None:
                temp = temp.next

            del temp.next
            temp.next = None
            self.iCount -= 1

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

            for i in range(1, pos - 1):
                temp = temp.next

            target = temp.next
            temp.next = target.next
            del target

            self.iCount -= 1

    def Display(self):
        temp = self.first

        while temp is not None:
            print("|", temp.data, "|->", end=" ")
            temp = temp.next

        print("None")

    def Count(self):
        return self.iCount


def main():
    sobj = SinglyLL()

    sobj.InsertFirst(101)
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    print("Elements of Linked List:")
    sobj.Display()
    print("Count:", sobj.Count())

    sobj.InsertLast(111)
    sobj.InsertLast(121)

    print("After InsertLast:")
    sobj.Display()
    print("Count:", sobj.Count())

    sobj.InsertAtPos(75, 4)

    print("After InsertAtPos:")
    sobj.Display()
    print("Count:", sobj.Count())

    sobj.DeleteFirst()
    sobj.DeleteFirst()

    print("After DeleteFirst:")
    sobj.Display()
    print("Count:", sobj.Count())

    sobj.DeleteLast()

    print("After DeleteLast:")
    sobj.Display()
    print("Count:", sobj.Count())

    sobj.DeleteAtPos(2)

    print("After DeleteAtPos:")
    sobj.Display()
    print("Count:", sobj.Count())


if __name__ == "__main__":
    main()