# tests/test_xor.py
from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
from compiler.mapper import RegisterMap
from alu.xor import apply_xor

def main():
    rm = RegisterMap()

    # 2 classical bits to store x1 result
    qc = QuantumCircuit(rm.total_qubits(), 2)
    # x2 = 01
    qc.x(rm.get_reg_qubits("x2")[0])

    # x3 = 11
    qc.x(rm.get_reg_qubits("x3")[0])
    qc.x(rm.get_reg_qubits("x3")[1])

    apply_xor(qc, rm, "x1", "x2", "x3")

    x1_qubits = rm.get_reg_qubits("x1")
    qc.measure(x1_qubits, [0, 1])
    # SIMULATION
    sim = Aer.get_backend("qasm_simulator")
    result = sim.run(qc, shots=1024).result()

    counts = result.get_counts()

    # OUTPUT
    print("\nMeasurement Results:")
    print(counts)

    # VISUALIZATION
    plot_histogram(counts)
    plt.savefig("xor_result.png")  
    plt.show(block=True)            

if __name__ == "__main__":
    main()