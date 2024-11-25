def greedy_optimization(data, max_cost):
    """
    Solves a greedy optimization problem where the goal is to maximize value 
    while staying within a maximum cost.

    Parameters:
    data: A list of dictionaries, each with 'cost' and 'value' keys.
    max_cost: The maximum allowable cost for the solution.

    Returns:
    solution: The list of selected items.
    total_value: The total value of the selected items.
    """
    # Step 1: Sort candidates by a greedy heuristic (e.g., value-to-cost ratio)
    candidates = sorted(data, key=lambda x: x['value'] / x['cost'], reverse=True)
    
    # Step 2: Initialize solution and total cost/value trackers
    solution = []
    total_cost = 0
    total_value = 0

    # Step 3: Iterate through the sorted candidates and select greedily
    for candidate in candidates:
        if total_cost + candidate['cost'] <= max_cost:  # Check feasibility
            solution.append(candidate)  # Add candidate to solution
            total_cost += candidate['cost']  # Update total cost
            total_value += candidate['value']  # Update total value

    # Step 4: Return the solution and total value
    return solution, total_value


# Example Usage
data = [
    {'cost': 10, 'value': 60},
    {'cost': 20, 'value': 100},
    {'cost': 30, 'value': 120},
]
max_cost = 50

solution, total_value = greedy_optimization(data, max_cost)
print("Selected Items:", solution)
print("Total Value:", total_value)
