""" CSC110 Fall 2020 Final Project : create_graphs
================================================================

This Python module contains functions that will visually display graphs in the user's
web browser using plotly. This module is called by menu.py where users can choose which
graph they want displayed, so the functions are ordered in the same way the buttons
are ordered in the menu (1. functions plotting CO2eq Emissions/Year,  2. functions plotting
% Change in CO2eq/Year, and 3. functions that Compare Regions) with their helper functions
below.

There are five different types of graphs that can be displayed depending on which function is called:

---------- GRAPH TYPE 1 - plot_co2eq ----------
This graph represents CO2eq vs Year for the three industries looked at in this project
(Energy, Oil and Gas Extraction, and Transport) for a given region in Canada.
The graph used is a plotly grouped bar chart with coloured bars representing an industry.
The computational process needed to create this graph does not include any mathematical computation,
as it simply plots the points from the original dataset for users to visualize.

---------- GRAPH TYPE 2 - plot_percent_change ----------
This graph represents the percent change of CO2eq vs Year for the three industries looked at in this project
(Energy, Oil and Gas Extraction, and Transport) for a given region in Canada.
The graph used is a plotly scatter plot with connected lines.
The computational process needed to create this graph includes mathematical manipulation of values
that can be seen in the helper functions: energy_percent_change,
                                          oil_gas_percent_change,
                                          transport_percent_change

---------- GRAPH TYPE 3/4/5 - compare_energy, compare_oil_gas, compare_transport ----------
These graphs represents the percent change of CO2eq vs Year for the function's respective industry for
all of the regions looked at in this project.
The graph used is a plotly scatter plot with connected lines.
The computational process needed to create these graphs are the same ones used in the plot_percent_change
function, as they both display the same values just with more information on all of the regions.

===============================
This file is Copyright (c) 2020 Maureen Navera.
"""

############################################################################################
from typing import List
import plotly.graph_objects as go
import create_region_class
import menu
############################################################################################


############################################################################################
# Functions called when Button 1 - Co2eq/ Year Graph is clicked on the menu
############################################################################################


def alberta_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Alberta dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.ALBERTA)


def british_columbia_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the British Columbia dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.BRITISH_COLUMBIA)


def manitoba_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Manitoba dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.MANITOBA)


def new_brunswick_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the New Brunswick dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.NEW_BRUNSWICK)


def newfoundland_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Newfoundland and Labrador dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.NEWFOUNDLAND)


def nova_scotia_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Nova Scotia dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.NOVA_SCOTIA)


def ontario_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Ontario dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.ONTARIO)


def pei_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Prince Edward Island dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.PEI)


def quebec_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Quebec dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.QUEBEC)


def saskatchewan_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Saskatchewan dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.SASKATCHEWAN)


def canada_graph1() -> None:
    """This function graphs CO2eq emission vs Year for the Canada dataset in the user's browser
    using plotly. This function uses the plot_co2eq function.
    """
    plot_co2eq(menu.CANADA)


############################################################################################
# Functions called when Button 2 - % Change in CO2eq/Year Graph is clicked on the menu
############################################################################################


def alberta_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Alberta dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.ALBERTA)


def british_columbia_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    British Columbia dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.BRITISH_COLUMBIA)


def manitoba_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Manitoba dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.MANITOBA)


def new_brunswick_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    New Brunswick dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.NEW_BRUNSWICK)


def newfoundland_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Newfoundland and Labrador dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.NEWFOUNDLAND)


def nova_scotia_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Nova Scotia dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.NOVA_SCOTIA)


def ontario_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Ontario dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.ONTARIO)


def pei_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Prince Edward Island dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.PEI)


def quebec_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Quebec dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.QUEBEC)


def saskatchewan_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Saskatchewan dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.SASKATCHEWAN)


def canada_graph2() -> None:
    """This function graphs the percent change in CO2eq emissions per Year for the
    Canada dataset in the user's browser using plotly.
    This function uses the plot_percent_change function.
    """
    plot_percent_change(menu.CANADA)


############################################################################################
# Functions (that can be) called when Button 3 - Compare Regions is clicked on the menu
############################################################################################

def compare_energy() -> None:
    """This function displays a graph in the user's web browser using plotly which represents
    the percent change in CO2eq emissions per year for the energy industry for all of
    the Regions of Canada looked at in this project..

    Each line segments x value represents the percent change from the last year's CO2eq emission
    so at x = 1990, y = 0.

    This function utilizes the energy_percent_change helper function below to get a list of
    the percent change each year for the energy industry. These lists are what will be used for their respective
    line segment's y values.
    """
    y_ab = energy_percent_change(menu.ALBERTA)
    y_bc = energy_percent_change(menu.BRITISH_COLUMBIA)
    y_ca = energy_percent_change(menu.CANADA)
    y_mb = energy_percent_change(menu.MANITOBA)
    y_nb = energy_percent_change(menu.NEW_BRUNSWICK)
    y_nl = energy_percent_change(menu.NEWFOUNDLAND)
    y_ns = energy_percent_change(menu.NOVA_SCOTIA)
    y_on = energy_percent_change(menu.ONTARIO)
    y_pe = energy_percent_change(menu.PEI)
    y_qc = energy_percent_change(menu.QUEBEC)
    y_sk = energy_percent_change(menu.SASKATCHEWAN)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ab,
        name='ALBERTA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_bc,
        name='BRITISH COLUMBIA'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_mb,
        name='MANITOBA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_nb,
        name='NEW BRUNSWICK'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_nl,
        name='NEWFOUNDLAND AND LABRADOR',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ns,
        name='NOVA SCOTIA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_on,
        name='ONTARIO'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_pe,
        name='PRINCE EDWARD ISLAND',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_qc,
        name='QUEBEC',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_sk,
        name='SASKATCHEWAN'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ca,
        name='CANADA',
    ))

    fig.update_layout(title='Percent Change in CO2eq Emissions by the Energy Industry from 1990 - 2018',
                      xaxis_title="Years",
                      yaxis_title="Percent Change in CO2eq Emissions (Energy Industry)",
                      legend_title="Regions of Canada",
                      font=dict(
                          family="Arial",
                          size=18,
                          color="black"
                      ))

    fig.show()


def compare_oil_gas() -> None:
    """This function displays a graph in the user's web browser using plotly which represents
    the percent change in CO2eq emissions per year for the oil and gas extraction industry for all of
    the Regions of Canada looked at in this project..

    Each line segments x value represents the percent change from the last year's CO2eq emission
    so at x = 1990, y = 0.

    This function utilizes the oil_gas_percent_change helper function below to get a list of
    the percent change each year for the energy industry. These lists are what will be used for their respective
    line segment's y values.
    """
    y_ab = oil_gas_percent_change(menu.ALBERTA)
    y_bc = oil_gas_percent_change(menu.BRITISH_COLUMBIA)
    y_ca = oil_gas_percent_change(menu.CANADA)
    y_mb = oil_gas_percent_change(menu.MANITOBA)
    y_nb = oil_gas_percent_change(menu.NEW_BRUNSWICK)
    y_nl = oil_gas_percent_change(menu.NEWFOUNDLAND)
    y_ns = oil_gas_percent_change(menu.NOVA_SCOTIA)
    y_on = oil_gas_percent_change(menu.ONTARIO)
    y_pe = oil_gas_percent_change(menu.PEI)
    y_qc = oil_gas_percent_change(menu.QUEBEC)
    y_sk = oil_gas_percent_change(menu.SASKATCHEWAN)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ab,
        name='ALBERTA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_bc,
        name='BRITISH COLUMBIA'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_mb,
        name='MANITOBA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_nb,
        name='NEW BRUNSWICK'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_nl,
        name='NEWFOUNDLAND AND LABRADOR',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ns,
        name='NOVA SCOTIA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_on,
        name='ONTARIO'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_pe,
        name='PRINCE EDWARD ISLAND',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_qc,
        name='QUEBEC',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_sk,
        name='SASKATCHEWAN'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ca,
        name='CANADA',
    ))

    fig.update_layout(title='Percent Change in CO2eq Emissions by the Oil and Gas Extraction Industry from 1990 - 2018',
                      xaxis_title="Years",
                      yaxis_title="Percent Change in CO2eq Emissions (Oil and Gas Extraction Industry)",
                      legend_title="Regions of Canada",
                      font=dict(
                          family="Arial",
                          size=18,
                          color="black"
                      ))

    fig.show()


def compare_transport() -> None:
    """This function displays a graph in the user's web browser using plotly which represents
    the percent change in CO2eq emissions per year for the transport industry for all of
    the Regions of Canada looked at in this project..

    Each line segments x value represents the percent change from the last year's CO2eq emission
    so at x = 1990, y = 0.

    This function utilizes the transport_percent_change helper function below to get a list of
    the percent change each year for the energy industry. These lists are what will be used for their respective
    line segment's y values.
    """
    y_ab = transport_percent_change(menu.ALBERTA)
    y_bc = transport_percent_change(menu.BRITISH_COLUMBIA)
    y_ca = transport_percent_change(menu.CANADA)
    y_mb = transport_percent_change(menu.MANITOBA)
    y_nb = transport_percent_change(menu.NEW_BRUNSWICK)
    y_nl = transport_percent_change(menu.NEWFOUNDLAND)
    y_ns = transport_percent_change(menu.NOVA_SCOTIA)
    y_on = transport_percent_change(menu.ONTARIO)
    y_pe = transport_percent_change(menu.PEI)
    y_qc = transport_percent_change(menu.QUEBEC)
    y_sk = transport_percent_change(menu.SASKATCHEWAN)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ab,
        name='ALBERTA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_bc,
        name='BRITISH COLUMBIA'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_mb,
        name='MANITOBA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_nb,
        name='NEW BRUNSWICK'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_nl,
        name='NEWFOUNDLAND AND LABRADOR',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ns,
        name='NOVA SCOTIA',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_on,
        name='ONTARIO'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_pe,
        name='PRINCE EDWARD ISLAND',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_qc,
        name='QUEBEC',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_sk,
        name='SASKATCHEWAN'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_ca,
        name='CANADA',
    ))

    fig.update_layout(title='Percent Change in CO2eq Emissions by the Transport Industry from 1990 - 2018',
                      xaxis_title="Years",
                      yaxis_title="Percent Change in CO2eq Emissions (Transport Industry)",
                      legend_title="Regions of Canada",
                      font=dict(
                          family="Arial",
                          size=18,
                          color="black"
                      ))

    fig.show()


############################################################################################
# Helper functions that will actually display graphs
############################################################################################

def plot_co2eq(region: create_region_class.Region) -> None:
    """ This function displays a graph in the user's web browser using plotly which represents
    CO2eq Emissions vs Year for the three industries looked at in this project (Energy, Oil and Gas Extraction,
    and Transport) for a given region in Canada.

    The data that will be represented is based on the what dataset is being passed through
    as a Region dataclass in the parameters of this function.

    The computational process needed to create this graph does not include any mathematical computation,
    as it simply plots the points from the original dataset for users to visualize.

    Precondition:
      - region.name != []
      - len(region.energy_co2eq) == len(region.oil_gas_co2eq) ==
        len(region.transport_co2eq) == len(region.years)
      - region.years = create_region_class.YEARS
    """
    years = create_region_class.YEARS
    fig = go.Figure(data=[
        go.Bar(name='ENERGY', x=years, y=region.energy_co2eq),
        go.Bar(name='OIL AND GAS EXTRACTION', x=years, y=region.oil_gas_co2eq),
        go.Bar(name='TRANSPORT', x=years, y=region.transport_co2eq)
    ])
    fig.update_layout(barmode='group',
                      title='CO2eq Emissions from 1990 - 2018 in ' + region.name,
                      xaxis_title="Years",
                      yaxis_title="CO2eq Emissions (in metric tonnes)",
                      legend_title="Industries",
                      font=dict(
                          family="Arial",
                          size=18,
                          color="black"
                      ))
    fig.show()


def plot_percent_change(region: create_region_class.Region) -> None:
    """This function displays a graph in the user's web browser using plotly which represents
    the percent change in CO2eq emissions per year for the three main industries that
    are being looked at in this project (Energy, Oil and Gas Extraction, and Transport)
    for a given Region of Canada.

    The data that will be represented is based on the what dataset is being passed through
    as a Region dataclass in the parameters of this function.

    Each line segments x value represents the percent change from the last year's CO2eq emission
    so at x = 1990, y = 0.

    This function utilizes three helper functions below to get a list of the percent change each year
    for the three industries being looked at. Those lists are what will be used for their respective
    line segment's y values.

    Precondition:
      - region.name != []
      - len(region.energy_co2eq) == len(region.oil_gas_co2eq) ==
        len(region.transport_co2eq) == len(region.years)
      - region.years = create_region_class.YEARS
    """
    y_energy = energy_percent_change(region)
    y_oil_and_gas = oil_gas_percent_change(region)
    y_transport = transport_percent_change(region)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_energy,
        name='ENERGY INDUSTRY',
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_oil_and_gas,
        name='OIL AND GAS EXTRACTION INDUSTRY'
    ))
    fig.add_trace(go.Scatter(
        x=create_region_class.YEARS,
        y=y_transport,
        name='TRANSPORT INDUSTRY',
    ))

    fig.update_layout(title='Percent Change in CO2eq Emissions from 1990 - 2018 in ' + region.name,
                      xaxis_title="Years",
                      yaxis_title="Percent Change in CO2eq Emissions",
                      legend_title="Industries",
                      font=dict(
                          family="Arial",
                          size=18,
                          color="black"
                      ))

    fig.show()


##########################################################################################
# The following code includes helper functions for the plot_percent_change function.
##########################################################################################


def energy_percent_change(region: create_region_class.Region) -> List:
    """This function calculates the percent change of CO2eq emissions per year for a given Region of Canada
    for the Energy Industry and returns those values in a list.

    Precondition:
      - region.name != []
      - len(region.energy_co2eq) == len(region.oil_gas_co2eq) ==
        len(region.transport_co2eq) == len(region.years)
      - region.years = create_region_class.YEARS
    """
    energy_co2eq = region.energy_co2eq
    # Since we are calculating percentage change, we will set the first value
    # in the list as our starting value at 0.
    percent_change = [0]

    for i in range(len(energy_co2eq) - 1):
        next_element = ((energy_co2eq[i + 1] - energy_co2eq[i]) / energy_co2eq[i]) * 100
        list.append(percent_change, next_element)

    return percent_change


def oil_gas_percent_change(region: create_region_class.Region) -> List:
    """This function calculates the percent change of CO2eq emissions per year for a given Region of Canada
    for the Oil and Gas Extraction Industry and returns those values in a list.

    Precondition:
      - region.name != []
      - len(region.energy_co2eq) == len(region.oil_gas_co2eq) ==
        len(region.transport_co2eq) == len(region.years)
      - region.years = create_region_class.YEARS
    """
    oil_gas_co2eq = region.oil_gas_co2eq
    # Since we are calculating percentage change, we will set the first value
    # in the list as our starting value at 0.
    percent_change = [0]
    for i in range(len(oil_gas_co2eq) - 1):
        if oil_gas_co2eq[i] == 0:
            next_element = (oil_gas_co2eq[i + 1] - oil_gas_co2eq[i]) * 100
        else:
            next_element = ((oil_gas_co2eq[i + 1] - oil_gas_co2eq[i]) / oil_gas_co2eq[i]) * 100
        list.append(percent_change, next_element)

    return percent_change


def transport_percent_change(region: create_region_class.Region) -> List:
    """This function calculates the percent change of CO2eq emissions per year for a given Region of Canada
    for the Transport Industry and returns those values in a list.

    Precondition:
      - region.name != []
      - len(region.energy_co2eq) == len(region.oil_gas_co2eq) ==
        len(region.transport_co2eq) == len(region.years)
      - region.years = create_region_class.YEARS
    """
    transport_co2eq = region.transport_co2eq
    # Since we are calculating percentage change, we will set the first value
    # in the list as our starting value at 0.
    percent_change = [0]
    for i in range(len(transport_co2eq) - 1):
        next_element = ((transport_co2eq[i + 1] - transport_co2eq[i]) / transport_co2eq[i]) * 100
        list.append(percent_change, next_element)

    return percent_change


#####################################################################################################
# Code checking using PyTa
#####################################################################################################

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 130,
        'extra-imports': ['python_ta.contracts', 'create_region_class', 'plotly.graph_objects', 'menu'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
