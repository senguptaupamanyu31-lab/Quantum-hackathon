# qrisc2/compiler/mapper.py

class RegisterMap:
    def __init__(self):
        self.registers = ["x0", "x1", "x2", "x3", "x4", "x5", "x6", "x7"]
        self.qubits_per_reg = 2
        self.ancilla_qubits = 2

        self.mapping = {}
        self.ancilla = []

        self._allocate()

    def _allocate(self):
        q = 0

        # Assign qubits to registers
        for reg in self.registers:
            self.mapping[reg] = list(range(q, q + self.qubits_per_reg))
            q += self.qubits_per_reg

        # Assign ancilla
        self.ancilla = list(range(q, q + self.ancilla_qubits))

    def get_reg_qubits(self, reg):
        return self.mapping[reg]

    def get_ancilla(self):
        return self.ancilla

    def total_qubits(self):
        return sum(len(v) for v in self.mapping.values()) + len(self.ancilla)

    def __repr__(self):
        return f"Registers: {self.mapping}, Ancilla: {self.ancilla}"