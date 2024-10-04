#!/usr/bin/python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Create the root element
    root = ET.Element('data')
    
    # Iterate through the dictionary items and add them as child elements
    for key, value in dictionary.items():
        # Create a child element with key as the tag and value as the text
        child = ET.Element(str(key))
        child.text = str(value)
        root.append(child)
    
    # Write the XML tree to the provided filename
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Dictionary serialized to {filename} successfully.")



def deserialize_from_xml(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    
    # Create an empty dictionary to store the deserialized data
    dictionary = {}
    
    # Iterate through the XML elements and add them to the dictionary
    for child in root:
        dictionary[child.tag] = child.text
    
    print(f"Data deserialized from {filename} successfully.")
    return dictionary

# Example usage
if __name__ == "__main__":
    # Sample dictionary to serialize
    sample_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
    
    # Serialize the dictionary to XML
    serialize_to_xml(sample_dict, 'task_03_xml.xml')
    
    # Deserialize the XML back to a dictionary
    deserialized_dict = deserialize_from_xml('task_03_xml.xml')
    
    # Output the deserialized dictionary
    print(deserialized_dict)

