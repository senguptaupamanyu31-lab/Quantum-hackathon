# tests/test_add.py

from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

from compiler.mapper import RegisterMap
from alu.add import apply_add


def main():
    rm = RegisterMap()

    qc = QuantumCircuit(rm.total_qubits(), 2)

    # -----------------------------
    # INPUT
    # x2 = 01
    # x3 = 11
    # -----------------------------

    qc.x(rm.get_reg_qubits("x2")[0])

    qc.x(rm.get_reg_qubits("x3")[0])
    qc.x(rm.get_reg_qubits("x3")[1])

    # -----------------------------
    # APPLY ADD
    # x1 = x2 + x3
    # -----------------------------
    apply_add(qc, rm, "x1", "x2", "x3")

    # -----------------------------
    # MEASURE x1
    # -----------------------------
    x1_qubits = rm.get_reg_qubits("x1")
    qc.measure(x1_qubits, [0, 1])

    # -----------------------------
    # SIMULATION
    # -----------------------------
    sim = Aer.get_backend("qasm_simulator")
    result = sim.run(qc, shots=1024).result()

    counts = result.get_counts()

    print("\nMeasurement Results:")
    print(counts)

    plot_histogram(counts)
    plt.savefig("add_result.png")
    plt.show(block=True)


if __name__ == "__main__":
    main()