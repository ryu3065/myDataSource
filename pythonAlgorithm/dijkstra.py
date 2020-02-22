graph = {}
graph["start"] = {}
graph["start"]['a'] = 6
graph["start"]['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['fin'] = 5
graph['b']['a']= 3
graph['fin'] = {}

costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = float('inf')

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

visited = []


def find_lowest_cost_node(costs):
  lowest_cost = float("inf")
  lowest_cost_node = None
  #print("find_lowest_cost_node")
  for n in costs:
    cost = costs[n]
    if cost < lowest_cost and n not in visited:
      lowest_cost = cost
      lowest_cost_node = n
      #print(n, costs, lowest_cost_node)
  return lowest_cost_node
  

def dijkstra(graph, parents, costs):
  node = find_lowest_cost_node(costs)
  while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
      print("n :", n)
      print("visited :",visited)
      new_cost = cost + neighbors[n]
      if costs[n] > new_cost:
        costs[n] = new_cost
        parents[n] = node
      #print(costs,parents)
    visited.append(node)
    node = find_lowest_cost_node(costs)
  return visited
print(costs)
print(dijkstra(graph, parents, costs), costs)


