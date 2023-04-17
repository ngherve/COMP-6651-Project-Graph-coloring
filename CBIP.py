import random

def generate_2colorable_graph(n, k, p):
    # Partition {1,2,...,n} into k disjoint subsets
    subsets = [[] for i in range(k)]
    for i in range(1, n+1):
        subset_idx = random.randint(0, k-1)
        subsets[subset_idx].append(i)

    # Generate edges between vertices
    edges = set()
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            in_same_subset = False
            for subset in subsets:
                if i in subset and j in subset:
                    in_same_subset = True
                    break
            if not in_same_subset and random.random() < p:
                edges.add((i, j))

    return edges

def CBIP(graph):
    # Initialize empty coloring
    coloring = {}

    for v in range(1, n+1):
        # Find 2-coloring of current partial graph
        v_neighbors = [u for u in range(1, v) if (u, v) in graph or (v, u) in graph]
        Hv = {v} | set(v_neighbors)
        independent_sets = []
        for u in range(1, v):
            if u not in Hv and all((u, w) not in graph and (w, u) not in graph for w in Hv):
                # u is independent of Hv
                for i, independent_set in enumerate(independent_sets):
                    if all((u, w) not in graph and (w, u) not in graph for w in independent_set):
                        independent_set.add(u)
                        break
                else:
                    independent_sets.append({u})

        # Color v with the smallest unused color
        used_colors = {coloring[u] for u in v_neighbors if u in coloring}
        for color in range(1, len(independent_sets)+2):
            if color not in used_colors:
                coloring[v] = color
                break

    # Calculate competitive ratio
    num_colors = max(coloring.values())
    competitive_ratio = num_colors / 2

    return competitive_ratio


# Set parameters
N = 100
k = 2
p = 0.3

# Set n values to be tested
n_values = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]

avg_competitive_ratios = []
for n in n_values:
    competitive_ratios = []
    for i in range(N):
        graph = generate_2colorable_graph(n, k, p)
        competitive_ratio = CBIP(graph)
        competitive_ratios.append(competitive_ratio)

    # Calculate average competitive ratio
    avg_competitive_ratio = sum(competitive_ratios) / N
    avg_competitive_ratios.append(avg_competitive_ratio)

    # Print results
    print("n =", n, "Average competitive ratio:", avg_competitive_ratio)