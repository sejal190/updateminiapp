import xml.etree.ElementTree as ET

def update_element(ps_no, element_name, new_value):
    try:
        # Load the XML file into an ElementTree object
        tree = ET.ElementTree(file='Employee.xml')

        # Get the root element of the XML file
        root = tree.getroot()

        # Loop through each employee element
        for employee in root:
            # Check if the PS.No. of the current employee element matches the provided PS.No.
            if employee.find('PS.No.').text == ps_no:
                # Find the element to be updated
                element = employee.find(element_name)

                # Update the value of the element
                element.text = new_value

                # Write the updated XML tree to the file
                tree.write('Employee.xml')

                # Return success message
                # return f"Successfully updated {element_name} for PS.No. {ps_no} to {new_value}"
                print(f"Successfully updated {element_name} for PS.No. {ps_no} to {new_value}")
                break

        # Return failure message if employee with provided PS.No. not found
        # return f"Employee with PS.No. {ps_no} not found"
            else:
                return f"Employee with entered PS.No. not found"
    except FileNotFoundError:
        return "Employee.xml file not found."
    # except Exception as e:
    #     return f"An error occurred while updating the element"
