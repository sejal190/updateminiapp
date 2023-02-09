import xml.etree.ElementTree as ET

root = ET.Element("Employees")

employee = ET.SubElement(root, "Employee")

ps_no = ET.SubElement(employee, "PS.No.")
ps_no.text = "1"

employee_name = ET.SubElement(employee, "Employee_Name")
employee_name.text = "John Doe"

dob = ET.SubElement(employee, "DOB")
dob.text = "01-01-2000"

doj = ET.SubElement(employee, "DOJ")
doj.text = "01-01-2020"

dor = ET.SubElement(employee, "DOR")
dor.text = "01-01-2022"

email = ET.SubElement(employee, "Email")
email.text = "johndoe@example.com"

contact = ET.SubElement(employee, "Contact")
contact.text = "1234567890"

designation = ET.SubElement(employee, "Designation")
designation.text = "Software Engineer"

business_unit = ET.SubElement(employee, "Business_Unit")
business_unit.text = "Software Development"

base_location = ET.SubElement(employee, "Base_Location")
base_location.text = "Mumbai"

ltts_grade = ET.SubElement(employee, "LTTS_Grade")
ltts_grade.text = "Grade A"

tree = ET.ElementTree(root)
tree.write("Employee.xml")
