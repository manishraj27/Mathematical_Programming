import numpy as np


def northwest_corner_method(cost_matrix, supply, demand):
    allocation = np.zeros_like(cost_matrix)
    i, j = 0, 0

    while i < len(supply) and j < len(demand):
        quantity = min(supply[i], demand[j])
        allocation[i][j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0:
            i += 1
        else:
            j += 1

    return allocation


# Example data
cost_matrix = np.array([[10, 20, 30],
                        [15, 25, 35],
                        [25, 30, 40]])

supply = [20, 30, 40]
demand = [30, 40, 25]

# Apply Northwest Corner Method
allocation_matrix = northwest_corner_method(cost_matrix, supply, demand)

print("Allocation Matrix:")
print(allocation_matrix)
