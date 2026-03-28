# tests/test_program.py

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import os

from simulation.noise_model import create_noise_model
from compiler.mapper import RegisterMap
from compiler.executor import Executor
from isa.instruction_set import parse_instruction, validate_instruction


def main():
    # -----------------------------
    # PROGRAM (your "assembly")
    # -----------------------------
    program = [
    "XOR x0 x1 x2",
    "AND x3 x2 x1",
    "MEASURE x0"
]

    # -----------------------------
    # PARSE + VALIDATE
    # -----------------------------
    instructions = []
    for line in program:
        inst = parse_instruction(line)
        validate_instruction(inst)
        instructions.append(inst)

    # -----------------------------
    # SETUP
    # -----------------------------
    rm = RegisterMap()

    # IMPORTANT: create separate circuits for fair comparison
    qc_ideal = QuantumCircuit(rm.total_qubits(), 2)
    qc_noisy = QuantumCircuit(rm.total_qubits(), 2)

    # -----------------------------
    # INITIAL INPUTS (same for both)
    # -----------------------------
    for qc in [qc_ideal, qc_noisy]:
        qc.x(rm.get_reg_qubits("x2")[0])

        qc.x(rm.get_reg_qubits("x3")[0])
        qc.x(rm.get_reg_qubits("x3")[1])

    # -----------------------------
    # EXECUTE PROGRAM (both circuits)
    # -----------------------------
    Executor(qc_ideal, rm).execute(instructions)
    Executor(qc_noisy, rm).execute(instructions)

    # -----------------------------
    # SIMULATION
    # -----------------------------
    sim = Aer.get_backend("qasm_simulator")

    # -------- IDEAL --------
    ideal_result = sim.run(qc_ideal, shots=1024).result()
    ideal_counts = ideal_result.get_counts()

    # -------- NOISY --------
    noise_model = create_noise_model()
    noisy_result = sim.run(qc_noisy, shots=1024, noise_model=noise_model).result()
    noisy_counts = noisy_result.get_counts()

    # -----------------------------
    # OUTPUT
    # -----------------------------
    print("\nIdeal Output:")
    print(ideal_counts)

    print("\nNoisy Output:")
    print(noisy_counts)

    # -----------------------------
    # VISUALIZATION
    # -----------------------------
    plot_histogram(
        [ideal_counts, noisy_counts],
        legend=['Ideal', 'Noisy']
    )

    out_path = "noise_comparison.png"
    plt.savefig(out_path)
    print(f"\nSaved comparison to: {os.path.abspath(out_path)}")

    try:
        plt.show(block=True)
    except Exception as e:
        print(f"Plot display skipped: {e}")


if __name__ == "__main__":
    main()