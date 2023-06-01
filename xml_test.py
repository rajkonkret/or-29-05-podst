from xml.dom import minidom

DOMTree = minidom.parse('dane_xml.xml')

print(DOMTree.toxml())

cNodes = DOMTree.childNodes
print(cNodes)  # [<DOM Element: znajomi at 0x2203b4f04b0>]
print(cNodes[0].getElementsByTagName('osoba')[0].toxml())
print(cNodes[0].getElementsByTagName('osoba')[1].toxml())
# <imie foo="aaaa">Janina</imie>
print(cNodes[0].getElementsByTagName('osoba')[1].getElementsByTagName('imie')[0].toxml())
