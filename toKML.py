import json
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Load JSON data
with open('data.json', 'r', encoding='utf-8') as f:
	data = json.load(f)

# Create KML structure
kml = Element('kml', xmlns="http://www.opengis.net/kml/2.2")
document = SubElement(kml, 'Document')

# Iterate through features and extract coordinates and STREET_NAME_TC
for feature in data['features']:
	coordinates = feature['geometry']['coordinates']
	street_name_tc = feature['properties']['STREET_NAME_TC']
	
	placemark = SubElement(document, 'Placemark')
	name = SubElement(placemark, 'name')
	name.text = street_name_tc
	
	point = SubElement(placemark, 'Point')
	coord = SubElement(point, 'coordinates')
	coord.text = f"{coordinates[0]},{coordinates[1]}"

# Write to KML file
tree = ElementTree(kml)
tree.write('output.kml', encoding='utf-8', xml_declaration=True)