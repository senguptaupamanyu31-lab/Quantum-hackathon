# qrisc2/scheduler/scheduler.py

class Scheduler:
    def __init__(self, rm):
        self.rm = rm

    def get_qubits_used(self, inst):
        """Return all qubits used by an instruction"""

        if inst.opcode == "MEASURE":
            return set(self.rm.get_reg_qubits(inst.rd))

        qubits = set()

        if inst.rd:
            qubits.update(self.rm.get_reg_qubits(inst.rd))
        if inst.rs1:
            qubits.update(self.rm.get_reg_qubits(inst.rs1))
        if inst.rs2:
            qubits.update(self.rm.get_reg_qubits(inst.rs2))

        return qubits

    def schedule(self, instructions):
        """
        Simple scheduler:
        Groups instructions into layers with no qubit conflicts
        """

        layers = []
        current_layer = []
        used_qubits = set()

        for inst in instructions:
            inst_qubits = self.get_qubits_used(inst)

            # conflict check
            if used_qubits & inst_qubits:
                # start new layer
                layers.append(current_layer)
                current_layer = [inst]
                used_qubits = set(inst_qubits)
            else:
                current_layer.append(inst)
                used_qubits.update(inst_qubits)

        if current_layer:
            layers.append(current_layer)

        return layers