# Matrix-Mapped Terminal Tic-Tac-Toe Engine

A sleek, lightweight, terminal-based 2-Player Tic-Tac-Toe application built from scratch in Python. The engine utilizes custom coordinate dictionary mapping, continuous terminal frame-flushing, and tabular grid rendering to deliver a clean arcade presentation without console wall-scrolling.

##  Key Features
- **Smart Matrix Mapping:** Implements a localized coordinate dictionary lookup (`1-9`) to execute 2D matrix state switches instantly, bypassing heavy conditional forks.
- **Dynamic View Refreshing:** Couples an automated system display flush with the `tabulate` framework to render a unified, static gaming board live after every turn.
- **Robust Collision Prevention:** Wraps entry loops around active cell value checks to block token overrides and manage user retry prompts safely.
- **Dual-State Coin Toss Core:** Simulates automated starting coin tosses, dynamically rearranging game execution loops and name-token bindings based on state flags.

##  Tech Stack & Dependencies
- **Language:** Python 3
- **Libraries Required:** `tabulate`
- **Concepts Used:** 2D Matrices, Local State Synchronization, Nested Loop Control Flow, Data Validation.

##  How to Run Locally

1. Install the required grid rendering package via your terminal:
   ```bash
   pip install tabulate
   ```
2. Execute the engine:
   ```bash
   python tictactoe.py
   ```
3. Input Player 1's starting token choice, execute the coin toss selection, and input grid coordinates `1-9` sequentially.
