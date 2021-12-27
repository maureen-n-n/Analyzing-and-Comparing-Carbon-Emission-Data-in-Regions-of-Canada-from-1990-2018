""" CSC110 Fall 2020 Final Project : create_region_class
================================================================

This Python module contains the data class definition for the Region class.
This dataclass will serve as the foundation for this project and each
dataset will be able to be represented concisely using the Region dataclass.

Within this module contain helper functions which modify a given dataset in ways
such that said dataset can be represented using the Region dataclass.

===============================
This file is Copyright (c) 2020 Maureen Navera.
"""

#################################################################################################
from dataclasses import dataclass
from typing import List

# ID codes for each industry used in the original dataset (SHOULD NOT BE CHANGED)

ENERGY = '100'
OIL_GAS_EXTRACTION = '130'
TRANSPORT = '200'

# Since the datasets all use years from 1990-2018, I will create a static list to represent years

YEARS = [1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,
         2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
#################################################################################################


@dataclass()
class Region:
    """ A region of Canada (i.e Canada's Provinces/ Canada itself)

    Attributes:
      - name: the name of the region
      - energy_co2eq = a list of floats representing the Energy Industry's CO2eq data.
        The order of the list corresponds to the order of the 'years' list
      - oil_gas_co2eq = a list of floats representing the Oil and Gas Extraction
        Industry's CO2eq data. The order of the list corresponds to the oder of the 'years' list
      - transport_co2eq = a list of floats representing the Transport Industry's CO2eq data.
        The order of the list correspomds to the order of the 'years' list
      - years = a list of years that corresponds to the given dataset

    Representation Invariants:
      - self.name != []
      - len(self.energy_co2eq) == len(self.oil_gas_co2eq) ==
        len(self.transport_co2eq) == len(self.years)
      - self.years = YEARS

    Sample Usage:
    >>> alberta = Region(name='Alberta',energy_co2eq=[151398.2746, 152259.6046, 160321.8755,\
                        164191.6517, 172062.034, 176127.7771, 181430.9698, 185177.3244, \
                        186493.9281, 193430.2206, 200473.4165, 199963.6482, 199709.4543,\
                        205553.6717, 202435.4977, 199473.2191, 205710.7549, 215590.8097,\
                        210029.6779, 204265.9777, 209780.488, 217679.4508, 226704.217,  \
                        238087.505, 244203.3194, 241895.6509, 231670.2285, 239840.6539, 238783.3646] \
                        oil_gas_co2eq=[29223.03126, 28541.97373, 30755.77538, 33122.96745,\
                        32899.4167,32507.45074,32581.14734, 31734.99446, 33482.65853, 43594.85235,\
                        48215.76005, 49961.36057, 51964.28565, 55256.10193, 52816.56667, 49698.40644,\
                        52844.90889, 59984.1555, 55802.90009, 57121.65544, 58215.21341, 64130.08195, \
                        70624.14511, 76079.25125, 79288.57868, 81970.32965, 83448.4389,86874.64436, \
                        90224.89785]\
                        transport_co2eq=[22294.38153, 20640.5126, 21147.08484, 21630.31336, 24038.62145, 24289.87694,\
                        25736.12969, 28134.09393, 29115.71534, 29401.57855, 29903.89893, 31987.74864, 30830.34067,\
                        31634.28711, 32956.10039, 34007.51339, 36648.18465, 37289.13678, 37483.91502, 36028.93257,\
                        39060.43379, 38688.10027, 40223.27376, 42782.31695, 43985.9594, 41773.79175, 40033.67837,\
                        42452.51367, 44993.18951]\
                        years=YEARS)
    """
    name: str
    energy_co2eq: List[float]
    oil_gas_co2eq: List[float]
    transport_co2eq: List[float]
    years: List[int]


def dataset_to_region(dataset_name: str) -> Region:
    """This function gets information from a given dataset and transforms it into the Region dataclass.
    This function utilizes the helper functions below to extract the data from the datasets and transform
    them into applicable data types for the Region class.

    Preconditions:
        - dataset_name != ''
        -'datasets/' == ''.join([dataset_name[i] for i in range(9)])
        -'.txt' == dataset_name[-4:]
        - dataset_name[9:11] in ['AB', 'BC', 'CA', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
    """
    region = Region(name=get_name(dataset_name), energy_co2eq=get_energy_co2eq(dataset_name),
                    oil_gas_co2eq=get_oil_gas_co2eq(dataset_name), transport_co2eq=get_transport_co2eq(dataset_name),
                    years=YEARS)
    return region


#####################################################################################################
# The following functions are helper functions to create the transform_dataset function.
#####################################################################################################


def get_name(dataset_name: str) -> str:
    """This function returns the name of the region from the given dataset.

    Preconditions:
        - dataset_name != ''
        -'datasets/' == ''.join([dataset_name[i] for i in range(9)])
        -'.txt' == dataset_name[-4:]
        - dataset_name[9:11] in ['AB', 'BC', 'CA', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']

    >>> get_name('datasets/AB.txt')
    'Alberta'
    """
    name = dataset_to_list(dataset_name)[5]

    # since the datasets have been altered so that they are the same lengths to make computations
    # easier, the following piece of code is used to assign the variable name to the full name of
    # regions whose names have been altered in the datasets.
    if name == 'PEI':
        name = 'Prince Edward Island'
    elif name == 'BritishColumbia':
        name = 'British Columbia'
    elif name == 'NewBrunswick':
        name = 'New Brunswick'
    elif name == 'NL':
        name = 'Newfoundland and Labrador'
    elif name == 'NovaScotia':
        name = 'Nova Scotia'
    return name


def get_energy_co2eq(dataset_name: str) -> List:
    """This function returns the CO2eq column for the Energy industry from the original dataset as a list.

    Preconditions:
        - dataset_name != ''
        -'datasets/' == ''.join([dataset_name[i] for i in range(9)])
        -'.txt' == dataset_name[-4:]
        - dataset_name[9:11] in ['AB', 'BC', 'CA', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
    """
    region_data = dataset_to_list(dataset_name)
    return [float(region_data[i + 1]) for i in range(len(region_data)) if region_data[i] == ENERGY]


def get_oil_gas_co2eq(dataset_name: str) -> List:
    """This function returns the CO2eq column for the Oil and Gas Extraction industry
    from the original dataset as a list.

    Preconditions:
        - dataset_name != ''
        -'datasets/' == ''.join([dataset_name[i] for i in range(9)])
        -'.txt' == dataset_name[-4:]
        - dataset_name[9:11] in ['AB', 'BC', 'CA', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
    """
    region_data = dataset_to_list(dataset_name)
    return [float(region_data[i + 1]) for i in range(len(region_data)) if region_data[i] == OIL_GAS_EXTRACTION]


def get_transport_co2eq(dataset_name: str) -> List:
    """This function returns the CO2eq column for the Transport industry from the original dataset as a list.

    Preconditions:
        - dataset_name != ''
        -'datasets/' == ''.join([dataset_name[i] for i in range(9)])
        -'.txt' == dataset_name[-4:]
        - dataset_name[9:11] in ['AB', 'BC', 'CA', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
    """
    region_data = dataset_to_list(dataset_name)
    return [float(region_data[i + 1]) for i in range(len(region_data)) if region_data[i] == TRANSPORT]


def dataset_to_list(dataset_name: str) -> List:
    """This function splits the dataset (originally a string) into a list and returns that list.

    Preconditions:
        - dataset_name != ''
        -'datasets/' == ''.join([dataset_name[i] for i in range(9)])
        -'.txt' == dataset_name[-4:]
        - dataset_name[9:11] in ['AB', 'BC', 'CA', 'MB', 'NB', 'NL', 'NS', 'ON', 'PE', 'QC', 'SK']
    """
    data = ((open(dataset_name)).read()).split()
    return data


#####################################################################################################
# Code checking using PyTa
#####################################################################################################

if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'allowed-io': ['dataset_to_list'],
        'extra-imports': ['python_ta.contracts', 'dataclasses'],
        'disable': ['R1705', 'C0200'],
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
