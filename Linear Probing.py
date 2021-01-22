# Program to implement Hashing with Linear Probing
import random

class hashTable:
    # initialize hash Table
    def __init__(self):
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
    def hashFunction(self, element):
        return element % self.size

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
            self.table[position] = element
            print("Element " + str(element) + " at position " + str(position))
            isStored = True
            self.elementCount += 1

        # collision occured hence we do linear probing
        else:
            print("Collision has occured for element " + str(element) + " at position " + str(
                position) + " finding new Position.")
            self.count += 1
            while self.table[position] != 0:
                position += 1
                if position >= self.size:
                    position = 0

            self.table[position] = element
            isStored = True
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
            isFound = True

        # if element is not found at position returned hash function
        # then first we search element from position+1 to end
        # if not found then we search element from position-1 to 0
        else:
            temp = position - 1
            # check if the element is stored between position+1 to size
            while position < self.size:
                if self.table[position] != element:
                    position += 1
                    self.countsearch += 1
                    self.comparisons += 1
                else:
                    return position

            # now checking if the element is stored between position-1 to 0
            position = temp
            while position >= 0:
                if self.table[position] != element:
                    position -= 1
                    self.countsearch += 1
                    self.comparisons += 1
                else:
                    return position

        if not found:
            print("Element not found")
            self.countunsuccessfulsearch += 1
            return False

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

# storing elements in table
num = 10000
remove = 500

for i in range(num):
    table1.insert(random.randint(0, 10000))

for i in range(num):
    table1.search(random.randint(0, 10000))

for i in range(remove):
    table1.remove(random.randint(0, 10000))

# displaying the Table
table1.display()
print()

