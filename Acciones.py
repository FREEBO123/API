import requests
import pandas as pd
import matplotlib.pyplot as plt

etf_conservador = ["VOO","AGG","SPY"]

def apiMonth(perfil):
    for n in perfil:
        # Endpoint de la API
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={n}&apikey="

        # Hacer la solicitud GET
        response = requests.get(url)

        # Comprobar si la solicitud fue exitosa
        if response.status_code == 200:
            data = response.json()  # Convertir la respuesta a JSON

        df = pd.DataFrame.from_dict(data['Monthly Time Series'],orient='index')

        df.columns = ["Open","High","Low","Close","Volume"]
        df.reset_index(inplace=True)
        df.rename(columns={"index":"Time"},inplace=True)

        df["Time"] = pd.to_datetime(df["Time"])

        #filtro
        #fecha_actual = df["Time"].max()
        #lastyear = fecha_actual - pd.Timedelta(days=365)
        #df = df[(df["Time"]>=lastyear)&(df["Time"]<=fecha_actual)]

        for col in ["Open","High","Low","Close","Volume"]:
            df[col]=df[col].astype(float)

        plt.figure(figsize=(10,6))

        plt.plot(df["Time"],df["Open"], label="Open")
        plt.plot(df["Time"],df["High"], label="High")
        plt.plot(df["Time"],df["Low"], label="Low")
        plt.plot(df["Time"],df["Close"], label="Close")

        plt.title(f"precios acciones {n}")
        plt.xlabel("tiempo")
        plt.xticks(rotation=45)
        plt.ylabel("precio")
        plt.legend()
        plt.grid()
        plt.tight_layout()

        plt.savefig(f'Grafico_Mensual_{n}.png', dpi=300, bbox_inches='tight')
        plt.close()

def apiDia(perfil):

    for n in perfil:
        # Endpoint de la API
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={n}&interval=30min&apikey="

        #convertir a json
        response = requests.get(url)
        data = response.json()

        #pivotar
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'],orient='index')
        #for columna in df.columns:
            #print(f"{columna}")------------>para ver solo los encabezados (si esque lo necesitas)

        #cambiar los titulos de las columnas
        df.columns = ["Open","High","Low","Close","Volume"]
        df.reset_index(inplace=True)
        df.rename(columns={"index":"Time"},inplace=True)

        #convertir a tiempo
        df["Time"] = pd.to_datetime(df["Time"])

        #filtro
        fecha_actual = df["Time"].max()
        lastyear = fecha_actual - pd.Timedelta(days=30)
        df = df[(df["Time"]>=lastyear)&(df["Time"]<=fecha_actual)]

        #convertir de string a float
        for col in ["Open","High","Low","Close","Volume"]:
            df[col]=df[col].astype(float)

        #graficar
        plt.figure(figsize=(10,6))

        plt.plot(df["Time"],df["Open"], label="Open")
        plt.plot(df["Time"],df["High"], label="High")
        plt.plot(df["Time"],df["Low"], label="Low")
        plt.plot(df["Time"],df["Close"], label="Close")

        plt.title(f"precios acciones {n}")
        plt.xlabel("tiempo")
        plt.xticks(rotation=45)
        plt.ylabel("precio")
        plt.legend()
        plt.grid()
        plt.tight_layout()

        plt.savefig(f'Grafico_Diario_{n}.png', dpi=300, bbox_inches='tight')
        plt.close()

def apiWeek(perfil):
    for n in perfil:
        # Endpoint de la API
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={n}&apikey="

        #convertir a json
        response = requests.get(url)
        data = response.json()

        #pivotar
        df = pd.DataFrame.from_dict(data['Weekly Time Series'],orient='index')
        #for columna in df.columns:
            #print(f"{columna}")------------>para ver solo los encabezados (si esque lo necesitas)

        #cambiar los titulos de las columnas
        df.columns = ["Open","High","Low","Close","Volume"]
        df.reset_index(inplace=True)
        df.rename(columns={"index":"Time"},inplace=True)

        #convertir a tiempo
        df["Time"] = pd.to_datetime(df["Time"])

        #filtro
        fecha_actual = df["Time"].max()
        lastyear = fecha_actual - pd.Timedelta(days=365)
        df = df[(df["Time"]>=lastyear)&(df["Time"]<=fecha_actual)]

        #convertir de string a float
        for col in ["Open","High","Low","Close","Volume"]:
            df[col]=df[col].astype(float)

        #graficar
        plt.figure(figsize=(10,6))

        plt.plot(df["Time"],df["Open"], label="Open")
        plt.plot(df["Time"],df["High"], label="High")
        plt.plot(df["Time"],df["Low"], label="Low")
        plt.plot(df["Time"],df["Close"], label="Close")

        plt.title(f"precios acciones {n}")
        plt.xlabel("tiempo")
        plt.xticks(rotation=45)
        plt.ylabel("precio")
        plt.legend()
        plt.grid()
        plt.tight_layout()

        plt.savefig(f'Grafico_Semanal_{n}.png', dpi=300, bbox_inches='tight')
        plt.close()

apiWeek(etf_conservador)
apiDia(etf_conservador)
apiMonth(etf_conservador)
