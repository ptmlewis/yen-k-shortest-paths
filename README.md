# 🗺️ Yen’s K-Shortest Paths Algorithm

## 🧠 Overview
Finds the **K shortest distinct paths** between two nodes in a directed weighted graph using **Yen’s Algorithm**, built upon Dijkstra’s algorithm.

## ⚙️ Features
- Computes top-K unique shortest paths  
- Reuses Dijkstra’s results for efficiency  
- Detects and removes cycles automatically  
- Modular design for easy reuse in routing systems

## 🚀 Run
```bash
python yen_k_shortest_paths.py
```

## 🧩 Example Output
```
Source: A | Target: D | K = 3
1) A → B → D : 5
2) A → C → D : 6
3) A → B → C → D : 8
```

## 🧠 Skills Demonstrated
Python · Graph Theory · Shortest-Path Algorithms · Network Optimization
