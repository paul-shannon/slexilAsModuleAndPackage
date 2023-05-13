import unittest
from slexil.morphemeGloss import MorphemeGloss
import pdb
import yattag

rawText = "in=DEF:MASC:SG	middle-MASC:SG	of=DEF:MASC:SG	journey–MASC:SG	of	our-FEM:SG	life-FEM"
termsFile = "../data/infernoDemo/grammaticalTerms.txt"
termsRaw = open(termsFile).readlines()
grammaticalTerms = [term.strip() for term in termsRaw]
tierGuide = '../data/infernoDemo/tierGuide.yaml'

class TestMorphemeGloss(unittest.TestCase):

	def test_morphemGloss(self):
		print("--- test_morphemeGloss")
		mg = MorphemeGloss(rawText, grammaticalTerms)
		mg.parse()
		parts = mg.getParts()
		self.assertEqual(len(parts), 27)

	def test_getTermsList(self):
		print("--- test_getTermsList")
		mg = MorphemeGloss(rawText, grammaticalTerms)
		mg.parse()
		terms = mg.getTermsList()
		self.assertEqual(terms, grammaticalTerms)

	def test_HTML(self):
		print("--- test_getHTML")
		mg = MorphemeGloss(rawText, grammaticalTerms)
		mg.parse()
		htmlDoc = yattag.Doc()
		mg.toHTML(htmlDoc)
		html = htmlDoc.getvalue()
		self.assertEqual(html.count("grammatical-term"), 8)
