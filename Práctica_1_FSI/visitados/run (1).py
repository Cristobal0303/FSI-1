# Search methods
import time
import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)
oe = search.GPSProblem('O', 'E'
                       , search.romania)
gz = search.GPSProblem('G', 'Z'
                       , search.romania)
nd = search.GPSProblem('N', 'D'
                       , search.romania)
mf = search.GPSProblem('M', 'F'
                       , search.romania)

list_cities = [ab, oe, gz, nd, mf]

for city in list_cities:

    print("BFS")
    start_time = time.perf_counter()
    print(search.breadth_first_graph_search(city).path())
    end_time = time.perf_counter()
    print("El tiempo que ha tardado es de: ", end_time - start_time, " segundos")
    print("")
    
    print("DFS")
    start_time = time.perf_counter()
    print(search.depth_first_graph_search(city).path())
    end_time = time.perf_counter()
    print("El tiempo que ha tardado es de: ", end_time - start_time, " segundos")
    print("")

    start_time = time.perf_counter()
    print("Ramificación y acotación")
    print(search.branch_and_bound(city).path())
    end_time = time.perf_counter()
    print("El tiempo que ha tardado es de: ", end_time - start_time, " segundos")
    print("")

    start_time = time.perf_counter()
    print("Ramificación y acotación con subestimación")
    print(search.branch_and_bound_h(city).path())
    end_time = time.perf_counter()
    print("El tiempo que ha tardado es de: ", end_time - start_time, " segundos")
    print("")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
