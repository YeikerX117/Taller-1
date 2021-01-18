#Taller filtro de datos
import pandas as pd
import dateutil
#Punto uno
data=pd.read_csv("E:\INGENIERIA DE SISTEMAS\Ciencia de datos\Taller\phone_data.csv")

#Item de mayor llamado
data["duration"].max() #10528 mayor duracion
#Falta terminar el punto número dos

#Llamada de mayor duración
data['duration'][data['item'] == 'call'].max() #10528.0
#Datos de mayotr duración
data['duration'][data['item'] == 'data'].max() #34429

#Punto tres
#Segundos total de llamadas
data['duration'][data['item'] == 'call'].sum() # 92321
#segundos entre sms
data['duration'][data['item'] == 'sms'].sum() #292
#segundos entre datos
data['duration'][data['item'] == 'data'].sum() #5164.35

#Entrada por cada mes
data['month'].value_counts()
#entreda por cada red
data['network'].value_counts()
#entrada por llamada
data['network'][data['item'] == 'call'].value_counts()

#Suma de duracion por mes
data.groupby('month')['duration'].sum()
#promedio de cada una de las llamdas por red
data.groupby('network')['duration'].mean()
#promedio de evento de datos por cada una de las redes 
############data.groupby('network')[data['network'] == 'data'].mean() #terminar

#número de entradas por mes 
data.groupby('month')['date'].count()
#número de entradas tipo llamada por cada una de las redes
data.groupby(['network', data['item'] == 'call'])['date'].count()
#número de entradas tipo sms por cada una de las redes
data.groupby(['network', data['item'] == 'sms'])['date'].count()

#Cuántos eventos de llamada, datos y sms hubo por mes
data.groupby(['month', 'item'])['date'].count()
#Por cada uno de los meses cuántas veces se usaron cada una de las redes
data.groupby(['month', 'network'])['date'].count()
#Por cada uno de los meses cuántas veces se usaron cada una de las redes
#discriminando el tipo de evento
data.groupby(['month', 'item', 'network'])['date'].count()
data.groupby(['month', 'network'])['date'].count()
