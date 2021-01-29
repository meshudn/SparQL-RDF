import rdflib
import requests
g = rdflib.Graph()

g.parse("dummy.rdf")

qres = g.query(
    """SELECT DISTINCT ?name ?expertise
       WHERE {
          ?a researchee:name ?name .
          ?a researchee:hasExpertise ?expertise .
       }""")

for row in qres:
    #print("%s %s" % row)
    value = row
