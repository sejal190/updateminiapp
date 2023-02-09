import xml.etree.ElementTree as ET
def delete_element(file, element_name, tag_name, tag_value):
    tree = ET.parse(file)
    root = tree.getroot()

    for elem in root.findall(element_name):
        if elem.find(tag_name).text == tag_value:
            root.remove(elem)
    tree.write(file)
    file ="Employee.xml"

# Example usage:
#file = "Employee.xml"
#delete_element(file, "Employee", "Employee_Name", "super sejal")