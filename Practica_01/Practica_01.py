''''
                                                        Mineria de Datos
                                                           Practica 01 
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import requests , io
import pandas as pd
from tabulate import tabulate

def get_csv_from_url(url : str) -> pd.DataFrame:
    r = requests.get(url).content
    return pd.read_csv(io.StringIO(r.decode('utf-8')))

def print_tabulate(df: pd.DataFrame) -> None:
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

csv_url = 'https://gist.githubusercontent.com/zhonglism/f146a9423e2c975de8d03c26451f841e/raw/vgsales.csv'

if __name__ == "__main__":
    df = get_csv_from_url(csv_url)
    print_tabulate(df)
    df.to_csv("../csv/video_games_sales.csv",index=False)
    
