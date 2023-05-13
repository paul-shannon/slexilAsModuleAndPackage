import unittest
import slexil
from xml.etree import ElementTree as etree

eafFile = '../data/infernoDemo/inferno-threeLines.eaf'
tierGuide = '../data/infernoDemo/tierGuide.yaml'

class TestListTiers(unittest.TestCase):

	def test_tierCount(self):
		print("--- running test_listTiers.py, test_tierCount")
		tree = etree.parse(eafFile)
		root = tree.getroot()
		root.tag
		root.attrib
		tierElements = root.findall("TIER")
		self.assertEqual(len(tierElements), 4)


