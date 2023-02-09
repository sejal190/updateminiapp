'''import xml.etree.ElementTree as ET

def xml_to_dict(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    employees = []
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

        employee_data = {
            "PS.No.": ps_no,
            "Employee Name": employee_name,
            "DOB": dob,
            "DOJ": doj,
            "DOR": dor,
            "Email": email,
            "Contact": contact,
            "Designation": designation,
            "Business Unit": business_unit,
            "Base Location": base_location,
            "LTTS Grade": ltts_grade
        }
        employees.append(employee_data)
        #return employees
employee_data = xml_to_dict("Employee.xml")
print(employee_data)
'''
def xml_to_dict(filename):
  import xmltodict
  import pprint
  with open(filename, 'r', encoding='utf-8') as file:
    my_xml = file.read()
  my_dict = xmltodict.parse(my_xml)
  pprint.pprint(my_dict, indent=2)
