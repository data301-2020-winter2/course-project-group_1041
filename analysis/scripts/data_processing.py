import pathlib
import pandas as pd
from project_functions import load_data

processed_path = pathlib.Path(__file__).parent.parent
data_path = processed_path.parent/'data/processed/'
PATH = processed_path.parent/'data/raw/Medical_Cost.csv'

if __name__ == '__main__':
    default_df = load_data(PATH)
    only_smokers = load_data(
        PATH,
        only_smokers=True,
        drop=['smoker']
    )
    no_smokers = load_data(
        PATH,
        no_smokers=True,
        drop=['smoker']
    )

    for filename, df in zip(
        ['processed_medical_cost.csv','processed_smokers.csv','processed_no_smokers.csv'],
        [default_df, only_smokers, no_smokers]
    ):
        df.to_csv(processed_path/filename)
