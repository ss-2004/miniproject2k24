from ac3 import CSPSolver
def show_head_row():
    print("Edge    | New Domain     | Edges to Reconsider")
    print("--------|----------------|--------------------")

def show_row(edge: tuple, xi: str, new_domain: list, edges_to_reconsider: list):
    print(str(edge) + "  |  " + str(xi) + "=" + str(new_domain) + "  |  " + str(edges_to_reconsider))

def show_solver(arcs: list, domains: dict, constraints: dict, resources: dict, processing_capacity: dict, bandwidth: dict, delay: dict, flow_difference: dict, active_backup: dict, node_activation: dict, vnf_placement: dict, endpoint_mapping: dict):
    solver = CSPSolver(arcs, domains, constraints, resources, processing_capacity, bandwidth, delay, flow_difference, active_backup, node_activation, vnf_placement, endpoint_mapping)
    result = solver.solve(True)

    for step in result:
        continue_input = input()

        if step is None:
            print("Inconsistent! No solution possible.")
        else:
            edge = step[0]

            if edge is None:
                final_domain = step[1]
                print("Result:", final_domain)
            else:
                xi = edge[0]
                new_domain = step[1][xi]
                edges_to_reconsider = step[2]
                show_row(edge, xi, new_domain, edges_to_reconsider)

if __name__ == "__main__":
    show_head_row()

    arcs = [('S', 'v1'), ('S', 'v2'), ('S', 'v3'), ('S', 's1'), ('v1', 'v2'), ('v1', 'm1'), 
            ('v2', 'v3'), ('v2', 'm2'), ('v3', 's2'), ('s1', 's2'), 
            ('s1', 's3'),('s2','m3'),('s3','s4'),('s4','D'),
            ('D','s5'),('D','v5'),('v5','v4'),('v4','v3')]
    
    domains = {
        'S': ['low', 'medium', 'high'],
        'D': ['medium', 'high'],
        'v1': ['low', 'medium'],
        'v2': ['low', 'medium', 'high'],
        'v3': ['medium', 'high'],
        'v4': ['low', 'medium'],
        'v5': ['low', 'medium', 'high'],
        's1': ['medium', 'high'],
        's2': ['low', 'medium'],
        's3': ['low', 'medium', 'high'],
        's4': ['medium', 'high'],
        's5': ['low', 'medium'],
        's6': ['low', 'medium', 'high'],
        's7': ['medium', 'high'],
        'm1': ['low', 'medium'],
        'm2': ['low', 'medium', 'high'],
        'm3': ['medium', 'high'],
    }

    constraints = {
        ('S', 'v1'): lambda node, vnf: node == 'low' and vnf == 'low',
        ('S', 'v2'): lambda node, vnf: node != 'low' or vnf != 'low',
        ('v1', 'v2'): lambda vnf, node: vnf == 'medium' or node == 'medium',
        ('v2', 'v3'): lambda vnf, node: vnf == 'medium' or node == 'medium',
        ('s1', 's2'): lambda node, vnf: node == 'high' and vnf == 'high',
        ('s2', 's3'): lambda node, vnf: node == 'medium' or vnf == 'medium',
        ('s3', 's4'): lambda node, vnf: node == 'medium' or vnf == 'high',
        ('s4', 'D'): lambda vnf, node: vnf == 'low' or node == 'medium',
        ('D', 'v5'): lambda node, vnf: node == 'medium' or vnf == 'medium',
        ('v5', 'v4'): lambda node, vnf: node == 'high' or vnf == 'high',
        ('v4', 'v3'): lambda node, vnf: node == 'medium' or vnf == 'medium'
        # Add more constraints here based on your requirements
    }

    # resources = {'node1': 100, 'node2': 150}
    # processing_capacity = {'vnf1': 50, 'vnf2': 70}
    # bandwidth = {'node1': 200, 'node2': 300}
    # delay = {'vnf1': 10, 'vnf2': 15}
    # flow_difference = {'vnf1': 20, 'vnf2': 25}
    # active_backup = {'vnf1': False, 'vnf2': True}
    # node_activation = {'node1': True, 'node2': False}
    # vnf_placement = {'vnf1': 'node1', 'vnf2': 'node2'}
    # endpoint_mapping = {'endpoint1': 'node1', 'endpoint2': 'node2'}

    resources = {'S': 100, 
                 'v1': 150, 
                 'v2': 100, 
                 'v3': 150, 
                 'v4': 100, 
                 'v5': 150, 
                 's1': 100, 
                 's2': 150, 
                 's3': 100, 
                 's4': 100, 
                 's5': 150,
                 's6': 150,
                 's7': 100,
                 'm1': 150, 
                 'm2': 100, 
                 'm3': 150, 
                 'D': 150}
    
    processing_capacity = {'S': 50, 
                           'v1': 70, 
                           'v2': 50, 
                           'v3': 70, 
                           'v4': 50, 
                           'v5': 70, 
                           's1': 50, 
                           's2': 70, 
                           's3': 50, 
                           's4': 50, 
                           's5': 50,
                           's6': 50,
                           's7': 70, 
                           'm1': 70, 
                           'm2': 50, 
                           'm3': 70, 
                           'D': 70}
    
    bandwidth = {'S': 200, 
                 'v1': 300, 
                 'v2': 200, 
                 'v3': 300, 
                 'v4': 200, 
                 'v5': 300, 
                 's1': 200, 
                 's2': 300, 
                 's3': 200, 
                 's4': 200, 
                 's5': 200,
                 's6': 200,
                 's7': 300, 
                 'm1': 300, 
                 'm2': 200, 
                 'm3': 300, 
                 'D': 300}

    delay = {'S': 10, 
             'v1': 15, 
             'v2': 10, 
             'v3': 15, 
             'v4': 10, 
             'v5': 15, 
             's1': 10, 
             's2': 15, 
             's3': 10, 
             's4': 10, 
             's5': 10,
             's6': 10,
             's7': 15,
             'm1': 15, 
             'm2': 10, 
             'm3': 15, 
             'D': 15}
    
    flow_difference = {'S': 20, 
                       'v1': 25, 
                       'v2': 20, 
                       'v3': 25, 
                       'v4': 20, 
                       'v5': 25, 
                       's1': 20, 
                       's2': 25, 
                       's3': 20, 
                       's4': 20, 
                       's5': 20,
                       's6': 10,
                       's7': 20, 
                       'm1': 25, 
                       'm2': 20, 
                       'm3': 25, 
                       'D': 25}
    
    active_backup = {'S': False, 
                     'v1': False, 
                     'v2': False, 
                     'v3': False, 
                     'v4': False, 
                     'v5': False, 
                     's1': False, 
                     's2': False, 
                     's3': False, 
                     's4': False, 
                     's5': False, 
                     's6': False,
                     's7': False,
                     'm1': False, 
                     'm2': False, 
                     'm3': False, 
                     'D': False}
    
    node_activation = {'S': True, 
                       'v1': True, 
                       'v2': True, 
                       'v3': True, 
                       'v4': True, 
                       'v5': True, 
                       's1': True, 
                       's2': False, 
                       's3': False, 
                       's4': True, 
                       's5': False, 
                       's6': True,
                       's7': True,
                       'm1': True, 
                       'm2': True, 
                       'm3': True, 
                       'D': True}
    
    vnf_placement = {'s1': 'S', 's1': 'v1', 
                     's3': 'm1', 's3': 'm2', 
                     's4': 'v2', 
                     's5': 'm3', 
                     'm2': 'm2', 
                     's6': 'v3', 
                     's7': 'v4', 's7': 'v5', 's7': 'D', 
                     'm1': 'v1', 'm1': 'v2', 
                     'm2': 'v3', 
                     's4': 'v4', 
                     's4': 'v5'
                    }
    endpoint_mapping = {'endpoint1': 'S', 'endpoint2': 'D'}


    # resources = {'S': 100, 'v1': 150, 'v2': 200, 'v3': 300, 's1': 100, 'm1': 70, 'm2': 50,
    #          's2': 150, 's3': 200, 'm3': 70, 's4': 100, 'D': 150, 's5': 50, 'v5': 200, 'v4': 300, 'v3': 100}

    # # Processing capacity for VNFs
    # processing_capacity = {'vnf1': 50, 'vnf2': 70}

    # # Bandwidth for nodes
    # bandwidth = {'S': 200, 'v1': 300, 'v2': 200, 'v3': 300, 's1': 200, 'm1': 150, 'm2': 100,
    #             's2': 200, 's3': 300, 'm3': 150, 's4': 200, 'D': 300, 's5': 100, 'v5': 200, 'v4': 300, 'v3': 200}

    # # Delay for VNFs
    # delay = {'vnf1': 10, 'vnf2': 15}

    # # Flow difference for VNFs
    # flow_difference = {'vnf1': 20, 'vnf2': 25}

    # # Active backup status for VNFs
    # active_backup = {'vnf1': False, 'vnf2': True}

    # # Node activation status
    # node_activation = {'S': True, 'v1': False, 'v2': True, 'v3': False, 's1': True, 'm1': False, 'm2': True,
    #                 's2': False, 's3': True, 'm3': False, 's4': True, 'D': False, 's5': True, 'v5': False, 'v4': True, 'v3': False}

    # # VNF placement
    # vnf_placement = {'vnf1': 'S', 'vnf2': 'v1'}

    # # Endpoint mapping
    # endpoint_mapping = {'endpoint1': 'S', 'endpoint2': 'v1'}

    show_solver(arcs, domains, constraints, resources, processing_capacity, bandwidth, delay, flow_difference, active_backup, node_activation, vnf_placement, endpoint_mapping)