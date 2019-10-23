#import NewStaff as ns

path = "data.txt"
with open(path, 'r') as f:
    contents = f.readlines()

    # Make a list called allData, stores list of each employee's data in one list
    allData = []
    for line in contents:
        for word in line:
            dataList = [] # a list of each employee's data
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

    #for x, y in range(len(allData)):
print(idList)
print(nameList)
print(positionList)
print(salaryList)
print(allData)