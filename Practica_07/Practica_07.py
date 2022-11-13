''''
                                                        Mineria de Datos
                                                           Practica 07 
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



def k_neighbors(df: pd.DataFrame) -> None:
    drop_cols = ['Publisher']
    df = df.drop(columns = drop_cols)

    kmeans = KMeans(n_clusters=8, random_state=0)
    df['cluster'] = kmeans.fit_predict(df[['Total_Sales', 'Mean_Sales']])
    centroids = kmeans.cluster_centers_
    cen_x = [i[0] for i in centroids] 
    cen_y = [i[1] for i in centroids]

    df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2]})
    df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2]})
    colors = ['#DF2020', '#81DF20', '#2095DF' , '#754B34' , '#EE6C17' , '#CC48B2',
              '#AF37CC','#A3A3A3']
    df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2], 3:colors[3], 
                             4:colors[4], 5:colors[5], 6:colors[6],7:colors[7]})

    plt.scatter(df.Total_Sales, df.Total_Games, c=df.c, alpha = 0.6, s=10)
    plt.xlabel('Total Sales')
    plt.ylabel('Mean_Sales')
    plt.title('K-Nearest Neighbors Total Sales and Mean Sales')
    plt.savefig('../imgs/K_Nearest_Neighbors_Total_Sales_Mean_Sales.png')


if __name__ == "__main__":
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    k_neighbors(df)
