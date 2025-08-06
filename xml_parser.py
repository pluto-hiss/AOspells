import xml.etree.ElementTree as ET

def parse_xml(file_path):
    """
    Parses an XML file and prints its content.

    Args:
        file_path (str): The path to the XML file.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        print(f"Root element: {root.tag}")
        print("-" * 20)

        for child in root:
            print(f"Tag: {child.tag}, Attributes: {child.attrib}")
            for sub_child in child:
                print(f"\tSub-Tag: {sub_child.tag}, Text: {sub_child.text}")
            print("-" * 10)

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    parse_xml("spells.xml")
