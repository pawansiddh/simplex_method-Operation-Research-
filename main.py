import pulp


num_variables = int(input("Enter the number of variables: "))
num_constraints = int(input("Enter the number of constraints: "))


lp_problem = pulp.LpProblem("Maximize_Profit", pulp.LpMaximize)


variables = [pulp.LpVariable(f"x{i+1}", lowBound=0)
             for i in range(num_variables)]


print("Enter the coefficients of the objective function:")
c = [float(input(f"Enter coefficient for x{i+1}: "))
     for i in range(num_variables)]


lp_problem += pulp.lpSum(c[i] * variables[i] for i in range(num_variables))


A = []
b = []


for i in range(num_constraints):
    print(f"Enter coefficients for constraint {i+1}:")
    constraint_coeffs = [
        float(input(f"  Enter coefficient for x{i+1}: ")) for i in range(num_variables)]

    inequality = input(
        f"Enter the inequality sign (<= or >=) for constraint {i+1}: ")
    constraint_value = float(
        input(f"Enter the constant value for constraint {i+1}: "))

    if inequality == "<=":
        A.append(pulp.lpSum(constraint_coeffs[i] * variables[i]
                 for i in range(num_variables)) <= constraint_value)
    elif inequality == ">=":
        A.append(pulp.lpSum(constraint_coeffs[i] * variables[i]
                 for i in range(num_variables)) >= constraint_value)
    else:
        print("Invalid inequality sign. Please use <= or >=.")
        exit(1)


for constraint in A:
    lp_problem += constraint


lp_problem.solve()


if pulp.LpStatus[lp_problem.status] == "Optimal":
    print("Optimal solution found:")
    for i, variable in enumerate(variables):
        print(f"{variable.name} = {variable.varValue}")
    print(f"Optimal value = {pulp.value(lp_problem.objective)}")
else:
    print("Optimization failed.")

'''Here we take a example of simplex method
   Zmax=X1+3X2;
   constraint1:3X1+6X2 <= 8;
   constraint2:5X1+2X2 <=10
   where X1 and X2 are >=0'''
