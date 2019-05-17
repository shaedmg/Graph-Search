# Search methods

import search

ab = search.GPSProblem('A', 'B' , search.romania)
az = search.GPSProblem('A', 'Z' , search.romania)
ad = search.GPSProblem('A', 'D' , search.romania)
asa = search.GPSProblem('A', 'S' , search.romania)
ag = search.GPSProblem('A', 'G' , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
print("Ramificacion y acotacion sin subestimacion" , search.bab(ab).path())
print("Ramificacion y acotacion con subestimacion" ,search.heur(ab).path())
print("Ramificacion y acotacion sin subestimacion" ,search.bab(az).path())
print("Ramificacion y acotacion con subestimacion" ,search.heur(az).path())
print("Ramificacion y acotacion sin subestimacion" ,search.bab(ad).path())
print("Ramificacion y acotacion con subestimacion" ,search.heur(ad).path())
print("Ramificacion y acotacion sin subestimacion" ,search.bab(asa).path())
print("Ramificacion y acotacion con subestimacion" ,search.heur(asa).path())
print("Ramificacion y acotacion sin subestimacion" ,search.bab(ag).path())
print("Ramificacion y acotacion con subestimacion" ,search.heur(ag).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
