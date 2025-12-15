# Interactive Maze Solver using Pygame

An interactive maze generator and solver built with Python and Pygame. This application visualizes maze creation and solving in real-time, allowing users to select start and end points and watch the solving algorithm animate its progress.

---

## Features

- Randomly generated mazes using recursive backtracking
- Interactive start and end point selection
- Animated depth-first search (DFS) maze solving
- Visual feedback for each step of the solving algorithm
- Color-coded interface for clarity
- Maze regeneration with a single key press (`R`)

---

## Screenshot

![Maze Solver Preview](/Maze_solver.png)


## Controls

| Action                 | Control       |
|------------------------|---------------|
| Select start/end point | Left Click    |
| Regenerate Maze        | R key         |
| Quit                   | Close window  |


## Color Legend

| Color Name     | Hex Code     | Meaning          |
|----------------|--------------|------------------|
| Dark Indigo    | `#1B1A55`     | Path             |
| Very Dark Navy | `#03001C`     | Wall             |
| Pale Cyan      | `#76ABAE`     | Final path       |
| Forest Green   | `#00712D`     | Start cell       |
| Bright Red     | `#F93827`     | End cell         |
| Lavender Gray  | `#9290C3`     | Search progress  |
