# State Space Search

Summer 2020 Project 1


# Setup

+ Use python from a dedicated repository like `brew` or `apt`. (Default Python 3 in macOS doesn't work with `tkinter` library.)

    `brew install python` &nbsp;&nbsp;&nbsp;&nbsp;(*this installs* `python3`)

+ Verify python3 installation:

    `which python3` &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(*should return path like* `/usr/local/bin/python3`)

+ Install project:

    `cd /path/to/directory`

    `git init`

    `git remote add origin https://github.com/saura8h/State-Space-Search.git`

    `git pull origin master`

+ Python virtual environment:

    `python3 -m venv sss`

    `source sss/bin/activate`

+ Run project:

    `python pacman.py`


# Test functions

+ Test search agent:

    `python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch`

+ Depth First Search:

    `python pacman.py -l tinyMaze -p SearchAgent -a fn=dfs`

    `python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs`

    `python pacman.py -l bigMaze -p SearchAgent -a fn=dfs`

+ Breadth First Search:

    `python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs`

    `python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs`

    `python pacman.py -l bigMaze -p SearchAgent -a fn=bfs`

+ Uniform Cost Search:

    `python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs`

    `python pacman.py -l mediumDottedMaze -p StayEastSearchAgent` 
    
    `python pacman.py -l mediumScaryMaze -p StayWestSearchAgent`

+ All functions (includes additional functions like `aStarSearch`, etc.)

    `python autograder.py` 

    (**NOTE**: Current project specification only requires *q1, q2,* and *q3* to pass. *q4* onwards is implemented in the [heuristic search][1] project.)


# Team

| Members                |
| ---------------------- |
| Jacqueline I. Cardenas |
| Loai AlFarran          |
| Saurabh Mishra         |
| Wayne Lin              |


[1]: https://github.com/thrended/AI/Heuristic-Search
