import pulp


model = pulp.LpProblem('Maximize_profit', pulp.LpMaximize)

A = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
B = pulp.LpVariable('Fruit Juice',lowBound=0, cat='Integer')

model += A + B
model += 2*A + B <= 100, 'Constraint of water'
model += A <= 50, 'Constraint of sugar'
model += A <= 30, 'Constraint of lemon juice'
model += 2 * B <= 40, 'Constraint of fruit puree'


model.solve()
print("Produce such amount of Lemonade:", A.varValue)
print("Produce such amount of Fruit Juice:", B.varValue)