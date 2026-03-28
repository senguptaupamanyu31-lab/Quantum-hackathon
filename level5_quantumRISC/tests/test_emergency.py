# tests/test_emergency.py

import matplotlib
matplotlib.use('TkAgg')  # interactive backend for plot windows

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

from compiler.mapper import RegisterMap
from compiler.executor import Executor
from isa.instruction_set import parse_instruction, validate_instruction
from simulation.noise_model import create_noise_model


def load_program():
    program = [
        "XOR x0 x1 x1",   # Emergency
        "AND x5 x2 x2",   # Fire
        "XOR x0 x0 x5",
        "AND x6 x3 x3",   # Gas
        "XOR x0 x0 x6",
        "AND x7 x4 x4",   # Intrusion
        "XOR x0 x0 x7",
        "MEASURE x0"
    ]

    instructions = []
    for line in program:
        inst = parse_instruction(line)
        validate_instruction(inst)
        instructions.append(inst)

    return instructions


def run_case(case_name, active_regs):
    print(f"\n=== {case_name} ===")

    rm = RegisterMap()
    qc = QuantumCircuit(rm.total_qubits(), 2)

    # Activate signals
    for reg in active_regs:
        qc.x(rm.get_reg_qubits(reg)[0])

    instructions = load_program()
    executor = Executor(qc, rm)
    executor.execute(instructions)

    sim = Aer.get_backend("qasm_simulator")

    # Ideal
    ideal = sim.run(qc, shots=1024).result().get_counts()

    # Noisy
    noise_model = create_noise_model()
    noisy = sim.run(qc, shots=1024, noise_model=noise_model).result().get_counts()

    print("Ideal:", ideal)
    print("Noisy:", noisy)

    plot_histogram([ideal, noisy], legend=["Ideal", "Noisy"])
    filename = f"{case_name.replace(' ', '_')}.png"
    plt.savefig(filename)
    print(f"Saved: {os.path.abspath(filename)}")

    try:
        plt.show()
    except Exception:
        pass


def main():
    # -----------------------------
    # TEST CASES
    # -----------------------------

    # Case 1: Emergency only
    run_case("Emergency Only", ["x1"])

    # Case 2: Fire + Gas → Fire should dominate
    run_case("Fire and Gas", ["x2", "x3"])

    # Case 3: Gas + Intrusion → Gas dominates
    run_case("Gas and Intrusion", ["x3", "x4"])

    # Case 4: All active → Emergency dominates
    run_case("All Signals Active", ["x1", "x2", "x3", "x4"])


if __name__ == "__main__":
    main()