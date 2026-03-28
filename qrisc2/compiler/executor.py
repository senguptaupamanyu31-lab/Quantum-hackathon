# qrisc2/compiler/executor.py

from alu.xor import apply_xor
from alu.and_gate import apply_and
from alu.add import apply_add


class Executor:
    def __init__(self, qc, rm):
        self.qc = qc
        self.rm = rm

    def execute(self, instructions):
        for inst in instructions:
            op = inst.opcode

            if op == "XOR":
                apply_xor(self.qc, self.rm, inst.rd, inst.rs1, inst.rs2)

            elif op == "AND":
                apply_and(self.qc, self.rm, inst.rd, inst.rs1, inst.rs2)

            elif op == "ADD":
                apply_add(self.qc, self.rm, inst.rd, inst.rs1, inst.rs2)

            elif op == "MEASURE":
                qubits = self.rm.get_reg_qubits(inst.rd)
                self.qc.measure(qubits, list(range(len(qubits))))

            else:
                raise ValueError(f"Unknown instruction: {op}")
            