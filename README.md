# TURING TEST + CAPTCHA IMPLEMENTATION

## Overview
This project demonstrates the concepts of Turing Test and CAPTCHA system by implementing a simple CAPTCHA verification system using Python(Flask) and HTML. The system generates distorted CAPTCHA images that humans can recognise but automated bots find difficult to solve.

## What is the Turing Test?
Proposed originally by Alan Turing in 1950, the Turing Test, is a method to determine whether a machine can exibit a level of intelligence equivalent to a human.

In the test:  
- A human judge communicates with both a human and a machine.  
- The judge does not know which participant is the machine.  
- If the judge cannot reliably distinguish the machine from the human, the machine is said to have passed the Turing Test.

## What is CAPTCHA?
CAPTCHA : Completely Automated Public Turing test to tell Computers and Humans Apart

It is a security mechanism used by websites to prevent automated bots from performing actions such as:

- creating fake accounts  
- spamming forms  
- scraping data  
- brute-force login attempts

The idea behind CAPTCHA is closely related to the concept of the Turing Test. Here, instead of testing whether machines can behave like humans, it tests whether users behave like humans instead of bots.
This project implements a text-based CAPTCHA system with image distortion.

## Project Structure
```
AI_Assignments/
|
└─ Captcha/
   │
   ├── captcha_app.py        # Main Flask application
   │
   ├── templates/
   │   └── Captcha.html      # Web interface
   │
   └── static/
       └── captcha.png       # Generated CAPTCHA image
```

## How the system works
1. The Flask server starts and hosts a webpage.  
2. A random CAPTCHA string is generated.  
3. The program creates an image containing the CAPTCHA text.  
4. Characters are randomly rotated and spaced.  
5. Noise lines and dots are added to increase difficulty.  
6. The image is displayed on the webpage.  
7. The user enters the CAPTCHA text.  
8. The server compares the input with the generated CAPTCHA.
   If the values match :
       Access Granted
   Otherwise :
       Incorrect CAPTCHA
9. A new CAPTCHA is generated after each attempt.

## How to run the project
1. Install dependencies
   ```
   pip install flask pillow
   ```
   or
   ```
   py -m pip install flask pillow
   ```
2. Navigate to the project folder
   ```
   cd Captcha
   ```
3. Run the flask application
   ```
   py captcha_app.py
   ```
4. Open the application in a browser
   Go to :
   ```
   http://127.0.0.1:5000
   ```
   The CAPTCHA verification page will appear.

## Project Features
This implementation includes:
- Random CAPTCHA generation (letters and numbers)  
- Character rotation and distortion  
- Random spacing between characters  
- Noise lines across the image  
- Random noise dots  
- Web-based CAPTCHA display  
- User input validation  
- CAPTCHA regeneration after each attempt

These distortions make it difficult for automated programs to reliably recognize the text.

## Technologies Used
- Python  
- Flask (web server framework)  
- Pillow [PIL] (for CAPTCHA image generation)  
- HTML (for the user interface)


# SEARCH ALGORITHMS (WITH MISSIONARY CANNIBAL EXAMPLE)

## Overview
This project implements the classic Missionaries and Cannibals problem using several uninformed search algorithms in Python.

The objective is to safely transport three missionaries and three cannibals across a river using a boat that can carry at most two people, without ever leaving missionaries outnumbered by cannibals on either side.

## Problem Description
There are :
- 3 Missionaries
- 3 Cannibals
- 1 Boat

The boat can carry at most two people at a time and there must be at least one traveller to operate the boat.  
The goal is to enure all the missionaries and cannibals reach the other side (left to right || right to left) safely.  
At no point should the number of cannibals exceed the number of missionaries on either side of the river (unless there are no missionaries on that side).  
If the condition is violated (i.e. number of cannibals >number of missionaries) at any givent point, the missionaries would be eated and it is considered a failed attempt.

## State Representation
Each state is represented a a tuple :
```
(M, C, B)
```
where :
- M : number of missionaries on the left bank
- C : number of cannibals on the left bank
- B : boat position
   - B = 0  → boat on left bank
   - B = 1  → boat on right bank

Initial State : (3, 3, 0)  
Goal State : (0, 0, 1)

## Search Algorithms Implemented
The following uninformed search strategies are implemented:

1. Breadth-First Search (BFS) :  
Explores states level by level using a queue.  
Guarantees the shortest solution path.

2. Depth-First Search (DFS) :  
Explores as far as possible along a branch before backtracking using a stack.

3. Iterative Deepening Depth First Search (IDDFS) :  
Combines the advantages of DFS and BFS by performing DFS with increasing depth limits.

## Project Structure
```
AI_Assignments/
|
└─ Search Algorithms/
   │
   └─ SearchAlgo_MissionaryCannibal.py
```
The file contains:
- Problem definition
- State validation
- Successor generation
- BFS implementation
- DFS implementation
- Depth-Limited Search (DLS)
- Iterative Deepening DFS (IDDFS)

## How the program works
1. The problem is initialized with the starting state.
2. A search algorithm explores possible states.
3. Each state generates valid successor states.
4. Invalid states (where missionaries are outnumbered) are discarded.
5. The algorithm continues searching until the goal state is found.
6. The sequence of states leading to the solution is returned.

## How to run the program
1. Navigate to the project directory
   ```
   cd Search_Algorithms
   ```
2. Run the python file
   ```
   python SearchAlgo_MissionaryCannibal.py
   ```
   or
   ```
   py SearchAlgo_MissionaryCannibal.py
   ```
The program will print the solution paths found using :  
- BFS
- DFS
- IDDFS

## Techologies Used
- Python (to implement the problem logic and search algorithms)
- Python Standard Library (to implement the queue structure for Breadth-First Search (BFS))
