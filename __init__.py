# qrisc2/alu/and_gate.py

def apply_and(qc, rm, rd, rs1, rs2):
    """
    rd = rs1 AND rs2 (bitwise)
    """

    rd_qubits = rm.get_reg_qubits(rd)
    rs1_qubits = rm.get_reg_qubits(rs1)
    rs2_qubits = rm.get_reg_qubits(rs2)

    if not (len(rd_qubits) == len(rs1_qubits) == len(rs2_qubits)):
        raise ValueError('Register qubit widths must match for AND operation')

    for i in range(len(rd_qubits)):
        if rs1_qubits[i] == rs2_qubits[i]:
            # rs1 and rs2 are the same register: AND(x, x) == x
            qc.cx(rs1_qubits[i], rd_qubits[i])
        else:
            qc.ccx(rs1_qubits[i], rs2_qubits[i], rd_qubits[i])
