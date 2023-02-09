import xml.etree.ElementTree as ET

def ReadXml():
    tree = ET.parse("Employee.xml")
    root = tree.getroot()

    for employee in root.findall("Employee"):
        ps_no = employee.find("PS.No.").text
        employee_name = employee.find("Employee_Name").text
        dob = employee.find("DOB").text
        doj = employee.find("DOJ").text
        dor = employee.find("DOR").text
        email = employee.find("Email").text
        contact = employee.find("Contact").text
        designation = employee.find("Designation").text
        business_unit = employee.find("Business_Unit").text
        base_location = employee.find("Base_Location").text
        ltts_grade = employee.find("LTTS_Grade").text

        print("PS.No.:", ps_no)
        print("Employee Name:", employee_name)
        print("DOB:", dob)
        print("DOJ:", doj)
        print("DOR:", dor)
        print("Email:", email)
        print("Contact:", contact)
        print("Designation:", designation)
        print("Business Unit:", business_unit)
        print("Base Location:", base_location)
        print("LTTS Grade:", ltts_grade)
        print("\n")
