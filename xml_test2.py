from xml.dom import minidom

root = minidom.Document()
xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', 'Geek')

xml.appendChild(productChild)
xml_str = root.toprettyxml(indent='\t')
print(xml_str)

save_path = 'gfg.xml'

with open(save_path, 'w') as f:
    f.write(xml_str)
#
# <?xml version="1.0" ?>
# <root>
# 	<product name="Geek"/>
# </root>
