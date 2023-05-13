from xml.etree import ElementTree as etree
import sys, os
import yaml
sys.path.append("../src/slexil")
from ijalLine import IjalLine as line
import pandas as pd
pd.set_option('display.max_columns', 500)

dataPath = "../data/infernoDemo"

def test_inferno():
    print("--- test_inferno")

    filename = "../data/infernoDemo/inferno-threeLines.eaf"
    xmlDoc = etree.parse(filename)
    lineCount = len(xmlDoc.findall("TIER/ANNOTATION/ALIGNABLE_ANNOTATION"))
    for lineNumber in range(lineCount):
        rootElement = xmlDoc.findall("TIER/ANNOTATION/ALIGNABLE_ANNOTATION")[lineNumber]
        pdb.set_trace()
        allElements = findChildren(xmlDoc, rootElement)
        tmpTbl = buildTable(xmlDoc, allElements)
        # print("---- line %d" % lineNumber)
        # print(tmpTbl)

        tierGuideFile = "../data/infernoDemo/tierGuide.yaml"
        with open(tierGuideFile, 'r') as f:
            tierGuide = yaml.safe_load(f)

    lines = []
    grammaticalTerms = ["hab", "past"]
    for i in range(lineCount):
        line = IjalLine(xmlDoc, i, tierGuide, grammaticalTerms)

