# Name: Lillian McGowan
# Date: April 16, 2025
# Program: Chapter 7 – Lists
# Description:
# This program asks the user to enter 5 numbers and stores them in a list.
# Then it finds the smallest and largest numbers, the total, and the average.
# It uses functions to break up the different tasks which makes the code easier to manage.
# Everything is printed out in a nice, clean way at the end.
# This helps show how functions, loops, and lists can work together in Python.

LIST_SIZE = 5 # constant for number of inputs

# Main function that controls the flow
def main():
    numsList = getNums()
    low = findLo(numsList)
    high = findHi(numsList)
    total = findTotal(numsList)
    average = findAvg(total)
    displayData(low, high, total, average)

# Function to get 5 numbers from user
def getNums():
    numsList = []
    print("Please enter 5 numbers:")
    for i in range(LIST_SIZE):
        num = float(input(f"Enter number {i + 1}: "))
        numsList.append(num)
    return numsList

# Function to find the lowest number
def findLo(numsList):
    lowest = numsList[0]
    for num in numsList:
        if num < lowest:
            lowest = num
    return lowest

# Function to find the highest number
def findHi(numsList):
    highest = numsList[0]
    for num in numsList:
        if num > highest:
            highest = num
    return highest

# Function to find the total of all numbers
def findTotal(numsList):
    total = 0
    for num in numsList:
        total += num
    return total

# Function to find the average using the total
def findAvg(total):
    return total / LIST_SIZE

# Function to display the results
def displayData(low, high, total, average):
    print("\n--- Results ---")
    print(f"Lowest number: {low}")
    print(f"Highest number: {high}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

# Run the program
main()
