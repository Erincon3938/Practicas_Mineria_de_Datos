''''
                                                        Mineria de Datos
                                                           Practica 06
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import matplotlib.pyplot as plt
import statsmodels.api as sm
import numbers
import pandas as pd
from tabulate import tabulate
import numpy as np


def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt="orgtbl"))

def transform_variable(df: pd.DataFrame, x:str)->pd.Series:
    if isinstance(df[x][0], numbers.Number):
        return df[x] 
    else:
        return pd.Series([i for i in range(0, len(df[x]))])


def linear_regression(df: pd.DataFrame, x:str, y: str)->None:
    fixed_x = transform_variable(df, x)
    model= sm.OLS(df[y],sm.add_constant(fixed_x)).fit()
    print(model.summary())

    coef = pd.read_html(model.summary().tables[1].as_html(),header=0,index_col=0)[0]['coef']
    df.plot(x=x,y=y, kind='scatter', figsize=(12,7.6))
    plt.plot(df[x],[pd.DataFrame.mean(df[y]) for _ in fixed_x.items()], color='green')
    plt.plot(df_by_sal[x],[ coef.values[1] * x + coef.values[0] for _, x in fixed_x.items()], color='red')
    plt.xticks(rotation=90)
    plt.title('Linear Regression')
    plt.savefig(f'../imgs/linearegresion_{y}_{x}.png')
    plt.close()


if __name__ == "__main__":
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv") 
    df_by_sal = df.groupby("Year").aggregate(Total_Sales=pd.NamedAgg(column="Total_Sales", aggfunc=pd.DataFrame.mean))
    df_by_sal.reset_index(inplace=True)
    print_tabulate(df_by_sal.head())
    linear_regression(df_by_sal, "Year", "Total_Sales")