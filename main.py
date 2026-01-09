import pulp

#This is a theoretical situation

# Nodes
plants = ['P1', 'P2', 'P3']
dcs = ['DC1', 'DC2']
retailers = ['R1', 'R2', 'R3', 'R4']

# Supply Capacities (We have plenty of production)
supply = {
    'P1': 1000,
    'P2': 1000,
    'P3': 1000
}

# Demand (High demand to stress the network)
demand = {
    'R1': 300,
    'R2': 500,
    'R3': 400,
    'R4': 400
}
# Total Demand = 1600 units

# DC Capacity (The Bottleneck!)
# We are limiting DC1 to 400. It is a popular hub, so this will hurt.
dc_capacity = {
    'DC1': 400,   # <--- THIS is the constrained resource
    'DC2': 1500   # DC2 has plenty of space
}

# Transportation Costs
# We make DC1 cheaper for many routes, making it the "preferred" path.
costs = {}

# P1 is very close to DC1 (Cost 2)
# P2 is far from DC2 (Cost 5)
cost_matrix_p_dc = [
    [2, 5], # P1 -> DC1, DC2
    [5, 3], # P2 -> DC1, DC2
    [6, 5]  # P3 -> DC1, DC2
]

cost_matrix_dc_r = [
    [2, 4, 5, 7], # DC1 -> Retailers (Generally cheaper)
    [4, 3, 6, 8]  # DC2 -> Retailers (Generally more expensive)
]

# Populate Cost Dictionary
for i, p in enumerate(plants):
    for j, d in enumerate(dcs):
        costs[(p, d)] = cost_matrix_p_dc[i][j]

for i, d in enumerate(dcs):
    for j, r in enumerate(retailers):
        costs[(d, r)] = cost_matrix_dc_r[i][j]

]



model = pulp.LpProblem("Supply_Chain_Optimization", pulp.LpMinimize)

# Variables
flow_p_dc = pulp.LpVariable.dicts("Flow_P_DC", [(p, d) for p in plants for d in dcs], lowBound=0, cat='Continuous')
flow_dc_r = pulp.LpVariable.dicts("Flow_DC_R", [(d, r) for d in dcs for r in retailers], lowBound=0, cat='Continuous')

# Objective: Minimize Cost
model += (
    pulp.lpSum([flow_p_dc[(p, d)] * costs[(p, d)] for p in plants for d in dcs]) +
    pulp.lpSum([flow_dc_r[(d, r)] * costs[(d, r)] for d in dcs for r in retailers])
), "Total_Landed_Cost"

# Constraints
# 1. Supply
for p in plants:
    model += pulp.lpSum([flow_p_dc[(p, d)] for d in dcs]) <= supply[p], f"Supply_Constraint_{p}"

# 2. Flow Conservation (In = Out)
for d in dcs:
    inflow = pulp.lpSum([flow_p_dc[(p, d)] for p in plants])
    outflow = pulp.lpSum([flow_dc_r[(d, r)] for r in retailers])
    model += (inflow == outflow, f"Flow_Balance_{d}")

# 3. DC Capacity
for d in dcs:
    inflow = pulp.lpSum([flow_p_dc[(p, d)] for p in plants])
    model += (inflow <= dc_capacity[d], f"DC_Capacity_{d}")

# 4. Demand
for r in retailers:
    model += pulp.lpSum([flow_dc_r[(d, r)] for d in dcs]) >= demand[r], f"Demand_Satisfaction_{r}"




model.solve()

print("="*40)
print(f"STATUS: {pulp.LpStatus[model.status]}")
print(f"TOTAL COST: ${pulp.value(model.objective):,.2f}")
print("="*40)

print("\n--- SENSITIVITY ANALYSIS (SHADOW PRICES) ---")
print("Constraint Name".ljust(25) + " | Shadow Price (Marginal Value)")
print("-" * 55)

for name, c in model.constraints.items():
    # Only print interesting non-zero shadow prices
    if abs(c.pi) > 0.001: 
        print(f"{name.ljust(25)} | ${c.pi:.2f}")

print("\n" + "="*40)
print("INTERPRETATION OF THIS RUN:")
print("1. If 'DC_Capacity_DC1' shows a negative value (e.g., -2.00),")
print("   it means expanding DC1 reduces total cost by $2.00 per unit.")
print("2. If 'Supply_Constraint' is missing, it means we have Excess Capacity.")