import rdflib
import requests
g = rdflib.Graph()
g2 = rdflib.Graph()

g.parse("dummy.rdf")
g2.parse("expertise.rdf")

qres = g.query(
    """SELECT DISTINCT ?name ?expertise
       WHERE {
          ?a researchee:name ?name .
          ?a researchee:hasExpertise ?expertise .
       }""")

for row in qres:
    #print("%s %s" % row)
    value = row

qres2 = g2.query(
        """SELECT DISTINCT ?name
           WHERE {
              ?name ?predicate ?object .
              FILTER (?name = "http://wirtrials.app.web/researchee#expertise1")
           }
           """)
for row2 in qres2:
     print("%s " % row2)