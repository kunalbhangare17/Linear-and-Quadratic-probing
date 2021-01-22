import random

class hashTable:
    # initialize hash Table
    def __init__(self):
        print("QUADRATIC PROBING")
        self.size = int(input("Enter the Size of the hash table : "))
        # initialize table with all elements 0
        self.table = list(0 for i in range(self.size))
        self.elementCount = 0
        self.comparisons = 0
        self.count = 0
        self.countsearch = 0
        self.countunsuccessfulsearch = 0
        self.countdelete = 0

    # method that checks if the hash table is full or not
    def isFull(self):
        if self.elementCount == self.size:
            return True
        else:
            return False

    # method that returns position for a given element
    # replace with your own hash function
    def hashFunction(self, element):
        return element % self.size

    # method to resolve collision by quadratic probing method
    def QuadraticProbing(self, element, position):
        posFound = False
        # limit variable is used to restrict the function from going into infinite loop
        # limit is useful when the table is 80% full
        limit = 50
        i = 1
        # start a loop to find the position
        while i <= limit:
            # calculate new position by quadratic probing
            newPosition = position + (i ** 2)
            newPosition = newPosition % self.size
            # if newPosition is empty then break out of loop and return new Position
            if self.table[newPosition] == 0:
                posFound = True
                break
            else:
                # as the position is not empty increase i
                i += 1
        return posFound, newPosition

    # method that inserts element inside the hash table
    def insert(self, element):
        # checking if the table is full
        if self.isFull():
            print("Hash Table Full")
            return False

        isStored = False

        position = self.hashFunction(element)

        # checking if the position is empty
        if self.table[position] == 0:
            # empty position found , store the element and print the message
            self.table[position] = element
            print("Element " + str(element) + " at position " + str(position))
            isStored = True
            self.elementCount += 1

        # collision occured hence we do quadratic probing
        else:
            print("Collision has occured for element " + str(element) + " at position " + str(
                position) + " finding new Position.")
            self.count += 1
            isStored, position = self.QuadraticProbing(element, position)
            if isStored:
                self.table[position] = element
                self.elementCount += 1

        return isStored

    # method that searches for an element in the table
    # returns position of element if found
    # else returns False
    def search(self, element):
        found = False

        position = self.hashFunction(element)
        self.comparisons += 1
        if (self.table[position] == element):
            self.countsearch += 1
            return position

        # if element is not found at position returned hash function
        # then we search element using quadratic probing
        else:
            limit = 50
            i = 1
            newPosition = position
            # start a loop to find the position
            while i <= limit:
                # calculate new position by quadratic probing
                newPosition = position + (i ** 2)
                newPosition = newPosition % self.size
                self.comparisons += 1

                # if element at newPosition is equal to the required element
                if self.table[newPosition] == element:
                    found = True
                    self.countsearch += 1
                    break

                elif self.table[newPosition] == 0:
                    found = False
                    break

                else:
                    # as the position is not empty increase i
                    i += 1
            if found:
                return newPosition
            else:
                print("Element not Found")
                self.countunsuccessfulsearch += 1
                return found

    # method to remove an element from the table
    def remove(self, element):
        position = self.search(element)
        if position is not False:
            self.table[position] = 0
            print("Element " + str(element) + " is Deleted")
            self.elementCount -= 1
            self.countdelete += 1
        else:
            print("Element is not present in the Hash Table")
        return

    # method to display the hash table
    def display(self):
        print("\n")
        for i in range(self.size):
            print(str(i) + " = " + str(self.table[i]))
        print("The number of element is the Table are : " + str(self.elementCount))
        print("Total number of collisions occured: " + str(self.count))
        print("Total number of successful searches: " + str(self.countsearch))
        print("Total number of unsuccessful searches: " + str(self.countunsuccessfulsearch))
        print("Total number of Deleted elements: " + str(self.countdelete))
        alp = num/self.size
        if alp <= 0.75:
            print(f"The alpha value or the loading density is: {alp} which is <= 0.75(Recommended)")
        elif alp > 0.75:
            print(f"The alpha value or the loading density is: {alp} which is > 0.75(Not Recommended)")


# main function
table1 = hashTable()

# storing elements in the table
num = 10000
remove = 500
#num = int(input("Enter the number of elements: "))

for i in range(num):
    table1.insert(random.randint(0, 100000))

for i in range(num):
    table1.search(random.randint(0, 100000))

for i in range(remove):
    table1.remove(random.randint(0, 100000))

    #table1.insert(int(input(f"Enter the {i} element: ")))

#rem = int(input("If you want to remove the elements then press 1 or press 0 to exit: "))

#if rem == 1:
    #table1.remove(int(input("Enter the number you want to remove: ")))
#elif rem == 0:
    #print("Exited")

# displaying the Table
table1.display()
print()
