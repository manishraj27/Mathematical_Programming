import numpy as np

# Simulated Annealing Function
def simulated_annealing(initial_solution, cost_function, temperature_schedule, max_iterations):
    current_solution = initial_solution
    current_cost = cost_function(current_solution)
    best_solution = current_solution
    best_cost = current_cost

    for iteration in range(max_iterations):
        temperature = temperature_schedule(iteration)
        neighbor_solution = get_neighbor(current_solution)
        neighbor_cost = cost_function(neighbor_solution)

        if neighbor_cost < current_cost or np.random.rand() < np.exp((current_cost - neighbor_cost) / temperature):
            current_solution = neighbor_solution
            current_cost = neighbor_cost

            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        print(f"Iteration {iteration}: Temperature = {temperature}, Current Cost = {current_cost}, Best Cost = {best_cost}")

    return best_solution, best_cost

# Example Cost Function (Replace with your own)
def example_cost_function(solution):
    return sum(solution)

# Example Temperature Schedule (Replace with your own)
def example_temperature_schedule(iteration):
    return 1 / (iteration + 1)

# Example Neighbor Generation Function (Replace with your own)
def get_neighbor(solution):
    return [1 if np.random.rand() < 0.5 else 0 for _ in range(len(solution))]

# Example Initial Solution (Replace with your own)
initial_solution = [0, 1, 0, 1, 0]

# Example Max Iterations (Replace with your own)
max_iterations = 10

# Run Simulated Annealing
best_solution, best_cost = simulated_annealing(initial_solution, example_cost_function, example_temperature_schedule, max_iterations)

print("\nFinal Best Solution:", best_solution)
print("Final Best Cost:", best_cost)
