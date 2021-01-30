import rdflib
import requests
g = rdflib.Graph()
g.parse("dummy.rdf")

qres = g.query(
    """SELECT DISTINCT ?a
       WHERE {
          ?a researchee:hasExpertise ?name .
       }""")

for row in qres:
    print("%s " % row)
    value = row


