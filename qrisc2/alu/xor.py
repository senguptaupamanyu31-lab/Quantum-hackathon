# qrisc2/alu/xor.py

def apply_xor(qc, rm, rd, rs1, rs2):
    """
    rd = rs1 XOR rs2 (alias-safe)
    """

    rd_q = rm.get_reg_qubits(rd)
    a_q = rm.get_reg_qubits(rs1)
    b_q = rm.get_reg_qubits(rs2)

    for i in range(len(rd_q)):

        # Apply only if different qubits
        if a_q[i] != rd_q[i]:
            qc.cx(a_q[i], rd_q[i])

        if b_q[i] != rd_q[i]:
            qc.cx(b_q[i], rd_q[i])