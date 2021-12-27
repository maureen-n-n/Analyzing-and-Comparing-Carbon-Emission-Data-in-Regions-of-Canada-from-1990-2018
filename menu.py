""" CSC110 Fall 2020 Final Project : menu
================================================================

This Python module creates four different menus using the pygame menu library.

The first menu allows the user to select which graph to display, the
choices corresponding to the three graphs that can be represented in the
create_graphs.py file (which is imported in this module).

The next three menus correspond to which button was pressed in the first menu,
and allows users to select either the region of Canada to display the given
graph for (if either of the first two buttons were clicked) or which industry
to display the graph for (if the third button was clicked)

This module utilises create_graphs.py to graph the information.

===============================
This file is Copyright (c) 2020 Maureen Navera.
"""

########################################################################################
import pygame
import pygame_menu
import create_region_class
import create_graphs
# ===========================================================================================
# The following code initializes each dataset as a region class. These variables are CONSTANT
# and should NOT be changed, so they are at top-level
ALBERTA = create_region_class.dataset_to_region('datasets/AB.txt')
BRITISH_COLUMBIA = create_region_class.dataset_to_region('datasets/BC.txt')
MANITOBA = create_region_class.dataset_to_region('datasets/MB.txt')
NEW_BRUNSWICK = create_region_class.dataset_to_region('datasets/NB.txt')
NEWFOUNDLAND = create_region_class.dataset_to_region('datasets/NL.txt')
NOVA_SCOTIA = create_region_class.dataset_to_region('datasets/NS.txt')
ONTARIO = create_region_class.dataset_to_region('datasets/ON.txt')
PEI = create_region_class.dataset_to_region('datasets/PE.txt')
QUEBEC = create_region_class.dataset_to_region('datasets/QC.txt')
SASKATCHEWAN = create_region_class.dataset_to_region('datasets/SK.txt')
CANADA = create_region_class.dataset_to_region('datasets/CA.txt')
# ===========================================================================================
########################################################################################


def choose_graph() -> None:
    """ This function displays the main menu of the program. When pressing any button on the menu,
    another menu is called depending on which button is pressed. The man menu consists of two buttons:

    ---------- BUTTON 1 - Co2eq/ Year Graph ----------
    When this button is pressed, the function graph1_choose_region is called which is another
    menu with buttons representing Canada's Regions. When this button is clicked, it guarantees
    that the graph that will be displayed after will correspond to the plot_co2eq function from
    create_graphs.py which represents CO2eq Emissions vs Year for the three industries looked at in this
    project (Energy, Oil and Gas Extraction, and Transport) for a given region in Canada.

    ---------- BUTTON 2 - % Change in CO2eq/Year Graph ----------
    When this button is pressed, the function graph2_choose_region is called which is another
    menu with buttons representing Canada's Regions. When this button is clicked, it guarantees
    that the graph that will be displayed after will correspond to the plot_percent_change
    function from create_graphs.py which represents the percent change in CO2eq emissions
    per year for the three main industries that are being looked at in this project
    (Energy, Oil and Gas Extraction, and Transport) for a given Region of Canada.

    ---------- BUTTON 3 - Compare Regions ----------
    When this button is pressed, the function compare_regions is called which is another
    menu with buttons representing the three industries looked at in this project: energy,
    oil and gas extraction, and transport. When this button is clicked, it guarantees
    that the graph that will be displayed after will correspond to one of the three functions:
    the compare_energy, compare_oil_gas and compare_transport functions from create_graphs.py
    which represents the percent change in CO2eq emissions per year for the respective industry
    of all the regions looked at in this project.

    """
    pygame.init()
    surface = pygame.display.set_mode((1200, 800))
    menu = pygame_menu.Menu(800, 1200, 'Select Which Graph to Display',
                            theme=pygame_menu.themes.THEME_DARK)

    line1 = "Choose whether to graph CO2 equivalent emissions per year "
    line2 = "or the percent change in these CO2eq emissions per year "
    line3 = "or to compare regions based on their CO2eq emissions per year"
    line4 = "for a given industry ranging from 1990 - 2018 "
    line5 = "for the energy, oil and gas extraction, and transport " \
            "industries for a given region of Canada."

    menu.add_button('1. CO2eq Emissions/Year Graph', graph1_choose_region)
    menu.add_button('2. % Change in CO2eq/Year Graph', graph2_choose_region)
    menu.add_button('3. Compare Regions', compare_regions)

    menu.add_vertical_margin(50)

    menu.add_label(line1, max_char=-1, font_size=25)
    menu.add_label(line2, max_char=-1, font_size=25)
    menu.add_label(line3, max_char=-1, font_size=25)
    menu.add_label(line4, max_char=-1, font_size=25)
    menu.add_label(line5, max_char=-1, font_size=25)

    menu.mainloop(surface)


def graph1_choose_region() -> None:
    """ This function displays a menu with buttons representing each region of canada being looked
    at in this project and a return button that send the user back to the menu from choose_graph.

    When a button is pressed, a graph will be displayed using plotly in the user's browser representing
    CO2eq vs Year for the given region button that has been pressed. This function calls multiple
    functions listed below which are responsible for calling the plot_co2eq function from
    create_graphs.py on the respective region.
    """
    pygame.init()
    surface = pygame.display.set_mode((1200, 800))
    menu = pygame_menu.Menu(800, 1200, 'Choose Which Region to Graph',
                            theme=pygame_menu.themes.THEME_DARK)

    # Add Buttons
    menu.add_button('ALBERTA', create_graphs.alberta_graph1)
    menu.add_button('BRITISH COLUMBIA', create_graphs.british_columbia_graph1)
    menu.add_button('MANITOBA', create_graphs.manitoba_graph1)
    menu.add_button('NEW BRUNSWICK', create_graphs.new_brunswick_graph1)
    menu.add_button('NEWFOUNDLAND AND LABRADOR ', create_graphs.newfoundland_graph1)
    menu.add_button('NOVA SCOTIA', create_graphs.nova_scotia_graph1)
    menu.add_button('ONTARIO', create_graphs.ontario_graph1)
    menu.add_button('PRINCE EDWARD ISLAND', create_graphs.pei_graph1)
    menu.add_button('QUEBEC', create_graphs.quebec_graph1)
    menu.add_button('SASKATCHEWAN', create_graphs.saskatchewan_graph1)
    menu.add_button('CANADA', create_graphs.canada_graph1)
    menu.add_vertical_margin(50)
    menu.add_button('return', choose_graph)

    menu.mainloop(surface)


def graph2_choose_region() -> None:
    """This function displays a menu with buttons representing each region of canada being looked
    at in this project and a return button that send the user back to the menu from choose_graph.

    When a button is pressed, a graph will be displayed using plotly in the user's browser representing
    percent change in CO2eq emissions per year for the given region button that has been pressed.
    This function calls multiple functions listed below which are responsible for calling the
    plot_percent_change function from create_graphs.py on the respective region.
    """
    pygame.init()
    surface = pygame.display.set_mode((1200, 800))
    menu = pygame_menu.Menu(800, 1200, 'Choose Which Region to Graph',
                            theme=pygame_menu.themes.THEME_DARK)

    # Add Buttons
    menu.add_button('ALBERTA', create_graphs.alberta_graph2)
    menu.add_button('BRITISH COLUMBIA', create_graphs.british_columbia_graph2)
    menu.add_button('MANITOBA', create_graphs.manitoba_graph2)
    menu.add_button('NEW BRUNSWICK', create_graphs.new_brunswick_graph2)
    menu.add_button('NEWFOUNDLAND AND LABRADOR ', create_graphs.newfoundland_graph2)
    menu.add_button('NOVA SCOTIA', create_graphs.nova_scotia_graph2)
    menu.add_button('ONTARIO', create_graphs.ontario_graph2)
    menu.add_button('PRINCE EDWARD ISLAND', create_graphs.pei_graph2)
    menu.add_button('QUEBEC', create_graphs.quebec_graph2)
    menu.add_button('SASKATCHEWAN', create_graphs.saskatchewan_graph2)
    menu.add_button('CANADA', create_graphs.canada_graph2)
    menu.add_vertical_margin(50)
    menu.add_button('return', choose_graph)

    menu.mainloop(surface)


def compare_regions() -> None:
    """This function displays a menu with buttons representing each major industry being looked
    at in this project and a return button that send the user back to the menu from choose_graph.

    Pressing a button will display a graph in the user's browser using plotly which represents
    the percent change in CO2eq emissions per year for the respective industry of all the regions
    looked at in this project. This function calls graphing functions from the create_graphs.py file.
    """
    pygame.init()
    surface = pygame.display.set_mode((1200, 800))
    menu = pygame_menu.Menu(800, 1200, 'Choose Which Industry to Compare Regions With',
                            theme=pygame_menu.themes.THEME_DARK)

    # Add Buttons
    menu.add_button('ENERGY', create_graphs.compare_energy)
    menu.add_button('OIL AND GAS EXTRACTION', create_graphs.compare_oil_gas)
    menu.add_button('TRANSPORT', create_graphs.compare_transport)
    menu.add_vertical_margin(50)
    menu.add_button('return', choose_graph)

    menu.mainloop(surface)


#####################################################################################################
# Code checking using PyTa
#####################################################################################################


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['python_ta.contracts', 'create_region_class',
                          'pygame', 'pygame_menu', 'create_graphs', 'pygame.init()'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
