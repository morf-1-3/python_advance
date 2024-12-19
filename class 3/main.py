# # #lesson1
# # import os
# # import json
# # PATH = os.path.abspath(__file__ + "/../")
# # FILE_PATH = PATH + "/json.json"
# # print(FILE_PATH)
# # my_dict = {
# #     "First name" : "Muklo",
# #     "Second name" : "ffklo"
# # }

# # with open (FILE_PATH,"w",encoding="utf-8") as file:
# #     json.dump(my_dict,file,ensure_ascii= 2)

# # with open (FILE_PATH,"r") as file:
# #     data = json.load(file)
# # print(type(data))

# # # lesson 3?
# # import os
# # import json
# # import csv
# # PATH = os.path.abspath(__file__ + "/../")
# # FILE_PATH = PATH + "/test.csv"

# # with open(FILE_PATH,"w",newline="") as f:
# #     writer = csv.writer(f)
# #     writer.writerow(["Name", "Lastname", "Point"])
# #     writer.writerow(["PAwl", "LKKFS", "31"])
# #     writer.writerow(["LSfgasg", "FGS", "11"])



# # with open(FILE_PATH,"r") as f:
# #     reader = csv.DictReader(f)
# #     for row in list(reader)[:1]:
# #         print(row)


# import os
# import json
# import csv
# from xml import etree
# import xml.etree.ElementTree as ET
# PATH = os.path.abspath(__file__ + "/../")
# FILE_PATH_CSV = PATH + "/test.csv"
# FILE_PATH = PATH + "/data.xml"
# with open(FILE_PATH,"r") as f:
#     data = f.read()
# data = ET.fromstring(data)
# root = data
# print(root.findall("person"))

# root.attrib["person"] = "SS"
# persons = root.findall("person")
# # persons.append("sfasf")
# with open(FILE_PATH_CSV,"w",newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["first_name","last_name","age"])
#     for person in list(persons):
        
#         name = person.find("first_name")
#         print(name.text)
#         age = person.find("age")
#         last_name = person.find("last_name")
#         writer.writerow([name.text,last_name.text,age.text])

# import os
# import json
# import csv
# PATH = os.path.abspath(__file__ + "/../")
# FILE_PATH = PATH + "/rezult.xml"

# import xml.etree.ElementTree as ET

# data = ET.Element("data")
 
# class User:
#     def __init__(self,id:int, name:str, last_name:str, age:int):
#         self.name = name
#         self.last_name = last_name
#         self.age = age
#         self.id = id
        
# users = [
#     User(1,"Maikl","Levandov",5),
#     User(2,"gagsga","hjjjkj",53),
#     User(3,"kkjyhjmh","awtqwt",55),
#     User(4,"Sasa","kasgsagh",16)
# ]

# for user in users:
#     user_item = ET.SubElement(data,"user")
#     user_item.attrib["id"] = str(user.id)

#     name_item = ET.SubElement(user_item,"name")
#     name_item.text =  user.name

#     last_name_item = ET.SubElement(user_item,"last name")
#     last_name_item.text = user.last_name

#     age_item = ET.SubElement(user_item,"age")
#     age_item.text= str(user.age)

# tree = ET.ElementTree(data)
# tree.write(FILE_PATH,encoding="utf-8",xml_declaration=True)
    
import os
import json
import csv
PATH = os.path.abspath(__file__ + "/../")
FILE_PATH = PATH + "/table.sqlite3"
import sqlite3

db = sqlite3.connect(FILE_PATH)
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PRODUCTS(
               name VARCHAR(255),
               price INTEGER
               ) 

''')
cursor.execute('''
INSERT INTO PRODUCTS (name, price) VALUES (
               "Iphone", 2000)''')
cursor.execute('''
INSERT INTO PRODUCTS (name, price) VALUES (
               "Iphone", 2000)''')
cursor.execute('''
INSERT INTO PRODUCTS (name, price) VALUES (
               "Iphone", 2000)''')

db.commit()