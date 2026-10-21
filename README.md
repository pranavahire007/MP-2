# MP-2
# 🎲 Snake and Ladder Using Breadth-First Search (BFS)
> A simple Python-based Snake and Ladder game simulation that uses the Breadth-First Search (BFS) algorithm to find the minimum number of dice throws required to reach the destination.

---

## 🎯 Objective

The main objective of this project is to understand and implement the **Breadth-First Search (BFS) graph traversal algorithm** to solve the Snake and Ladder problem.

The project represents the game board as a graph, where each position is a node and each possible dice throw represents an edge. BFS explores the reachable positions level by level to determine the minimum number of dice throws required to reach the destination.

---

## 📖 Introduction

Snake and Ladder is a popular board game in which players move across numbered positions based on dice throws. Ladders help players move forward to higher positions, while snakes move players backward to lower positions.

In this project, a board containing 30 positions is implemented using Python. The starting position is 1, and the destination is 30. A dictionary stores the starting and ending positions of all snakes and ladders.

The **Breadth-First Search (BFS)** algorithm is used to explore possible moves. A queue stores the positions waiting to be explored, and a visited list prevents the same position from being processed multiple times.

Since BFS explores states in increasing order of the number of dice throws, it finds the minimum number of throws required to reach the destination, assuming each dice throw has equal cost.

---

## ✨ Features

| Feature | Description |
|---|---|
| Game Board | Simulates a board containing 30 positions. |
| Snakes and Ladders | Uses a dictionary to represent jumps between positions. |
| BFS Algorithm | Explores possible moves level by level. |
| Queue Implementation | Uses Python's `deque` to manage positions waiting to be explored. |
| Visited Tracking | Prevents repeated processing of the same board position. |
| Minimum Dice Throws | Calculates the minimum number of dice throws required to reach position 30. |
| Destination Check | Detects when the destination is reached. |
| Boundary Validation | Prevents moves beyond the final board position. |

---

## 🧩 Data Structure and Algorithm Used

### 1. Graph

The Snake and Ladder board is represented as an implicit graph.

- **Vertices:** Board positions from 1 to 30.
- **Edges:** Possible moves resulting from dice throws of 1 to 6.
- **Snakes and Ladders:** Special jumps that change the destination position of a move.

### 2. Queue

A queue is used to store the board positions waiting to be explored. The program uses Python's `deque` from the `collections` module.

The `popleft()` operation removes the oldest position from the queue, following the FIFO (First In, First Out) principle.

### 3. Visited List

A Boolean list records whether a position has already been visited. This avoids processing the same position repeatedly and prevents unnecessary exploration.

### 4. Breadth-First Search (BFS)

BFS explores all reachable positions in increasing order of the number of dice throws.

**Algorithm steps:**

1. Initialize the queue with the starting position 1 and zero dice throws.
2. Mark the starting position as visited.
3. Remove the next position from the queue.
4. If the destination is reached, display the minimum number of dice throws.
5. Generate all possible dice outcomes from 1 to 6.
6. Ignore moves that exceed position 30.
7. Apply the corresponding snake or ladder, if present.
8. Add each unvisited resulting position to the queue.
9. Continue until the destination is reached or no positions remain to explore.

---

## 💻 Technology Used

- **Programming Language:** Python
- **IDE:** Visual Studio Code (VS Code)
- **Data Structures:** Queue, List, and Dictionary
- **Algorithm:** Breadth-First Search (BFS)
- **Python Library:** `collections.deque`
- **Python Concepts:** Functions, Loops, Conditional Statements, Dictionaries, and Lists

---

## ⚙️ Operations

### 1. Initialize the Game Board

The board size is set to 30 positions. The program defines the starting position, destination, snakes, and ladders.

### 2. Initialize the BFS Queue

The queue starts with the initial state `(1, 0)`, representing position 1 and zero dice throws.

### 3. Explore Possible Dice Outcomes

For each position, the algorithm considers all dice outcomes from 1 to 6. Moves beyond the final position are ignored.

### 4. Apply Snakes and Ladders

If the next position contains a snake or ladder, the player's position is immediately changed to the corresponding destination.

### 5. Track Visited Positions

The program marks newly discovered positions as visited and adds them to the queue with the updated number of dice throws.

### 6. Calculate Minimum Dice Throws

When position 30 is reached, the program displays the minimum number of dice throws required.

### 7. Display the Result

The program prints whether the destination has been reached and displays the minimum number of throws.

---

## ▶️ How to Run

1. Install Python on your computer.
2. Open Visual Studio Code.
3. Create a folder named `Snake-and-Ladder-Using-BFS`.
4. Create a Python file named `main.py`.
5. Copy and paste the project code into `main.py`.
6. Open the terminal in VS Code.
7. Run the following command:

```bash
python main.py
```

8. The program will execute BFS and display the minimum number of dice throws needed to reach position 30.

---

## 📌 Learning Outcomes

- Understanding graph representation through a board game.
- Learning the Breadth-First Search (BFS) traversal algorithm.
- Understanding queue operations and the FIFO principle.
- Using a visited list to prevent repeated exploration.
- Learning how dictionaries represent special transitions such as snakes and ladders.
- Understanding how BFS finds the shortest path in an unweighted graph.
- Applying graph algorithms to solve practical problems.
- Improving Python programming and problem-solving skills.

---

## 🎓 Conclusion

The **Snake and Ladder Using BFS** mini project demonstrates how graph traversal algorithms can solve practical problems involving multiple possible moves.

By representing board positions as graph states and using a queue to explore possible dice outcomes, the program determines the minimum number of dice throws required to reach the destination.

This project provides practical experience with BFS, queues, graph traversal, and visited-state tracking. It also builds a foundation for understanding shortest-path problems and other applications of graph algorithms.

---

### 👩‍💻 Developed as a Data Structures Mini Project

**Python | Graphs | BFS | Queue | Shortest Path**
