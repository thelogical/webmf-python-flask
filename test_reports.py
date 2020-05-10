import xml.etree.ElementTree as ET 
import os

filename = os.listdir('test-results')[0]
tree = ET.parse('test-results/'+filename)
root = tree.getroot()
stats = root.attrib
print("Unit test summary......")
print("Errors: {}".format(stats['errors']))
print("Failures: {}".format(stats['failures']))
print("Tests: {}".format(stats['tests']))
print("Total execution time: {}".format(stats['time']))

assert stats['errors'] == '0' or stats['failures'] == 0, 'Some tests failed'

if stats['errors'] == '0' and stats['failures'] == '0':
    print("")
    print("All Unit tests cleared")
