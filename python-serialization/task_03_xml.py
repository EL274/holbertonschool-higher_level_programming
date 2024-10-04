#!/usr/bin/python3


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Create the root element
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.Element(str(key))
        child.text = str(value)
        root.append(child)
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Dictionary serialized to {filename} successfully.")


def deserialize_from_xml(filename):
    # Parse the XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    dictionary = {}
    # Iterate through the XML elements and add them to the dictionary
    for child in root:
        dictionary[child.tag] = child.text
    print(f"Data deserialized from {filename} successfully.")
    return dictionary
