def getData():
    path = "data.txt"
    with open(path, 'r') as f:
        contents = f.readlines()

        # Make a list called allData, stores list of each employee's data in one list
        allData = []
        for line in contents:
            for word in line:
                dataList = []  # a list of each employee's data
                string = line.split("#")

            allData.append(string)
        idList = []
        for i in range(len(allData)):
            idList.append(allData[i][0])

        nameList = []
        for i in range(len(allData)):
            nameList.append(allData[i][1])

        positionList = []
        for i in range(len(allData)):
            positionList.append(allData[i][2])

        salaryList = []
        for i in range(len(allData)):
            salaryList.append(allData[i][3])


class StaffData:

    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary

    def setID(self):
        id = input("Input ID[SXXXX]: ")
        if len(id) == 5 and id[1] == 'S':
            if (type(id[1:4]) == type(5)) and (id not in idList):
                return self.id
            else:
                setID()
        else:
            setID()

    def setName(self):
        name = input("Input name[0...20]: ")
        if len(name) <= 20:
            return self.name
        else:
            setName()

    def setPosition(self):
        position = input("Input position[Staff|Manager|Office]: ")
        posOptions = ["Staff", "Manager", "Office"]
        if position in posOptions:
            return self.position
        else:
            setPosition()

    def setSalary(self):
        salary = input("Input salary for " + position)
        if position == "Staff":
            if salary < 3500000 and salary > 7000000:
                return self.salary
            else:
                setSalary()
        elif position == "Officer":
            if salary < 7000001 and salary > 10000000:
                return self.salary
            else:
                setSalary()
        elif position == "Manager":
            if salary > 10000000:
                return self.salary
            else:
                setSalary()
        else:
            setSalary()

    def main():
        StaffData.setID()
        StaffData.setName()
        StaffData.setPosition()
        StaffData.setSalary()

    def findID():
        id = input("Input ID[SXXXX]: ")

        for i, j in range(len(allData)):
            if j == id:
                del allData[i]
            else:
                findID()

    def deleteStaff():
        findID()
        #with open(path, )
        getData()

#for x, y in range(len(allData)):
#print(idList)
#print(nameList)
#print(positionList)
#print(salaryList)
#print(allData)

def mainMenu():
    print("1. New Staff")
    print("2. Delete Staff")
    print("3. View Summary Data")
    print("4. Save & Exit")
    choice = int(input("Input Choice: "))

    if choice == 1:
        StaffData.main()
    elif choice == 2:
        StaffData.deleteStaff()
    elif choice == 3:




getData()
mainMenu()