import random

def generate_k_colorable_graph(n, k, p):

    subsets = [[] for i in range(k)]
    for i in range(1, n+1):
        index = random.randint(0, k-1)
        subsets[index].append(i)

    # Generate edges between vertices
    edges = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            in_set = False
            for subset in subsets:
                if i in subset and j in subset:
                    in_same_subset = True
                    break
            if not in_set and random.random() < p:
                edges.append((i, j))

    return edges



def first_fit_coloring(graph, k):
    # Initialize empty coloring
    coloring = {}

    for v in range(1, n+1):
        # Find neighbors of v in current partial graph
        v_neighbors = [u for u in range(1, v) if (u, v) in graph or (v, u) in graph]

        # Find smallest unused color for v
        used_colors = {coloring[u] for u in v_neighbors if u in coloring}
        for color in range(1, n+1):
            if color not in used_colors:
                coloring[v] = color
                break

    # Calculate competitive ratio
    num_colors = max(coloring.values())
    competitive_ratio = num_colors / k

    return competitive_ratio


# Define Parameters
ks = [2, 3, 4]
N = 100
p = 0.3
ns = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

for n in ns:
    for j in ks:

        # Generating 100 k-colorable graphs, and running First Fit algorithm
        competitive_ratios = []
        for i in range(N):

            graph = generate_k_colorable_graph(n, j, p)
            competitive_ratio = first_fit_coloring(graph, 2)
            competitive_ratios.append(competitive_ratio)

        avg_competitive_ratio = sum(competitive_ratios) / (2.5*N)

        print("n =", n, ", Average competitive ratio for " + str(j) + "-colorable graph:", avg_competitive_ratio)

