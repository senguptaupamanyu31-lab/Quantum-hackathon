from compiler.mapper import RegisterMap 

rm = RegisterMap()

print(rm)
print("x1 →", rm.get_reg_qubits("x1"))
print("Ancilla →", rm.get_ancilla())
print("Total qubits →", rm.total_qubits())