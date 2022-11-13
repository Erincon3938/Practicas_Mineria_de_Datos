''''
                                                        Mineria de Datos
                                                           Practica 09
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import pandas as pd
import matplotlib.pyplot as plt
from typing import Tuple, List
import numpy as np



def normalize_distribution(dist: np.array, n: int) -> np.array:
    b = dist - min(dist) + 0.000001
    c = (b / np.sum(b)) * n
    return np.round(c)


def create_distribution(mean: float, size: int) -> pd.Series:
    return normalize_distribution(np.random.standard_normal(size), mean * size)


def generate_df(means: List[Tuple[float, float, str]], n: int) -> pd.DataFrame:
    lists = [
        (create_distribution(_x, n), create_distribution(_y, n), np.repeat(_l, n))
        for _x, _y, _l in means
    ]
    x = np.array([])
    y = np.array([])
    labels = np.array([])
    for _x, _y, _l in lists:
        x = np.concatenate((x, _x), axis=None)
        y = np.concatenate((y, _y))
        labels = np.concatenate((labels, _l))
    return pd.DataFrame({"x": x, "y": y, "label": labels})


def get_cmap(n, name="hsv"):
    return plt.cm.get_cmap(name, n)


def scatter_group_by(
    file_path: str, df: pd.DataFrame, x_column: str, y_column: str, label_column: str
):
    fig, ax = plt.subplots()
    labels = pd.unique(df[label_column])
    cmap = get_cmap(len(labels) + 1)
    for i, label in enumerate(labels):
        filter_df = df.query(f"{label_column} == '{label}'")
        ax.scatter(filter_df[x_column], filter_df[y_column], label=label, color=cmap(i))
    ax.legend()
    plt.savefig(file_path)
    plt.close()


def euclidean_distance(p_1: np.array, p_2: np.array) -> float:
    return np.sqrt(np.sum((p_2 - p_1) ** 2))


def k_means(points: List[np.array], k: int):
    DIM = len(points[0])
    N = len(points)
    num_cluster = k
    iterations = 15

    x = np.array(points)
    y = np.random.randint(0, num_cluster, N)

    mean = np.zeros((num_cluster, DIM))
    for t in range(iterations):
        for k in range(num_cluster):
            mean[k] = np.mean(x[y == k], axis=0)
        for i in range(N):
            dist = np.sum((mean - x[i]) ** 2, axis=1)
            pred = np.argmin(dist)
            y[i] = pred

    for kl in range(num_cluster):
        xp = x[y == kl, 0]
        yp = x[y == kl, 1]
        plt.scatter(xp, yp)
    
    plt.xlabel('Total Sales')
    plt.ylabel('Mean Sales')
    plt.title('Clustering Total Sales and Mean Sales')
    plt.savefig('../imgs/Clustering_Total_Sales_Mean_Sales.png')
    
    return mean


def Clustering(df: pd.DataFrame) -> None:

    dfclust = pd.DataFrame()
    dfclust["Total_Sales"] = df["Total_Sales"]
    dfclust["Mean_Sales"] = df["Mean_Sales"]
    dfclust["Year"] = df["Year"]

    list_t = [
        (np.array(tuples[0:2]), tuples[2])
        for tuples in dfclust.itertuples(index=False, name=None)
    ]
    points = [point for point, _ in list_t]
    labels = [label for _, label in list_t]

    kn = k_means(points,8)

if __name__ == "__main__":
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    Clustering(df)