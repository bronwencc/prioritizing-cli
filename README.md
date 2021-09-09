# Prioritizing Repo

I wrote this code to rank items by comparing two strings and asking the user to pick one. I originally envisioned using message boxes to return the input and wrote a [program](https://github.com/bronwencc/prioritizing-gui) that used the Tkinter-based [EasyGUI_Qt](https://easygui-qt.readthedocs.io/en/latest/api.html) created by user [aroberge](https://github.com/aroberge/easygui_qt). User aroberge was inspired by EasyGUI (created by Stephen Ferg).

The code was written to take in one .CSV file or allow for items to be inputed one-by-one by the user.

## Contents
This repository contains the code in a few `.py` Python files, written with version 3.8+. It also has two folders, one for saving a list of given or existing items and the other for saving the prioritizing ranking results as a .CSV file.

### Python files
There is one main Python file relying on methods contained in others.
#### `prioritize.py`
This contains the main method and calls to the other Python files. It loops through combination pairs and saves the results to files in \data-lists\ and \results\.

#### `file_ops.py`
This contains the function `getfile` which requests a filepath and then reads in the given file with the `csv` Python package to a list of lists. The function returns the file path and the list resulting from being read in.
The functions `savecsv` and `savelist` are also in this file, both of which prompt for a file name and use csv writer to save the provided list. The function `savecsv` saves a list of lists-type of data with each list on a new line in \results\. The latter `savelist` saves a list-type in one line in \data-lists\.

#### `comparing.py`
This contains a function `comparelists` to find items in common between two lists. This function is used in the method `infer` which compares four lists to draw a conclusion that one item associated with one pair of lists would be chosen over the item associated with the other pair of lists.

#### `combine.py`
This contains the function `combos` which uses `itertools.combinations` to return a list of combinations of the given size (or defaults to 2) from a given array-like.

### Folders
#### data-lists
This folder is where sample priority-ranking input data is stored.
#### results
This folder contains the sample output dictionaries as .CSV files.