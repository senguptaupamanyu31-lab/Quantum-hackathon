# Quantum Hackathon 🚀

This repository contains projects developed during the Q-Hack Quantum Computing Hackathon, which was structured as a multi-level challenge. Each level focuses on progressively deeper concepts in quantum computing and circuit design. :contentReference[oaicite:0]{index=0}

---

# 📌 Level 1: Design of a 4-bit Ripple Carry Adder using Quantum Circuits

## 🧠 Objective
The goal of Level 1 was to translate a classical digital circuit (4-bit ripple carry adder) into a reversible quantum circuit using quantum gates.

Unlike classical circuits, quantum circuits must:
- Preserve information (reversibility)
- Avoid overwriting inputs
- Use additional qubits (ancilla) for intermediate computations

## ⚙️ What We Built
We implemented a 4-bit Ripple Carry Adder using:
- CNOT (CX) gates → XOR operations  
- Toffoli (CCX) gates → AND (carry generation)  

Each bit addition is handled using a quantum full adder block, and carry propagates from one stage to the next — forming a ripple carry structure.

## 🔢 Qubit Mapping

| Register | Qubits | Description |
|----------|--------|------------|
| A | q0–q3 | First 4-bit input |
| B | q4–q7 | Second 4-bit input |
| Sum | q8–q11 | Output sum |
| Carry | q12–q16 | Carry propagation |
| Temp | q17–q20 | Ancilla qubits |

## 🔁 Working Principle

Sum: S = A ⊕ B ⊕ Cin  
Carry: Cout = (A · B) ⊕ (Cin · (A ⊕ B))

Steps:
- Compute A ⊕ B using CNOT gates  
- Compute sum using XOR with carry-in  
- Generate carry using Toffoli gates  
- Propagate carry  
- Uncompute ancilla qubits  

## 🧪 Example

A = 1011 (11)  
B = 0110 (6)  
Output = 10001 (17)

---

# 📌 Level 2: Smart City Emergency Priority System using Multiplexer (MUX)

## 🧠 Problem Statement

In a smart city environment, multiple sensors monitor:
- Fire Detection  
- Gas Leakage  
- Intrusion Detection  
- Medical Emergency  

Due to limited bandwidth, only one signal can be transmitted.

## ⚙️ Approach

### Classical Priority
Fire > Gas > Intrusion > Medical

### Quantum Implementation
- CX gates  
- CCX gates  
- MCX gates  

## 🔢 Qubit Mapping

| Qubit | Signal |
|------|--------|
| q0 | Medical |
| q1 | Intrusion |
| q2 | Gas |
| q3 | Fire |
| q4 | Output |

## 🧪 Key Idea

Superposition allows simultaneous evaluation of all input combinations.

---

# 📌 Level 3: Quantum State Analysis using QuTiP

## 🧠 Problem Statement

ψ₁ = (|0⟩ + |1⟩) / √2  
ψ₂ = (|0⟩ − |1⟩) / √2  

Claim: *“Both states look similar on the Bloch Sphere”*

## 🔍 Results

- Inner product = 0 → orthogonal  
- Bloch coordinates:
  - ψ₁ → (1, 0, 0)
  - ψ₂ → (-1, 0, 0)

## 🎯 Conclusion

The states are **NOT similar**.  
They differ by phase and lie in opposite directions on the Bloch sphere.

---

# 📌 Level 4: Adaptive Eavesdropping Detection (BB84 Protocol)

## 🧠 Problem Statement

In real quantum communication:
- Errors arise from noise and eavesdropping  
- Eve adapts her attack to remain undetected  

Goal:
Detect Eve even when she hides within noise.

---

## 🎯 Objective

- Simulate BB84 protocol  
- Introduce noise  
- Add adaptive attacker  
- Detect using statistical methods  
- Visualize in real time  

---

## ⚙️ Approach

System Flow:

Alice → Eve → Noise → Bob → Compare → Detect  

Key Idea:
- Noise → random errors  
- Eve → structured disturbance  
- Detection → statistical deviation  

---
