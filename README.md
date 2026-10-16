Proyecto de consulta API

Descripción del Proyecto:

el objetivo de este proyecto es realizar consultas mediante una conexion API a la pagina Alphavantage, la cual otorga informacion sobre el precio de las acciones del mercado de valores

1. Conectando a la API:

    para hacer uso de la API, se necesita una KEY, la cual se te otorga cuando se registra en la pagina oficial de alphavantage, se uso la libreria Requests para las solicitudes HTML y Pandas para convertir la informacion a Dataframe

2. Funciones:

    para simplificar la ejecucion del codigo se separo cada horizonte de tiempo en 3 funciones distintas, las cuales iteran sobre los ETF's guardados dentro de una variable definida.

3. Filtros y graficos:

    se usaron como ejemplo 3 ETF's con 3 horizontes distintos, diario, semanal y mensual, los cuales se graficaron usando matplotlib y guardandolo como png