import sqlite3

def sqlite3_tables_creation():
    con = sqlite3.connect('BD_Sqlite.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE Работник(ID integer PRIMARY KEY,
                                        Name TEXT NOT NULL,
                                        Surname TEXT NOT NULL,
                                        Age INTEGER NOT NULL)''')
    big_data = []
    data1 = ["1", "Vlad", "Melnik", "25"]
    data2 = ["2", "Nikolay", "Kodak", "56"]
    data3 = ["3", "Olga", "Fedotva", "20"]
    data4 = ["4", "Oleg", "Babak", "35"]

    big_data.append(data1)
    big_data.append(data2)
    big_data.append(data3)
    big_data.append(data4)

    for data_unit1 in big_data:
        cur.execute('''INSERT INTO Работник VALUES(?, ?, ?, ?)''', data_unit1)
    for i in cur.execute('SELECT * FROM Работник'):
        print(i)
    con.commit()


    cur.execute('''CREATE TABLE Зарплата(ID integer PRIMARY KEY NOT NULL,
                                        Name TEXT NOT NULL,
                                        Surname TEXT NOT NULL,
                                        Salary1 INTEGER NOT NULL,
                                        FOREIGN KEY (ID) REFERENCES Работник (ID))''')
    big_data = []
    data1 = ["1","Vlad", "Melnik", "56354"]
    data2 = ["2", "Nikolay", "Kodak", "4524"]
    data3 = ["3", "Olga", "Fedotva", "8556"]
    data4 = ["4", "Oleg", "Babak", "7854"]

    big_data.append(data1)
    big_data.append(data2)
    big_data.append(data3)
    big_data.append(data4)

    for data_unit2 in big_data:
        cur.execute('''INSERT INTO Зарплата VALUES(?, ?, ?, ?)''', data_unit2)
    for i in cur.execute('SELECT * FROM Зарплата'):
        print(i)
    con.commit()

    cur.execute('''CREATE TABLE Должность(ID integer PRIMARY KEY NOT NULL,
                                        Name TEXT NOT NULL,
                                        Surname TEXT NOT NULL,
                                        Должнось TEXT NOT NULL,
                                        FOREIGN KEY (ID) REFERENCES Работник (ID))''')
    big_data = []
    data1 = ["1","Vlad", "Melnik", "Тестировщик"]
    data2 = ["2", "Nikolay", "Kodak", "Разработчик"]
    data3 = ["3", "Olga", "Fedotva", "Менеджер"]
    data4 = ["4", "Oleg", "Babak", "Руководитель"]

    big_data.append(data1)
    big_data.append(data2)
    big_data.append(data3)
    big_data.append(data4)

    for data_unit3 in big_data:
        cur.execute('''INSERT INTO Должность VALUES(?, ?, ?, ?)''', data_unit3)
    for i in cur.execute('SELECT * FROM Должность'):
        print(i)
    con.commit()
    cur.close()
    con.close()


sqlite3_tables_creation()