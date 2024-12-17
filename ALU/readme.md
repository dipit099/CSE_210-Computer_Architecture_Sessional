# 4-bit ALU Simulation and Hardware Implementation

## Overview  
This repository contains the **4-bit ALU** simulation and hardware implementation project for **CSE 210 (Computer Architecture Sessional)** at **BUET**.  

### **Functional Requirements**
- Efficiently design the ALU **with minimum possible ICs**.  
- The following **FLAGS** must be implemented:
   - **C (Carry)**
   - **S (Sign)**
   - **V (Overflow)**
   - **Z (Zero)**  

---

### **Operations**  

#### **NOT Operation**  
- **Z Flag**: 1 if result is `0000`.  
- **S Flag**: Reflects the MSB; incorrect changes will not be accepted.  
- **C & V Flags**: Can be treated as "Don't Care".  

#### **AND/OR/XOR Operation**  
- **C and V Flags**: Cleared (`0`) after operation.  
- **S and Z Flags**: Updated based on output.  

---

### **Control Signals**  

| **cs2** | **cs1** | **cs0** | **Operation**          |
|---------|---------|---------|------------------------|
| 0       | 0       | 0       | Add with Carry         |
| 0       | X       | 1       | Sub with Borrow        |
| 0       | 1       | 0       | Transfer A             |
| 1       | 0       | 0       | Increment A            |
| 1       | X       | 1       | **OR**                 |
| 1       | 1       | 0       | Decrement A            |

---

## ⚙️ Tools Used  
- Hardware Implementation

---



