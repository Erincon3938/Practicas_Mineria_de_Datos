''''
                                                        Mineria de Datos
                                                           Practica 03
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import pandas as pd
from tabulate import tabulate

def print_tabulate(df: pd.DataFrame):
    print(tabulate(df, headers=df.columns, tablefmt='orgtbl'))

def categorize(Publisher:str) -> str:

    if 'Nintendo' in Publisher:
        return 'Nintendo'

    elif 'Microsoft Game Studios' in Publisher:
        return 'Microsoft'

    elif 'Take-Two Interactive' in Publisher:
        return 'Take-Two'
    
    elif 'Sony Computer Entertainment' in Publisher or 'Sony Computer Entertainment Europe' in Publisher:
        return 'Sony'
    
    elif 'Activision' in Publisher:
        return 'Activision'

    elif 'Ubisoft' in Publisher:
        return 'Ubisoft'
    
    elif 'Bethesda Softworks' in Publisher:
        return 'Bethesda'

    elif 'Electronic Arts' in Publisher:
        return 'EA'

    elif 'Sega' in Publisher:
        return 'Sega'

    elif 'Square Enix' in Publisher or 'SquareSoft' in Publisher:
        return 'Square Enix'

    elif 'Atari' in Publisher:
        return 'Atari'

    elif 'Konami Digital Entertainment' in Publisher:
        return 'Konami'

    elif 'Capcom' in Publisher:
        return 'Capcom'
    
    elif 'Namco Bandai Games' in Publisher:
        return 'Bandai Namco'

    elif 'THQ' in Publisher:
        return 'THQ'

    return 'Otro'

def normalize_data() -> pd.DataFrame:
    df = pd.read_csv("../csv/video_games_sales_clean.csv")
    df["Publisher"] = df["Publisher"].map(str).map(categorize)
    return df

def analysis_publisher() -> None:
    df = normalize_data()
    df_by_publisher = df.groupby(["Publisher","Year"]).agg({'Global_Sales': ['sum', 'min', 'max','mean','count']})
    df_by_publisher.reset_index(inplace=True)
    df_by_publisher.columns = ['Publisher','Year','Total_Sales','Sales_Minimum','Sales_Maximum','Mean_Sales','Total_Games']
    print_tabulate(df_by_publisher)
    df_by_publisher.to_csv("../csv/video_games_sales_clean_analysis.csv", index=False)


if __name__ == "__main__":
    analysis_publisher()
