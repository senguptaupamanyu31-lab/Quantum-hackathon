# Quantum-hackathon
This repository contains projects made during the Q-Hack hackathon. It was a level based hackathon with different problem statements for each level.
📌 Level 1: Design of a 4-bit Ripple Carry Adder using Quantum Circuits
🧠 Objective
The goal of Level 1 was to translate a classical digital circuit (4-bit ripple carry adder) into a reversible quantum circuit using quantum gates.

Unlike classical circuits, quantum circuits must:

Preserve information (reversibility)
Avoid overwriting inputs
Use additional qubits (ancilla) for intermediate computations
⚙️ What We Built
We implemented a 4-bit Ripple Carry Adder using:

CNOT (CX) gates → for XOR operations
Toffoli (CCX) gates → for AND (carry generation)
Each bit addition is handled using a quantum full adder block, and carry propagates from one stage to the next — forming a ripple carry structure.

🔢 Qubit Mapping
Register	Qubits	Description
A	q0–q3	First 4-bit input
B	q4–q7	Second 4-bit input
Sum	q8–q11	Output sum
Carry	q12–q16	Carry propagation
Temp	q17–q20	Ancilla qubits for intermediate XOR
🔁 Working Principle
Each full adder computes:

Sum: S = A ⊕ B ⊕ Cin

Carry: Cout = (A · B) ⊕ (Cin · (A ⊕ B))

Steps:
Compute intermediate XOR (A ⊕ B) using CNOT gates
Compute sum using XOR with carry-in
Generate carry using Toffoli gates
Propagate carry to the next stage
Uncompute temporary qubits to maintain reversibility
🧪 Example
Input:
A = 1011 (11)
B = 0110 (6)
Expected Output:
Sum = 10001 (17)
🛠️ Tools & Technologies
Qiskit – Quantum circuit design and simulation
Qiskit Aer Simulator – Local simulation of quantum circuits
Google Colab – Development environment
📊 Results
Successfully designed a reversible quantum ripple carry adder
Verified circuit behavior using simulation
Demonstrated carry propagation across multiple qubits
💡 Key Learnings
Difference between classical and quantum circuit design
Importance of reversibility in quantum computing
Use of ancilla qubits for intermediate computations
Implementation of arithmetic logic using quantum gates
👨‍💻 Author
Developed as part of Q-Hack Hackathon Level 1
⭐ Note
This project focuses on conceptual understanding and implementation of reversible arithmetic circuits, which form the foundation for more advanced quantum algorithms and hardware design.

📌 Level 2: Smart City Emergency Priority System using Multiplexer (MUX)
🧠 Problem Statement
In a smart city environment, multiple sensors continuously monitor critical emergency conditions such as:

Fire Detection
Gas Leakage
Intrusion Detection
Medical Emergency
Due to limited communication bandwidth, only one signal can be transmitted at a time to the central control unit.

The objective was to design a system that:

Selects only one signal
Prioritizes more critical emergencies over others
⚙️ Approach
We implemented the solution in two ways:

1️⃣ Classical Priority MUX
A priority-based combinational logic was implemented where:

Priority	Signal
Highest	Fire (s3)
High	Gas (s2)
Medium	Intrusion (s1)
Low	Medical (s0)
Logic:
If Fire → select Fire  
Else if Gas → select Gas  
Else if Intrusion → select Intrusion  
Else if Medical → select Medical  
Else → No signal
This ensures that only the highest priority active signal is transmitted.

⚛️ Quantum Implementation
To extend the idea into quantum computing, we designed a reversible priority MUX circuit using quantum gates.

🔢 Qubit Mapping
Qubit	Signal
q0	Medical (s0)
q1	Intrusion (s1)
q2	Gas (s2)
q3	Fire (s3)
q4	Output
⚙️ Circuit Design Logic
The circuit uses:

CNOT (CX) → for conditional activation
Toffoli (CCX) → for controlled AND operations
Multi-controlled gates (MCX) → for enforcing priority conditions
🔁 Priority Implementation
The logic is encoded as follows:

Fire (Highest Priority)

Directly sets output if active
CX(q3 → q4)
Gas (Second Priority)

Activated only if Fire = 0
Uses inverted Fire + Toffoli gate
Intrusion (Third Priority)

Activated only if Fire = 0 AND Gas = 0
Uses multi-controlled gate
Medical (Lowest Priority)

Activated only if all higher signals are 0
Uses 4-controlled gate
🧪 Superposition Testing
To demonstrate quantum behavior:

All inputs were placed in superposition using Hadamard gates
This allows:

Simultaneous evaluation of all 16 input combinations
Verification of correct priority selection probabilistically
📊 Results
Histogram shows distribution of output states (0 or 1)

Expected behavior:

Output = 1 for 15 cases (any emergency present)
Output = 0 only when all inputs are 0
Observations:
Output closely matches expected probability distribution
Accuracy calculated based on deviation from ideal results
🔍 Verification
Two validation methods were used:

✔ Deterministic Testing
All 16 input combinations tested individually
Verified correct priority selection
✔ Probabilistic Testing
Superposition-based simulation
Compared expected vs observed output distribution
💡 Key Learnings
Implementation of priority logic using reversible quantum gates
Use of multi-controlled gates (MCX) for complex conditions
Understanding of quantum parallelism via superposition
Bridging classical digital logic with quantum circuit design
🚀 Future Improvements
Optimize circuit depth and gate count
Implement noise-aware execution on real quantum hardware
Extend to multi-output emergency classification
Integrate with real-time IoT sensor simulation
🎯 Conclusion
This project demonstrates how a classical priority-based multiplexer can be translated into a quantum circuit, preserving logical correctness while leveraging quantum principles like superposition and reversibility.

It highlights the potential of quantum computing in intelligent decision-making systems for smart city infrastructure.

📌 Level 3: Quantum State Analysis using QuTiP
🧠 Problem Statement
Two students prepare the following qubit states:

ψ₁ = (|0⟩ + |1⟩) / √2
ψ₂ = (|0⟩ − |1⟩) / √2

They claim:

"Both states look similar on the Bloch Sphere!"
Your task is to verify, visualize, and explain this claim using QuTiP.

🧠 Overview
This project analyzes two quantum states:

ψ₁ = (|0⟩ + |1⟩) / √2
ψ₂ = (|0⟩ − |1⟩) / √2

The goal is to determine whether these states are similar or different using:

Mathematical verification
Bloch sphere representation
Physical interpretation
The implementation is done using QuTiP in Google Colab.

🎯 Objectives
Represent quantum states programmatically
Compute inner product to check similarity
Extract Bloch sphere coordinates
Visualize states on the Bloch sphere
Provide physical interpretation
⚙️ Technologies Used
Python
NumPy
QuTiP (Quantum Toolbox in Python)
Google Colab
📂 Code Explanation
🔹 1. Define Basis States
zero = basis(2, 0)
one = basis(2, 1)
Creates standard quantum states:

(|0\rangle = [1, 0]^T)
(|1\rangle = [0, 1]^T)
🔹 2. Define Given States
psi1 = (zero + one).unit()
psi2 = (zero - one).unit()
Creates normalized superposition states:

( |\psi_1\rangle = |+\rangle )
( |\psi_2\rangle = |-\rangle )
🔹 3. Verification using Inner Product
overlap = psi1.dag() * psi2
Computes: [ \langle \psi_1 | \psi_2 \rangle ]
✅ Result:
0
🔥 Interpretation:
Inner product = 0 → states are orthogonal
Therefore → completely different
🔹 4. Bloch Sphere Coordinates
x1 = (psi1.dag() * sigmax() * psi1).real
y1 = (psi1.dag() * sigmay() * psi1).real
z1 = (psi1.dag() * sigmaz() * psi1).real
Computes expectation values of Pauli matrices:

( \sigma_x, \sigma_y, \sigma_z )
📊 Results:
State	(x, y, z)
( \psi_1 )	(1, 0, 0)
( \psi_2 )	(-1, 0, 0)
🔹 5. Visualization
b = Bloch()
b.add_states(psi1)
b.add_states(psi2)
b.show()
Displays both states on Bloch sphere:

🔴 ( \psi_1 ) → +X direction
🔵 ( \psi_2 ) → −X direction
🧠 Key Concepts
🔸 Inner Product
Measures similarity between quantum states.

( = 1 ) → identical
( = 0 ) → orthogonal (completely different)
🔸 Orthogonality
Two states are orthogonal if:

[ \langle \psi_1 | \psi_2 \rangle = 0 ]

👉 Meaning:

No overlap
Perfectly distinguishable
🔸 Bloch Sphere Insight
Both states lie on equator (z = 0)

But:

( \psi_1 ) → +X axis
( \psi_2 ) → −X axis
👉 They are opposite points

🔥 Final Conclusion
Although both states have equal probability amplitudes (50% for (|0\rangle) and (|1\rangle)), they differ by a relative phase of π.

This results in:

Orthogonality (inner product = 0)
Opposite directions on Bloch sphere
Different measurement behavior
👉 Therefore:

The two states are fundamentally different quantum states.

🚀 How to Run
Open in Google Colab
Install dependencies:
pip install qutip
Run all cells
📌 Learning Outcome
This project demonstrates that:

Quantum states are not defined only by probabilities
Phase plays a critical role
Visualization + math together give full understanding
