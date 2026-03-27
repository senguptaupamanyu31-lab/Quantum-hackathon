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


# # 📌 Level 4 BB84 Protocol with Noise & Adaptive Eavesdropping Detection



## 🧠 Problem Statement

In practical quantum communication, errors arise not only from eavesdropping but also from channel noise.

You are tasked with designing a system that can distinguish between natural noise and a stealthy eavesdropper (Eve) who attempts to remain undetected.

---

## 🎯 Task

Implement a modified BB84 protocol where:

- The quantum channel has intrinsic noise  
- Eve performs an adaptive attack:
  - She intercepts only a fraction of qubits  
  - She adjusts her attack rate based on observed error levels  

---

## 🧭 Approach

To solve this problem, we model the communication process using the BB84 quantum key distribution protocol and extend it to include realistic conditions.

### 1. BB84 Simulation

- Alice generates random bits and bases (Z and X)  
- Qubits are prepared based on these values  
- Bob measures the qubits using randomly chosen bases  

Only the cases where Alice and Bob use the same basis are retained (sifting process).

---

### 2. Modeling Channel Noise

To simulate real-world conditions:

- Random bit flips are introduced during transmission  
- This represents imperfections in the quantum channel  
- Noise produces **random, unbiased errors**

---

### 3. Modeling Adaptive Eavesdropper (Eve)

Eve performs an intercept-resend attack:

- She intercepts only a fraction of qubits  
- Measures them in a random basis  
- Resends the measured state  

Adaptive behavior:

- If observed error is low → Eve increases attack rate  
- If observed error is high → Eve reduces attack rate  

This allows Eve to **hide within the noise level**

---

### 4. Error Analysis

After transmission:

- Alice and Bob compare a subset of their bits  
- The error rate is computed as the fraction of mismatched bits  

---

## 🔍 Solution Strategy

A simple threshold-based detection (error > noise) is not sufficient because Eve adapts her behavior.

Instead, we use **statistical detection over multiple rounds**:

### Key Observations

- Noise introduces **random fluctuations**  
- Eve introduces a **consistent bias in error rate**  

---

### Detection Method

We track:

- Error rate over multiple rounds  
- Average error  
- Variance (standard deviation)

Then apply:

If:
average_error > noise_level + threshold

→ Eavesdropping detected

---

## 🎯 Final Insight

Even when Eve tries to remain undetected by adjusting her attack rate, she introduces subtle but consistent deviations from expected noise behavior.

These deviations become detectable through statistical analysis over time.

---

## 🔥 Conclusion

This approach demonstrates that:

- Quantum communication can detect eavesdropping even in noisy environments  
- Adaptive attackers can hide temporarily but cannot eliminate statistical signatures  
- Reliable detection requires analyzing trends rather than single measurements  

---

## 💡 Key Takeaway

Noise is random.  
Eavesdropping is structured.  

By observing patterns over time, we can distinguish between the two.
