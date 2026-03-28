# qrisc2/compiler/executor.py

from alu.xor import apply_xor
from alu.and_gate import apply_and
from alu.add import apply_add
from scheduler.scheduler import Scheduler


class Executor:
    def __init__(self, qc, rm):
        self.qc = qc
        self.rm = rm
        self.scheduler = Scheduler(rm)

    def execute(self, instructions):
        # -----------------------------
        # SCHEDULE INSTRUCTIONS
        # -----------------------------
        layers = self.scheduler.schedule(instructions)

        print("\nScheduled Layers:")
        for i, layer in enumerate(layers):
            print(f"Layer {i}: {[inst.opcode for inst in layer]}")

        # -----------------------------
        # EXECUTE LAYER BY LAYER
        # -----------------------------
        for layer in layers:
            for inst in layer:
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