"""CSC110 Fall 2020 Final Project: main
============================================================================

This module imports and calls all the files and functions that are needed to
to run the project from start to finish. When run, the other modules will
load necessary files from the datasets that have been downloaded,
perform computations with these datasets, and produce an interactive menu
for the user to navigate.

-------------------NAVIGATING THE MENU-------------------
When this module is run, you will be met with a menu (using pygame's menu library)
that prompts you to choose whether you want to display a graph which represents
CO2eq Emissions per year, a graph which represents the percent change in CO2eq
Emissions per year, or a graph which compares the percent change in CO2eq per year
for a given industry for all of the Regions looked at in this project.
The label under the buttons also explains the buttons and what kinds of graphs they
will display.

If the first two buttons are pressed, visually, the same menu will appear. This menu
prompts the user to choose which Region of Canada's data to display for the graph
choice they made in the previous menu. Clicking on a Region button will open
the graph in the user's browser using the plotly library. This menu also
contains a return button for the user to return to the graph-choosing menu.

If the third button is pressed, the user will be taken to a menu which allows them
to select which industry to compare regions with. Selecting an industry will display
a graph representing all of the regions looked at in this project's CO2eq emission
percentage change for the industry that was clicked. This menu also contains a
return button for the user to return to the graph-choosing menu.

When a graph is displayed, plotly allows the user to choose which data to display.
The user can choose the data being displayed by clicking labels on the respective
graph's legend.

Enjoy :)

===============================
This file is Copyright (c) 2020 Maureen Navera.
"""
##############################################################################
import menu
##############################################################################

if __name__ == '__main__':
    menu.choose_graph()
