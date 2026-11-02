# AISC Practical — Flat Python Program Collection

All 30 programs are directly inside this ZIP. There are **no folders**.
Extract all files into one folder and run any script independently.

## Files

### Half Adder, Full Adder, Perceptron
- `Half_Adder_MCP.py`
- `Full_Adder_MCP.py`
- `Single_Layer_Perceptron_AND.py`

### Water Jug
- `Water_Jug_A_Star.py`
- `Water_Jug_BFS.py`
- `Water_Jug_DFS.py`
- `Water_Jug_Greedy_Best_First.py`

### 8-Puzzle
- `Eight_Puzzle_A_Star_Manhattan.py`
- `Eight_Puzzle_A_Star_Misplaced_Tiles.py`
- `Eight_Puzzle_BFS.py`
- `Eight_Puzzle_DFS.py`
- `Eight_Puzzle_Greedy_Best_First.py`

### Experiment 05: Backpropagation
- `Exp05_Backpropagation_2_2_1.py`

### Experiment 06: Kohonen SOFM and LVQ
- `Exp06_Kohonen_SOFM.py`
- `Exp06_LVQ.py`

### Experiment 07: Associative Memory
- `Exp07_Autoassociative_Memory.py`
- `Exp07_BAM.py`
- `Exp07_Heteroassociative_Memory.py`

### Experiment 08: Fuzzy Sets and Relations
- `Exp08_AlgebraicProduct.py`
- `Exp08_AlgebraicSum.py`
- `Exp08_BoundedDifference.py`
- `Exp08_BoundedSum.py`
- `Exp08_CartesianProduct.py`
- `Exp08_FuzzyComplement.py`
- `Exp08_FuzzyIntersection.py`
- `Exp08_FuzzyUnion.py`
- `Exp08_MaxMinComposition.py`
- `Exp08_MaxProductComposition.py`

### Experiment 09: Fuzzy Logic Controller
- `Exp09_Fuzzy_Logic_Controller.py`

### Experiment 10: ANFIS
- `Exp10_ANFIS.py`

## Run on Ubuntu / terminal

```bash
python3 --version
python3 -m pip install -r requirements.txt
python3 Half_Adder_MCP.py
python3 Full_Adder_MCP.py
python3 Water_Jug_BFS.py
python3 Eight_Puzzle_A_Star_Manhattan.py
python3 Exp05_Backpropagation_2_2_1.py
```

Run the other files using the same `python3 FileName.py` syntax.
Fuzzy controller and ANFIS scripts create plots in the current working directory.

## Provenance / scope

- Exp05–Exp10 are adapted from the uploaded AISC assignment PDFs.
- Half Adder and Perceptron follow the chat examples; Full Adder and the search programs are additional standard practical examples.
- Exp06 SOFM follows the assignment’s winner-only update.
- Exp07 BAM mirrors forward recall as shown in the assignment.
- The ANFIS dataset is scikit-learn diabetes progression data with median-split proxy targets, not actual diabetes diagnoses.

No Python source code has been altered while flattening the archive.
