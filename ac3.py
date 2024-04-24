import queue

class CSPSolver:
    worklist = queue.Queue()  # a queue of arcs (this can be a queue or set in AC-3)

    def __init__(self, arcs: list, domains: dict, constraints: dict, resources: dict, processing_capacity: dict, bandwidth: dict, delay: dict, flow_difference: dict, active_backup: dict, node_activation: dict, vnf_placement: dict, endpoint_mapping: dict):
        self.arcs = arcs
        self.domains = domains
        self.constraints = constraints
        self.resources = resources
        self.processing_capacity = processing_capacity
        self.bandwidth = bandwidth
        self.delay = delay
        self.flow_difference = flow_difference
        self.active_backup = active_backup
        self.node_activation = node_activation
        self.vnf_placement = vnf_placement
        self.endpoint_mapping = endpoint_mapping

    def solve(self, generate=False) -> dict:
        result = self.solve_helper()

        if generate:
            return result
        else:
            return_value = []

            for step in result:
                if step is None:
                    return step  # inconsistency found
                else:
                    return_value = step

            return return_value[1]  # return only the final domain

    def solve_helper(self) -> dict:
        [self.worklist.put(arc) for arc in self.arcs]

        while not self.worklist.empty():
            (xi, xj) = self.worklist.get()

            if self.revise(xi, xj):
                if len(self.domains[xi]) == 0:
                    yield None
                    break

                neighbors = [neighbor for neighbor in self.arcs if neighbor[0] == xj]
                [self.worklist.put(neighbor) for neighbor in neighbors]

                yield ((xi, xj), self.domains, neighbors)
            else:
                yield ((xi, xj), self.domains, None)

        yield (None, self.domains, None)

    def revise(self, xi: object, xj: object) -> bool:
        revised = False
        print(f"Revising domains for ({xi}, {xj})")

        xi_domain = self.domains[xi]
        xj_domain = self.domains[xj]

        constraints = [constraint for constraint in self.constraints if constraint[0] == xi and constraint[1] == xj]

        for x in xi_domain[:]:
            satisfies = False

            for y in xj_domain:
                for constraint in constraints:
                    check_function = self.constraints[constraint]

                    if check_function(x, y):
                        satisfies = True

            if not satisfies:
                print(f"Removing value {x} from domain {xi}")
                xi_domain.remove(x)
                revised = True
        print(f"Domains after revision for ({xi}, {xj}): {self.domains}")

        return revised
