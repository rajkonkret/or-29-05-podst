import xml.etree.ElementTree as ET


def generate_XML(filename):
    root = ET.Element("Catalog")

    m1 = ET.Element("mobile")
    root.append(m1)

    b1 = ET.SubElement(m1, "brand")
    b1.text = "Redmi"
    b2 = ET.SubElement(m1, "price")
    b2.text = "6999"

    m2 = ET.Element('mobile')
    root.append(m2)

    tree = ET.ElementTree(root)

    with open(filename, 'wb') as file:
        tree.write(file)


# uruchomi sie tylko gdy ten plik bedzie uruchomiony bezpośrednio
if __name__ == '__main__':
    generate_XML('Catalog.xml')  # <Catalog><mobile><brand>Redmi</brand><price>6999</price></mobile><mobile /></Catalog>
