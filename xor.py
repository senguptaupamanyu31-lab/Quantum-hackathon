# qrisc2/alu/add.py

def apply_add(qc, rm, rd, rs1, rs2):
    """
    rd = rs1 + rs2 (2-bit ripple carry adder)
    """

    rd_q = rm.get_reg_qubits(rd)
    a_q = rm.get_reg_qubits(rs1)
    b_q = rm.get_reg_qubits(rs2)
    anc = rm.get_ancilla()

    c = anc[0]  # carry qubit (must start at 0)

    # --- LSB (bit 0) ---
    qc.cx(a_q[0], rd_q[0])
    qc.cx(b_q[0], rd_q[0])
    qc.ccx(a_q[0], b_q[0], c)

    # --- MSB (bit 1) ---
    qc.cx(a_q[1], rd_q[1])
    qc.cx(b_q[1], rd_q[1])

    # add carry to MSB
    qc.cx(c, rd_q[1])

    # optional carry-out (not used further)
    qc.ccx(a_q[1], b_q[1], anc[1])