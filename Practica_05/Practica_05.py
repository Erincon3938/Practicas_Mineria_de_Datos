''''
                                                        Mineria de Datos
                                                           Practica 05 
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import statsmodels.api as sm
from statsmodels.formula.api import ols
import pandas as pd
from scipy.stats import shapiro
import pingouin as pg
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import kurtosis


def anova(df_aux: pd.DataFrame, str_ols: str) -> None:
    modl = ols(str_ols, data=df_aux).fit()
    anova_df = sm.stats.anova_lm(modl, typ=2)
    if anova_df["PR(>F)"][0] < 0.005:
        print("\nHay diferencias")
        print(anova_df)

    else:
        print("\nNo hay diferencias")

    
def anova_1() -> None:
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    print("\n")
    df_by_publisher = df.groupby(["Publisher", "Year"])[["Total_Sales"]].aggregate(pd.DataFrame.sum)
    df_by_publisher.reset_index(inplace=True)
    df_by_publisher.set_index("Year", inplace=True)
    df_by_publisher.reset_index(inplace=True)
    df_aux = df_by_publisher.drop(['Year'], axis=1)
    print(df_aux.head())
    anova(df_aux, "Total_Sales ~ Publisher")

def kurtosis() -> None :
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    print('\nKursotis:', stats.kurtosis(df["Total_Sales"]))
    print(f'Como {stats.kurtosis(df["Total_Sales"])} > 3 la distribución es Leptocúrtica')


def shapiro_wilk() -> None:
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    stat,p = shapiro(df["Total_Sales"]) 
    print("\nPrueba distribución normal de Shapiro-Wilk")
    print("El valor p es: ", p)
    alpha = 0.05
    
    if p > alpha:
        print('La muestra parece Gaussiana o Normal (no se rechaza la hipótesis nula H0)')
    else:
        print('La muestra no parece Gaussiana o Normal(se rechaza la hipótesis nula H0)')

def mann_whitney_wilcoxon() -> None:
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    df_muestra = df.sample(400)
    pnm = pg.mwu(df_muestra["Total_Sales"], df_muestra["Total_Games"])
    print("\nPrueba no parametrica Mann-Whitney-Wilcoxon:")
    print("El valor de p es: ", pnm.iloc[0]['p-val'])
    print ("El valor de u es: ", pnm.iloc[0]["U-val"])
    print("Como", pnm.iloc[0]['p-val'], "< 0.05 la diferencia entre las medianas es estadísticamente significativa\n")

def histogram() -> None:

    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    plt.title('Histogram of Total Sales')
    df['Total_Sales'].plot.hist()
    plt.savefig('../imgs/Histogram_Total_Sales.png')

def probability_plot() -> None:
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    plt.close()
    stats.probplot(df['Total_Sales'], plot=plt)
    plt.xlabel('Diagrama de Probabilidad(normal) de la variable {}'.format('Total Sales'))
    plt.savefig('../imgs/Probability_Plot_Total_Sales.png')


if __name__ == "__main__":
    anova_1()
    kurtosis()
    shapiro_wilk()
    mann_whitney_wilcoxon()
    histogram()
    probability_plot()
    



   