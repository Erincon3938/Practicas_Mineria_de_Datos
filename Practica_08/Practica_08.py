''''
                                                        Mineria de Datos
                                                           Practica 08
                                            Ernesto Guadalupe Rincon Ortiz 1903481
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm


def Forecasting(df: pd.DataFrame) -> None:

    a = df['Publisher']
    b = df['Year']
    c = df['Total_Sales']
    d = df['Sales_Minimum']
    e = df['Sales_Maximum']
    f = df['Mean_Sales']
    x = df['Total_Games']

    fig, ax = plt.subplots(figsize=(6, 3.84))

    df.plot(x = 'Year', y = 'Total_Sales', kind = "scatter", ax = ax )
    ax.set_facecolor('w')
    ax.set_title('Scatter Year and Total Sales')

    for ax, color in zip([ax, ax, ax, ax], ['black', 'black', 'black', 'black']):
        plt.setp(ax.spines.values(), color=color)
        plt.setp([ax.get_xticklines(), ax.get_yticklines()], color=color)

    plt.savefig('../imgs/Scatter_Year_and Total_Sales.png')


    corr_test = pearsonr(x = df['Year'], y =  df['Total_Sales'])
    print("Coeficiente de correlación de Pearson: ", corr_test[0])
    print("P-value: ", corr_test[1])

    X = df[['Year']] 
    y = df['Total_Sales']

    X_train, X_test, y_train, y_test = train_test_split(
                                            X.values.reshape(-1,1),
                                            y.values.reshape(-1,1),
                                            train_size   = 0.8,
                                            random_state = 1234,
                                            shuffle      = True
                                        )
    modelo = LinearRegression()
    modelo.fit(X = X_train.reshape(-1, 1), y = y_train)

    print("Intercept:", modelo.intercept_)
    print("Coeficiente:", list(zip(X.columns, modelo.coef_.flatten(), )))
    print("Coeficiente de determinación R^2:", modelo.score(X, y))

    predicciones = modelo.predict(X = X_test)
    print(predicciones[0:3,])

    rmse = mean_squared_error(
            y_true  = y_test,
            y_pred  = predicciones,
            squared = False
        )
    print("")
    print(f"El error (rmse) de test es: {rmse}")

    X = df[['Year']] 
    y = df['Total_Sales']

    X_train, X_test, y_train, y_test = train_test_split(
                                            X.values.reshape(-1,1),
                                            y.values.reshape(-1,1),
                                            train_size   = 0.8,
                                            random_state = 1234,
                                            shuffle      = True
                                        )

    X_train = sm.add_constant(X_train, prepend=True)
    modelo = sm.OLS(endog=y_train, exog=X_train,)
    modelo = modelo.fit()
    print(modelo.summary())

    modelo.conf_int(alpha=0.05)

    predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
    predicciones['x'] = X_train[:, 1]
    predicciones['y'] = y_train
    predicciones = predicciones.sort_values('x')

    fig, ax = plt.subplots(figsize=(6, 3.84))

    ax.scatter(predicciones['x'], predicciones['y'], marker='o', color = "#557AC2")
    ax.plot(predicciones['x'], predicciones["mean"], label="OLS", color='#FF0000')
    ax.plot(predicciones['x'], predicciones["mean_ci_lower"], color='#FFA600', label="95% CI")
    ax.plot(predicciones['x'], predicciones["mean_ci_upper"], color='#FFA600')
    ax.fill_between(predicciones['x'], predicciones["mean_ci_lower"], predicciones["mean_ci_upper"], alpha=0.1)

    for ax, color in zip([ax, ax, ax, ax], ['black', 'black', 'black', 'black']):
        plt.setp(ax.spines.values(), color=color)
        plt.setp([ax.get_xticklines(), ax.get_yticklines()], color=color)

    ax.set_facecolor('w')
    plt.title('Forecasting Year and Total Sales')
    plt.xlabel('Year')
    plt.ylabel('Total Sales')
    ax.legend()
    plt.savefig('../imgs/Forecasting_Year_and Total_Sales.png')


if __name__ == "__main__":
    df = pd.read_csv("../csv/video_games_sales_clean_analysis.csv")
    Forecasting(df)