Treasure Trace - Treasure Map Project
=====================================

Author:
Cristopher Vega

GitHub Repository:
https://github.com/CrisVA24/treasure_map_project


Project Description
-------------------
This project consists of a graphical application developed in Python that allows users to create custom treasure maps and automatically solve them using a backtracking algorithm.

The application includes two main features:
1. Map Generator
2. Treasure Finder (Backtracking Solver)


Features
--------
Map Generator:
- Create a grid-based map with customizable size (Small, Medium, Large)
- Place elements on the map:
  - Obstacles (#)
  - Treasures (T)
  - Starting point (S)
- Visual interface using Tkinter
- Save the map to a file (map.txt)

Treasure Finder:
- Solve the map using a backtracking algorithm
- Find a valid path from the starting point to a treasure
- Display the path using '*' on the interface

How to Run
----------
1. Make sure you have Python installed (Python 3 recommended)
2. Open a terminal in the project directory
3. Run the following command:

   python main.py

4. Use the graphical interface to:
   - Select a map size
   - Create your map
   - Solve it using the "Solve Map" button


Project Structure
-----------------
treasure_map_project/

    main.py
    app.py

    views/
        start_screen.py
        map_editor_screen.py

    controllers/
        map_controller.py

    models/
        map_model.py


Technologies Used
-----------------
- Python 3
- Tkinter (GUI)


Notes
-----
- The application uses backtracking to find a valid path to a treasure.
- The algorithm stops when the first valid path is found for efficiency.
- If no solution exists, an error file is generated indicating the starting position.
