import pandas as pd
import numpy as np

PATH = '../data/raw/Medical_Cost.csv'

def load_data(path, **optional_params):
    '''
    Loads the medical data, dropping all rows with NA

    Note that the Data is already really clean

    OPTIONAL PARAMETERS
     - only_smokers (bool): When True, data set will only include rows where there
           smoker == 'yes'
     - no_smokers (bool): When True, data set will not include any smokers
     - has_children (bool): When True, data set will only include rows that have children
           When False, data set will only include rows that have 0 children
     - from_region (list[string]): only includes rows from given region
           Accepted regions ['southwest','southeast','northwest','northeast']
     - older_than (int): returns rows with age above what is given
     - younger_than (int): returns rows with age below what is given
     - is_male (bool): returns data with only males
     - is_female (bool): returns data with only females
    '''
    df = (
        pd.read_csv(path)
        .dropna(axis=0)
    )

    if 'only_smokers' in optional_params:
        if optional_params['only_smokers']:
            

    return df
