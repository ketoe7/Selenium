import math
from random import randint


def generateID(yearOfRelease):
    if(type(yearOfRelease) != int):
        print("Year of ID's release must be intiger!")
        return -2
    elif (yearOfRelease < 2001 or yearOfRelease > 2019):
        print("You've entered invalid year of ID's releas (Must be in range 2001 to 2019)")
        return -3
    else:

        yearToAmountOfAllReleasedIDs = {}
        indexOfLetter = []
        letterToNumber = {}
        checkSum = 0
        IDNumber = []

        alfabet = ''.join(chr(x + 65) for x in range(26))
        wagi = [7, 3, 1, 9, 7, 3, 1, 7, 3]

        for i in range(len(alfabet)):
            letterToNumber[alfabet[i]] = 10 + i

        #O and Q does not occur in serial number
        del letterToNumber['O']
        del letterToNumber['Q']

        print("Letter to numbers: " + str(letterToNumber))

        for i in range(26):
            indexOfLetter.append(chr(i + 65))

        #P and Q does not occur in serial number
        indexOfLetter.remove('O')
        indexOfLetter.remove('Q')

        try:
            fileName = "IDStatistics.txt"
            with open(fileName, 'r') as f:

                #stats = open("//home/mikolaj/PycharmProjects/IDGenerator/Generator/IDStatistics.txt", 'r')
                lines = f.readlines()

                #count the amount off all released IDs for specific year
                sum = 0;
                for line in lines:
                    sum += float(line.split(";")[1])
                    yearToAmountOfAllReleasedIDs[line.split(";")[0]] = sum
                    print("In " + line.split(";")[0] + " there were " + str(yearToAmountOfAllReleasedIDs[line.split(";")[0]]) + " of all released IDs (from 2001)")

                #Indicator which shows how often the serial number is changed
                changeLetterPoint = 100000.0

                # amount of all serial number's changes on the end of year
                maxAmountOfCycles = math.floor(yearToAmountOfAllReleasedIDs[str(yearOfRelease)] / changeLetterPoint)

                # amount of all serial number's changes on the beginning of year
                minAmountOfCycles2 = math.floor(yearToAmountOfAllReleasedIDs[str(yearOfRelease-1)] / changeLetterPoint)

                # Generate random amount of changes between beginning and end of the year
                randomAmountOfCycle = randint(minAmountOfCycles2, maxAmountOfCycles)


                IDNumber.append(indexOfLetter[math.floor(randomAmountOfCycle / (24 * 24))])
                IDNumber.append(indexOfLetter[math.floor((randomAmountOfCycle % (24 * 24)) / 24)])
                IDNumber.append(indexOfLetter[math.floor((randomAmountOfCycle % (24 * 24)) % 24)])

                #letters = [firstLetter, secondLetter, thirdLetter]
                for i in range(3):
                    checkSum += letterToNumber[IDNumber[i]] * wagi[i]

                #Generate digit's patr of ID's number
                for i in range(5):
                    randomNumber = randint(0, 9)
                    IDNumber.append(str(randomNumber))
                    checkSum += randomNumber * wagi[i + 4]

                remainder = checkSum % 10
                IDNumber.insert(3, remainder)

                print("Your ID is " + str(IDNumber) + " and checksum = " + str(remainder) + " = first digit of ID's number")

                print("This is valid ID")
                f.close()
                return IDNumber
        except IOError:
            print("Could not read file: ", fileName)

if __name__ == '__main__':
    generateID(2001)