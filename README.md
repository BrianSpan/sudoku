# Sudoku solver with optional visual backtracking

### Part of a portfolio of Python projects developed by Brian Spangler

Demonstration of Python and brute-force backtracking recursion  
- Usage of program-wide variable to toggle whether displayed  
- Demonstration of limitation of using 1D array instead of traditional 2D  
  
- Read sample board  
- Continuously use recursion to find unfilled square  
- Optionally display progress on Pygame screen  

### Features:  
Most examples of sudoku recursion use 2D arrays. I thought I would do a challenge of 
only using a 1D array. I didn't want to "cheat" by using a level of abstraction of putting in (x,y) and converting
to the position in the array/list but but to using the array/list directly. I did this a test so see if I could work with that limitation.
Most of the functionality is still trivial except for figuring if the inner box is valid.
See the function isvalidbox() to see the tricky math.

Constant DISPLAYPROGRESS can be set to True or False to toggle whether displayed in Pygame

### Future upgrades:  
- Loading a puzzle instead of hardcoding one  
- Instead of solving left-to-right top-to-bottom, solve in an order of a LIFO stack. This would appear random.
   

### Requirements:  
Python 3.7+  
Pygame (if DISPLAYPROGRESS is True)  

### Reference: https://en.wikipedia.org/wiki/Sudoku_solving_algorithms
