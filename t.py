from ac3 import CSPSolver

# Adds a interactive layer above csp_ac3.py to visually show the ac-3 algorithm
# Go to next step in the ac-3 algorithm by hitting the enter key


# Show the heading row
def show_head_row():
    print("Edge    | New Domain     | Edges to Reconsider")
    print("--------|----------------|--------------------")


# Display a single row of ac-3
def show_row(edge: tuple, xi: str, new_domain: list, edges_to_reconsider: list):
    print(str(edge) + "  |  " + str(xi) + "=" + str(new_domain) + "  |  " + str(edges_to_reconsider))


# solve the given CSP and print the results from the generated solve funcion
def show_solver(arcs: list, domains: dict, constraints: dict):
    solver = CSPSolver(arcs, domains, constraints)
    result = solver.solve(True)  # True indicates that we are using the method as a generator

    for step in result:
        continue_input = input()  # continue with the function generator only on user input (ex: enter key)

        if step == None:
            # found an inconsistency
            print("Inconsistent!. No solution possible.")
        else:
            edge = step[0]

            if edge == None:
                # reached the final result
                final_domain = step[1]
                print("Result:", final_domain)
            else:
                xi = edge[0]
                new_domain = step[1][xi]
                edges_to_reconsider = step[2]
                show_row(edge, xi, new_domain, edges_to_reconsider)


if __name__ == "__main__":
    show_head_row()

    # arcs, domains, and constraints
    arcs = [('s', 'v1'), ('v1', 'v2'), ('v2', 'v3'), ('v3', 'd'),
            ('d', 'v3'), ('v3', 'v2'), ('v2', 'v1'), ('v1', 's'),
            ('s', 's1'), ('s', 's2'), 
            ('s1', 's'), ('s2', 's'),
            ('s3', 'd'), ('s4', 'd'),
            ('d', 's3'), ('d', 's4'),
            ('s2', 's3'), ('s3', 's2'),
            ('s1', 's4'), ('s4', 's1')
    ]

    # domains = {
    #     's': [2, 3, 4, 5, 6, 7],
    #     'd': [4, 5, 6, 7, 8, 9],
    #     'v1': [1, 2, 3, 4, 5],
    #     'v2': [1, 2, 3, 4, 5],
    #     'v3': [1, 2, 3, 4, 5],
    #     's1': [1, 2, 3, 4, 5],
    #     's2': [1, 2, 3, 4, 5],
    #     's3': [1, 2, 3, 4, 5],
    #     's4': [1, 2, 3, 4, 5]
    # }

    # domains = {
    #     's': [1, 2, 3, 4, 5],
    #     'd': [2, 3, 4, 5],
    #     'v1': [1, 2, 3],
    #     'v2': [1, 2, 3],
    #     'v3': [1, 2, 3],
    #     's1': [1, 2, 3],
    #     's2': [1, 2, 3],
    #     's3': [1, 2, 3],
    #     's4': [1, 2, 3]
    # }

    # domains = {
    #     's': [1, 2, 3],
    #     'd': [2, 3, 4],
    #     'v1': [1, 2],
    #     'v2': [1, 2],
    #     'v3': [2, 3],
    #     's1': [1, 2],
    #     's2': [1, 2],
    #     's3': [2, 3],
    #     's4': [2, 3]
    # }

    # domains = {
    #     's': [1, 2, 3],
    #     'd': [2, 3, 4],
    #     'v1': [2],
    #     'v2': [2],
    #     'v3': [2, 3],
    #     's1': [1, 2],
    #     's2': [1, 2],
    #     's3': [2, 3],
    #     's4': [2, 3]
    # }

    domains = {
        's': [1, 2, 3, 4, 5, 6, 7],
        'd': [2, 3, 4],
        'v1': [4, 5, 6, 7, 8],
        'v2': [1, 2, 3, 4],
        'v3': [2, 3],
        's1': [4, 5],
        's2': [1, 2],
        's3': [2, 3],
        's4': [6, 7]
    }

    # constraints:
    # b = 2*a
    # a = c
    # b >= c - 2
    # b <= c + 2
    constraints = {
        ('s', 'v1'): lambda s, v1: s * 2 == v1,
        ('v1', 's'): lambda v1, s: v1 == 2 * s,
        ('v1', 'v2'): lambda v1, v2: v1 == v2,
        ('v2', 'v1'): lambda v2, v1: v2 == v1,
        
        ('v2', 'v3'): lambda v2, v3: v2 >= v3 - 2,
        ('v2', 'v3'): lambda v2, v3: v2 <= v3 + 2,
        ('v3', 'v2'): lambda v3, v2: v2 >= v3 - 2,
        ('v3', 'v2'): lambda v3, v2: v2 <= v3 + 2,
        
        ('v3', 'd'): lambda v3, d: v3 >= d - 1,
        # ('v2', 'v3'): lambda v2, v3: v2 <= v3 + 2,
        ('d', 'v3'): lambda d, v3: v3 >= d - 1,
        # ('v3', 'v2'): lambda v3, v2: v2 <= v3 + 2,
    }

    show_solver(arcs, domains, constraints)
