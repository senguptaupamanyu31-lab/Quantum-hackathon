# tests/test_parallel.py

import matplotlib
matplotlib.use('TkAgg')  # Use interactive backend for displaying plots

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

from compiler.mapper import RegisterMap
from compiler.executor import Executor
from isa.instruction_set import parse_instruction, validate_instruction
from simulation.noise_model import create_noise_model


def build_instructions(program):
    instructions = []
    for line in program:
        inst = parse_instruction(line)
        validate_instruction(inst)
        instructions.append(inst)
    return instructions


def main():
    # -----------------------------
    # PARALLELIZABLE PROGRAM
    # -----------------------------
    program = [
    "XOR x0 x1 x2",
    "AND x3 x4 x5",
    "XOR x1 x2 x3",
    "AND x4 x5 x0",
    "XOR x2 x3 x4",
    "MEASURE x0"
]

    instructions = build_instructions(program)

    rm = RegisterMap()

    # -----------------------------
    # SEQUENTIAL EXECUTION
    # -----------------------------
    qc_seq = QuantumCircuit(rm.total_qubits(), 2)

    # inputs
    qc_seq.x(rm.get_reg_qubits("x1")[0])
    qc_seq.x(rm.get_reg_qubits("x2")[1])
    qc_seq.x(rm.get_reg_qubits("x4")[0])
    qc_seq.x(rm.get_reg_qubits("x5")[1])

    # manual sequential execution (NO scheduler)
    from alu.xor import apply_xor
    from alu.and_gate import apply_and

    apply_xor(qc_seq, rm, "x0", "x1", "x2")
    apply_and(qc_seq, rm, "x3", "x4", "x5")

    qc_seq.measure(rm.get_reg_qubits("x0"), [0, 1])

    # -----------------------------
    # SCHEDULED EXECUTION
    # -----------------------------
    qc_sched = QuantumCircuit(rm.total_qubits(), 2)

    # same inputs
    qc_sched.x(rm.get_reg_qubits("x1")[0])
    qc_sched.x(rm.get_reg_qubits("x2")[1])
    qc_sched.x(rm.get_reg_qubits("x4")[0])
    qc_sched.x(rm.get_reg_qubits("x5")[1])

    executor = Executor(qc_sched, rm)
    executor.execute(instructions)

    # -----------------------------
    # DEPTH COMPARISON
    # -----------------------------
    print("\nCircuit Depth Comparison:")
    print(f"Sequential Depth: {qc_seq.depth()}")
    print(f"Scheduled Depth: {qc_sched.depth()}")

    # -----------------------------
    # NOISE COMPARISON
    # -----------------------------
    sim = Aer.get_backend("qasm_simulator")
    noise_model = create_noise_model()

    seq_counts = sim.run(qc_seq, shots=1024, noise_model=noise_model).result().get_counts()
    sched_counts = sim.run(qc_sched, shots=1024, noise_model=noise_model).result().get_counts()

    print("\nSequential Output (Noisy):", seq_counts)
    print("Scheduled Output (Noisy):", sched_counts)

    # -----------------------------
    # PLOT
    # -----------------------------
    plot_histogram([seq_counts, sched_counts], legend=["Sequential", "Scheduled"])
    plt.savefig("parallel_comparison.png")
    plt.show(block=True)


if __name__ == "__main__":
    main()