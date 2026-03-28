# qrisc2/simulation/noise_model.py

from qiskit_aer.noise import NoiseModel, depolarizing_error


def create_noise_model():
    noise_model = NoiseModel()

    # Single-qubit error (for X, CX decomposition, etc.)
    error_1 = depolarizing_error(0.01, 1)   # 1% error

    # Two-qubit error (for CX, CCX)
    error_2 = depolarizing_error(0.05, 2)   # 5% error

    # Apply to gates
    noise_model.add_all_qubit_quantum_error(error_1, ['x'])
    noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

    return noise_model