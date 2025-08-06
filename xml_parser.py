import xml.etree.ElementTree as ET
from collections import Counter
import matplotlib.pyplot as plt

def parse_xml(file_path):
    """
    Parses an XML file and returns a Counter of spell categories.

    Args:
        file_path (str): The path to the XML file.
    """
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        categories = []
        for child in root:
            if child.tag in ["activespell", "passivespell"]:
                category = child.get("category")
                if category:
                    categories.append(category)
        return Counter(categories)

    except ET.ParseError as e:
        print(f"Error parsing XML file: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return None

def plot_bar_chart(category_counts):
    """
    Plots a bar chart of spell categories.

    Args:
        category_counts (Counter): A Counter of spell categories.
    """
    labels, values = zip(*category_counts.items())
    plt.figure(figsize=(12, 6))
    plt.bar(labels, values)
    plt.xlabel("Category")
    plt.ylabel("Number of Spells")
    plt.title("Distribution of Spell Categories")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("spell_categories.png")
    print("Bar chart saved as spell_categories.png")

if __name__ == "__main__":
    category_counts = parse_xml("spells.xml")
    if category_counts:
        plot_bar_chart(category_counts)
