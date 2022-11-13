''''
                                                        Mineria de Datos
                                                           Practica 02 
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import pandas as pd
import numpy as np
from tabulate import tabulate


def clean_csv() -> None:

    df = pd.read_csv("../csv/video_games_sales.csv").interpolate()
    df['Rank'] = np.arange(1, len(df)+1)
    df.insert(0, "Index", np.arange(len(df)), allow_duplicates=False)
    df['Platform'] = df['Platform'].replace({"2600": 'XPLAT'})
    df['Year'] = df['Year'].astype(np.int64)
    df.to_csv("../csv/video_games_sales_clean.csv",index=False)
    print_tabulate(df)

def print_tabulate(df: pd.DataFrame) -> None:
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))


if __name__ == "__main__":
    clean_csv()
