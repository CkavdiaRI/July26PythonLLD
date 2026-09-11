from models.gate import Gate

class GateRepository:
    def __init__(self):
        self.gates = dict[int, Gate] = {} # Dictionary to store gates by their IDs

    def find_gate_by_id(self, gate_id: int) -> Gate:
        return self.gates.get(gate_id)