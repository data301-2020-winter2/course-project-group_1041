'''
Task #3 for Milestone 2

Created function that loads data into a pd.DataFrame;
Cleans the data using method chaining;
Filters data based on optional parameters.
'''
import pandas as pd

PATH = '../data/raw/Medical_Cost.csv'

def load_data(path, **optional_params):
    '''
    Loads the medical data, dropping all rows with NA

    Parameters
    ----------
    path : str
        Path to CSV that is loaded into a pd.DataFrame
    is_male : bool, optional
        Filters out non men when True
    is_female : bool, optional
        Filters out non women when True
    only_smokers : bool, optional
        Filters out non smokers when True
    no_smokers : bool, optional
        Filters out smokers when True
    has_children : bool, optional
        Filters out people with(out) children depending on if True or False
    older_than : int, optional
        Filters out people equal to or younger than specified age
    younger_than : int, optional
        Filters out people equal to or older than specified age
    bmi_more_than : double, optional
        Filters out people with a BMI above specified
    bmi_less_than : double, optional
        Filters out people with a BMI below specified
    charge_more_than : double, optional
        Filters out rows where charge is more than specified amount of dollars
    charge_less_than : double, optional
        Filters out rows where charge is less than specified amount of dollars
    reset_index : bool, optional
        Changes the index after the filtering when True
    drop : list[str], optional
        Drops the listed columns from the DataFrame
    [NOT YET IMPLEMENTED]
    from_region : list[str], optional
        Filters out rows where location is not in list

    Returns
    -------
    pd.DataFrame
        DataFrame loaded from path with optional filters
    '''
    # Note that the Data is already really clean so there isn't much we actually want to do in our chaining
    
    df = (
        pd.read_csv(path)
        .dropna(axis=0)
        .sort_values(['age', 'charges'])
        .assign(age_category=lambda x: pd.cut(x['age'],
                                              [17, 25, 40, 55, 65],
                                              labels=['17-25', '25-40', '40-55', '55-65']
                                             ),
                bmi_category=lambda x: pd.cut(x['bmi'],
                                              [10, 18.5, 25, 30, 40],
                                              labels=['under', 'healthy', 'over', 'obese']
                                             ),
                cost_category=lambda x: pd.cut(x['charges'],
                                              [0, 10000, 20000, 30000, 100000],
                                              labels=['$0-$10,000', '$10,000-$20,000', '$20,000-$30,000', 'Over $30,000']
                                             )
               )                                       
    )
    
    
    if ('only_smokers' in optional_params and 'no_smokers' in optional_params) or \
            ('is_male' in optional_params and 'is_female' in optional_params):
        raise Exception("Two optional params cannot be used in conjunction with one another\n"
                "only_smokers cannot be used in conjunction with no_smokers\n"
                "is_male cannot be used in conjunction with is_female")
    # Filtering by Sex
    if 'is_male' in optional_params:
        if optional_params['is_male'] == True:
            df = df[df['sex'] == 'male']
    if 'is_female' in optional_params:
        if optional_params['is_female'] == True:
            df = df[df['sex'] == 'female']
    # Filtering Smokers
    if 'only_smokers' in optional_params:
        if optional_params['only_smokers'] == True:
           df = df[df['smoker'] == 'yes']
    if 'no_smokers' in optional_params:
        if optional_params['no_smokers'] == True:
           df = df[df['smoker'] == 'no']
    # Filtering People with Children
    if 'has_children' in optional_params:
        if optional_params['has_children'] == True:
            df = df[df['children'] > 0]
        if optional_params['has_children'] == False:
            df = df[df['children'] == 0]
    # Filtering by Age
    if 'older_than' in optional_params:
        df = df[df['age'] > optional_params['older_than']]
    if 'younger_than' in optional_params:
        df = df[df['age'] < optional_params['younger_than']]
    # Filtering by Charges
    if 'charge_more_than' in optional_params:
        df = df[df['charges'] > optional_params['charge_more_than']]
    if 'charge_less_than' in optional_params:
        df = df[df['charges'] > optional_params['charge_less_than']]
    # Filtering by Region
    if 'from_region' in optional_params:
        # TODO pd.Series.isin
        pass
    # Filtering by BMI
    if 'bmi_less_than' in optional_params:
        df = df[df['bmi'] < optional_params['bmi_less_than']]
    if 'bmi_more_than' in optional_params:
        df = df[df['bmi'] > optional_params['bmi_more_than']]
    # Resets index
    if 'reset_index' in optional_params:
        if optional_params['reset_index'] == True:
            df.reset_index(inplace=True, drop=True)
    # Drop Columns
    if 'drop' in optional_params:
        df.drop(inplace=True, columns=optional_params['drop'])
            
    return df
