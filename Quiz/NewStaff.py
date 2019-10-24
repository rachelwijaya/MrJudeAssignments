
class NewStaff:
    __id = ""
    __name = ""
    __position = ""
    __salary = 0
    def __init__(self, id, name, position, salary):
        self.__id = id
        self.__name = name
        self.__position = position
        self.__salary = salary

    def setID(self):
        id = input("Input ID[SXXXX]: ")
        if len(id) == 5 and id[1] == 'S':
            if (type(id[1:4]) == type(5)) and (id not in idList):
                return self.__id
            else:
                setID()
        else:
            setID()

    def setName(self):
        name = input("Input name[0...20]: ")
        if len(name) <= 20:
            return self.__name
        else:
            setName()

    def setPosition(self):
        position = input("Input position[Staff|Manager|Office]: ")
        posOptions = ["Staff", "Manager", "Office"]
        if position in posOptions:
            return self.__position
        else:
            setPosition()

    def setSalary(self):
        salary = input("Input salary for " + position)
        if position == "Staff":
            if salary < 3500000 and salary > 7000000:
                return self.__salary
            else:
                setSalary()
        elif position == "Officer":
            if salary < 7000001 and salary > 10000000:
                return self.__salary
            else:
                setSalary()
        elif position == "Manager":
            if salary > 10000000:
                return self.__salary
            else:
                setSalary()
        else:
            setSalary()

    def main(self):
        self.setID()
        self.setName()
        self.setPosition()
        self.setSalary()

    def toString(self):
        string = self.__id + "#" + self.__name + "#" + self.__position + "#" + self.__salary
        with open("data.txt", 'w') as f:
            f.write(string)