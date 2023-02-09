from ReadXml import *
from EntireData import *
from XmltoDict import *
from hierarchydata import *
from Update import *
from delete import *
from excel import *
import os
while True:
    a = int(input("Enter choice"))
    if a==1:
        view_data("Employee.xml")
    elif a==2:
        ReadXml()
    elif a==3:
        xml_to_dict("Employee.xml")
    elif a==4:
        xml_hierarchy_re(xml_string, "Employees")
    elif a==5:
        xml_to_excel('Employee.xml', 'Employee.xlsx')
    elif a==6:
        file="Employee.xml"
        delete_element(file, "Employee", "Employee_Name", "Sejal")
        print("deleted sucessfully")
    elif a==7:

        q=print(update_element('12345', 'Employee_Name', 'Shanm'))
        if(q!=None):
            os.remove("Employee.xlsx")
            xml_to_excel('Employee.xml', 'Employee.xlsx')
    else:
        print("----------Enter a valid input----------")


