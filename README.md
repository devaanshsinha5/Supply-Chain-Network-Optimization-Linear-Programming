# Supply-Chain-Network-Optimization-Linear-Programming
A Linear Programming model using Python (PuLP) to minimize Total Landed Cost in a multi-echelon network.
# Multi-Echelon Supply Chain Network Optimization

![Project Status](https://img.shields.io/badge/Status-Optimal-success)
![Optimization](https://img.shields.io/badge/Method-Linear%20Programming-blue)
![Python](https://img.shields.io/badge/Code-Python%20%7C%20PuLP-yellow)

## 📌 Project Overview
This project utilizes **Operations Research (OR)** techniques to optimize a multi-stage logistics network. Using **Linear Programming (LP)**, I modeled the flow of goods from manufacturing plants through distribution centers (transshipment nodes) to final retail zones.

The objective was to minimize **Total Landed Cost (TLC)** while adhering to strict supply, demand, and capacity constraints. The project includes a post-optimality **Sensitivity Analysis** to identify critical bottlenecks and guide strategic infrastructure investment.

## 🛠️ Tools & Technologies
* **Language:** Python 3.10+
* **Optimization Library:** `PuLP` (Linear Programming Solver)
* **Methodology:** Network Simplex, Sensitivity Analysis (Shadow Pricing)

## 📊 Key Strategic Results
Based on the optimization run, the model established a baseline optimal cost of **$12,400.00**. The sensitivity analysis revealed two critical insights for capital investment:

### 1. Primary Bottleneck: Distribution Center 1
* **Shadow Price:** `$-4.00`
* **Interpretation:** DC 1 is the most critical constraint in the network. Expanding capacity here offers the highest ROI, reducing total network costs by **$4.00 per unit** of added capacity.

### 2. Secondary Bottleneck: Plant 2
* **Shadow Price:** `$-2.00`
* **Interpretation:** Unlike Plants 1 and 3 (which have excess slack), **Plant 2** is operating at maximum capacity. Increasing production capabilities at Plant 2 would yield a savings of **$2.00 per unit**.

### 3. Cost-to-Serve Analysis
The model calculated the marginal cost of serving each retail zone:
* **Retailer 4** is the most expensive region to serve (Marginal Cost: **$13.00/unit**).
* **Retailers 1 & 2** are the most efficient regions (Marginal Cost: **$8.00/unit**).

## 🧮 Mathematical Formulation
The problem was formulated as a **Minimum Cost Flow** problem:

$$\text{Minimize } Z = \sum_{i} \sum_{j} c_{ij} x_{ij}$$

**Subject to:**
1.  **Supply Constraints:** $\sum x_{ij} \le S_i$
2.  **Flow Conservation:** $\sum Inflow = \sum Outflow$ (at DCs)
3.  **Demand Satisfaction:** $\sum x_{jk} \ge D_k$

## 📉 Sensitivity Analysis Data
The following "Shadow Prices" (Dual Values) were generated to guide management decisions:

| Constraint Name | Shadow Price | Business Interpretation |
| :--- | :--- | :--- |
| **DC_Capacity_DC1** | **$-4.00** | **High Priority Invest:** Max ROI for expansion. |
| **Supply_Constraint_P2** | **$-2.00** | **Invest:** Production limit is binding. |
| **Supply_Constraint_P1** | **$0.00** | **Do Not Invest:** Excess capacity exists. |
| **Retailer 4 Demand** | **$13.00** | **High Cost:** Most expensive customer zone. |

## 🚀 How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/devaanshsinha5/supply-chain-network-optimization.git](https://github.com/devaanshsinha5/supply-chain-network-optimization.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pulp
    ```
3.  Run the model:
    ```bash
    python main.py
    ```

---
*Author: Devaansh Sinha*
