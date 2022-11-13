''''
                                                        Mineria de Datos
                                                           Practica 04
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def create_boxplot_by_type(df: pd.DataFrame ) -> None :
    df_by_type = df.groupby(["Publisher","Year"])[["Total_Sales"]].aggregate(pd.DataFrame.mean)
    df_by_type.boxplot(by = 'Publisher', figsize=(12,7.6)) 
    plt.xticks(rotation=90)
    plt.title(f'Mean Total Game Sales in Millions\n')
    plt.savefig(f"../imgs/Boxplot_Publisher_Total_Sales.png")
    plt.close()


def plot_by_publisher(df: pd.DataFrame, pub:str) -> None :
    df[df["Publisher"] == pub].plot(y =["Total_Games"])
    plt.title(f'Mean total game sales in millions of {pub}\n')
    plt.savefig(f"../imgs/Linealplot_{pub}.png")
    df[df["Publisher"] == pub].boxplot(by ='Publisher')
    plt.savefig(f"../imgs/Boxplot_{pub}.png")


def create_plot_publisher(df: pd.DataFrame) -> None :

    df_by_pub = df.groupby(["Publisher","Year"])[["Total_Games"]].aggregate(pd.DataFrame.mean)
    df_by_pub.reset_index(inplace=True)
    df_by_pub.set_index("Year", inplace=True)

    for pub in set(df_by_pub["Publisher"]):
       plot_by_publisher(df_by_pub, pub)
    df_aux = df.groupby(["Year" ,"Publisher"])[["Total_Games"]].mean().unstack()
    df_aux.plot(y = 'Total_Games', legend=False, figsize=(32,18))
    plt.xticks(rotation=90)
    plt.legend()
    plt.title(f'Mean Total Game Sales in Millions\n')
    plt.savefig("../imgs/Mean_Total_Sales.png")
    plt.close()


def bar_graphic(df: pd.DataFrame) -> None :

    
    df_by_total_sales = df.groupby("Publisher")[["Total_Games"]].aggregate(pd.DataFrame.sum)
    df_by_total_sales.plot(kind = 'barh',figsize = (9.2,6),color = '#DA2E2E').get_legend().set_visible(False)
    plt.title(f'Total Games in Million\n')
    plt.savefig('../imgs/Bar_Graphic_Total_Games.png')

    df_by_total_games = df.groupby("Publisher")[["Total_Sales"]].aggregate(pd.DataFrame.sum)
    df_by_total_games.plot(kind = 'barh',figsize = (9.2,6),color = '#2E8EDA').get_legend().set_visible(False)
    plt.title(f'Total Game Sales in Millions\n')
    plt.savefig('../imgs/Bar_Graphic_Total_Sames_Sales.png')

    df_by_sales_minimum = df.groupby("Publisher")[["Sales_Minimum"]].aggregate(pd.DataFrame.sum)
    df_by_sales_minimum.plot(kind = 'barh',figsize = (9.2,6),color = '#4BC554').get_legend().set_visible(False)
    plt.title(f'Minimum Video Game Sales in Millions\n')
    plt.savefig('../imgs/Bar_Graphic_Sales_Minimum.png')

    df_by_mean_sales = df.groupby("Publisher")[["Mean_Sales"]].aggregate(pd.DataFrame.sum)
    df_by_mean_sales.plot(kind = 'barh',figsize = (9.2,6),color = '#F15E1A').get_legend().set_visible(False)
    plt.title(f'Mean Video Game Sales in Millions\n')
    plt.savefig('../imgs/Bar_Graphic_Mean_Sales.png')

    df_by_maximum_sales = df.groupby("Publisher")[["Sales_Maximum"]].aggregate(pd.DataFrame.sum)
    df_by_maximum_sales.plot(kind = 'barh',figsize = (9.2,6),color = '#5ECFDD').get_legend().set_visible(False)
    plt.title(f'Maximum Video Game Sales in Millions\n')
    plt.savefig('../imgs/Bar_Graphic_Maximum_Sales.png')


def func(pct, allvalues) -> str: 
    absolute = int(pct / 100.*np.sum(allvalues)) 
    return "{:.1f}%".format(pct, absolute) 

def pie_graphic(df: pd.DataFrame)-> None:

    explode = tuple((0.04 for x in range(16)))

    df = df.groupby("Publisher")[["Total_Sales"]].aggregate(pd.DataFrame.sum)
    df.plot(kind='pie',subplots=True ,autopct= lambda pct: func(pct, df), explode=explode,startangle = 0,
        pctdistance = 0.8, figsize = (9.2,6))
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    plt.legend().set_visible(False)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)
    plt.title(f'Total Game Sales')
    plt.axis("equal")
    plt.savefig('../imgs/Pie_Graphic_Total_Games_sales.png')

def graphics() -> None:

    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv") 
    bar_graphic(df)
    pie_graphic(df)
    create_boxplot_by_type(df)
    create_plot_publisher(df)

    
if __name__ == "__main__":
    graphics()