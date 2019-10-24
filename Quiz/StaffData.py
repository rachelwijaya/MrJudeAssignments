import statistics as st
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
                StaffData.setID()
        else:
            StaffData.setID()

    def setName(self):
        name = input("Input name[0...20]: ")
        if len(name) <= 20:
            return self.name
        else:
            StaffData.setName()

    def setPosition(self):
        position = input("Input position[Staff|Manager|Office]: ")
        posOptions = ["Staff", "Manager", "Office"]
        if position in posOptions:
            return self.position
        else:
            StaffData.setPosition()

    def setSalary(self):
        salary = input("Input salary for " + position)
        if position == "Staff":
            if salary < 3500000 and salary > 7000000:
                return self.salary
            else:
                StaffData.setSalary()
        elif position == "Officer":
            if salary < 7000001 and salary > 10000000:
                return self.salary
            else:
                StaffData.setSalary()
        elif position == "Manager":
            if salary > 10000000:
                return self.salary
            else:
                StaffData.setSalary()
        else:
            StaffData.setSalary()

    def newStaff(self):
        self.id = StaffData.setID()
        self.name = StaffData.setName()
        self.position = StaffData.setPosition()
        self.salary = StaffData.setSalary()
        dataList = []
        dataList.append(self.id)
        dataList.append(self.name)
        dataList.append(self.position)
        dataList.append(self.salary)
        getData().allData.append(dataList)

    def findID(self):
        id = input("Input ID[SXXXX]: ")
        data = getData().allData
        for i, j in range(len(data)):
            if data[i][j] == data[i][id]:
                del allData[i]
            else:
                StaffData.findID()

    def deleteStaff(self):
        StaffData.findID()
        StaffData.getData()

    def summary(self):
        staffSal, officerSal, managerSal = [],[],[]
        data = getData().allData
        for i in range(len(data)):
            if data[i][2] == "Staff":
                staffSal.append(data[3])
            elif data[i][2] == "Officer":
                officerSal.append(data[3])
            elif data[i][2] == "Manager":
                managerSal.append(data[3])

        print("1. Staff")
        print("Minimum salary: ", min(staffSal))
        print("Maximum salary: ", max(staffSal))
        print("Average salary: ", st.mean(staffSal))
        print("2. Officer")
        print("Minimum salary: ", min(officerSal))
        print("Maximum salary: ", max(officerSal))
        print("Average salary: ", st.mean(officerSal))
        print("3. Manager")
        print("Minimum salary: ", min(managerSal))
        print("Maximum salary: ", max(managerSal))
        print("Average salary: ", st.mean(managerSal))




#
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
    while True:
        choice = int(input("Input Choice: ")
        if choice == 1:
            StaffData.newStaff()
        elif choice == 2:
            StaffData.deleteStaff()
        elif choice == 3:
            StaffData.summary()
        #elif choice == 4:
            #return False
        else:
            mainMenu()

        mainMenu()





getData()
mainMenu()