
from xml.dom import registerDOMImplementation
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from dateutil import parser
import requests
from datetime import date  
from datetime import datetime
import pathlib  
import os
import json
import time as ti
from functools import reduce
from datetime import timedelta
from datetime import time
import pytz

newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
print("The current time in New York is:", timeInNewYork)##currentTimeInNewYork)
##print("Esta version tiene señuelo para bolsausa")

d =date.today()
# d es la fecha de hoy que se le aplica la hora de New York

dos = datetime(d.year, d.month, d.day, hour=8, minute=30, tzinfo=newYorkTz,  fold=0)
##if timeInNewYork.hour==9:
    ##print ("tiene  buena pinta")
    ##dos = datetime(d.year, d.month, d.day, timeInNewYork.hour-1, minute=30, tzinfo=newYorkTz,  fold=0)

##if timeInNewYork.hour==10:
    ##print ("tiene  buena pinta")
    ##dos = datetime(d.year, d.month, d.day, timeInNewYork.hour-2, minute=30, tzinfo=newYorkTz,  fold=0)


print("hora comienzo new york",dos)
tiempooperacionnewyork = timeInNewYork  > dos ## horacomienzonewyork ####es >, < es para pruebas

##else:
    ##print("la hora corriente en new york es ", timeInNewYork.hour)

print("La hora de comienzo de New York es ",dos)
horacomienzonewyork = dos

print ("comparacion tiempo new york > horacomienzonewyork ",tiempooperacionnewyork)


diahoy = date.today().isoformat()
momentohoy = str(datetime.now())
numdiasemana=date.fromisoformat(diahoy).isoweekday() #del 1 lunes a 7 domingo

sabadoodomingo = False ##date.fromisoformat(diahoy).isoweekday()>5 ##>5

#print(numdiasemana)
#print(momentohoy)

df = pd.DataFrame()
df1 = pd.DataFrame()
dfcotiz_dacci = pd.DataFrame()
datos_resumen_fon ={} ##datos resumen del fondo
clave_unica=""
datosaccenelfondo={}
cotiz_dacci ={}
diccotiz={}
dictfondos= {}
dictacciones={} #numero de acciones fondo
dicfontic={} 
#acciones keys, y fondos values
coberturaFondo={} #participación del fondo en una acción
indicebolsafontic=""
bolsafontic={}
tickersunicos={}
fondossinorden={}
cotizaaccion=[]
fonvariacion={}
dicaccfon={} ##fondos con sus acciones
listatodosdatosaccenelfondo=[]
cadenalinealistadohistoricobak=''
txtlistadohistoricobak=[] #para escribir el historictickersocotiza.csv
itemhistorico=[]          #para hacer y tratar con python graficas
contador = 0
fonvariacion={}

data=[["Senuelo",0.0, 0.0]]  
dfcot_ac = pd.DataFrame(data, columns=["ticker","precio","por_var"])###ticker"])
dffinal = pd.DataFrame(data, columns=["ticker","precio", "por_var"])




archivonombresfondos ='/home/jose/Fondos/Auxiliares/nombreFondos_prueba.csv'
archivotickers ='/home/jose/Fondos/Auxiliares/tickers.csv'
rhcsv = '/home/jose/Fondos/Auxiliares/resumenhistoricocsv_prueba.csv'
cotizahoypython='/home/jose/Fondos/Auxiliares/cotizahoypy_prueba.csv'
resucsv ='/home/jose/Fondos/Auxiliares/resumencsv_prueba.csv'
tikercsv = '/home/jose/Fondos/Auxiliares/tikercsv_prueba.csv'

##cotizahoypython='C://Auxiliares/cotizahoypy.csv'from
archivonombresfondos ='C:\\Auxiliares\\nombreFondos.csv'
archivotickers ='C:\\Auxiliares\\tickers.csv'
rhcsv = 'C:\\Auxiliares\\resumenhistoricocsv.csv'
cotizahoypython='C:\\Auxiliares\\cotizahoypy.csv'
resucsv ='C:\\Auxiliares\\resumencsv.csv'
tikercsv = 'C:\\Auxiliares\\tikercsv.csv'
muestramerge = 'C:\\Auxiliares\\muestramerge.csv'

resumencsv_inner_detallado = "c:/Auxiliares/resumencsv_inner_detallado.csv"
resumencsv= "c:/Auxiliares/resumencsv.csv"

'''
archivonombresfondos ='nombreFondos.csv'
archivotickers ='tickers.csv'
rhcsv = 'resumenhistoricocsv.csv'
cotizahoypython='cotizahoypy.csv'
resucsv ='resumencsv.csv'
tikercsv = 'tikercsv.csv'
muestramerge = 'muestramerge.csv'

resumencsv_inner_detallado = "resumencsv_inner_detallado.csv"
resumencsv= "resumencsv.csv"
'''
class cuerpo():

        fecha_actual_formateada = None
        momento_actual_formateada = None

        def __init__(self):
        
                self.fecha_actual_formateada   = datetime.now().strftime("%d-%m-%Y")
                self.momento_actual_formateada = datetime.now().strftime("%H:%M:%S")     
        



        def mostrar(self):

                df_inner_detallados = pd.read_csv(resumencsv_inner_detallado,header = 0, index_col =0, sep=';',decimal='.', encoding='ISO-8859-1')
                print(df_inner_detallados)

                print(df_inner_detallados.columns)
                input("linea 134")
        
        

                ##df_inner_detallados.columns = ["fondo","Idorden",'accion','ticker','porcentaje', 'mes', 'a??o', 'precio', 'por_var', 'reperc_fondo', 'menos2_5', 'menos1_5', 'mas1_5']      

                #input("linea 239 df_inner_detallados")
                ######df_inner_detallados['por_var'] = df_inner_detallados['por_var'].str.replace('%','')
                ##calcular un dataframe que sume los valores de cada campo por fondo
                fondos = pd.Series(df_inner_detallados['fondo'].unique()) 
                print("linea 241 fondos")
                print(fondos)



                n_fondos = len(fondos)  
                fecha = str(self.fecha_actual_formateada)
                print("linea 196")  
                print(fecha)
                serie_fecha = pd.Series([fecha]*n_fondos)
                df_serie_fecha = pd.DataFrame(serie_fecha)

                df_fondos = pd.DataFrame(fondos, columns=['fondo']) 
                print("linea 246 df_fondos")
                print(df_fondos)

                df_suma_reperc_por_fondo = pd.DataFrame(pd.Series( df_inner_detallados.groupby('fondo')['reperc_fondo'].sum()), columns=['reperc_fondo'])
                print("linea 250 df_suma_reperc_por_fondo" )
                print(df_suma_reperc_por_fondo)
                serie_suma_reperc_por_fondo = pd.Series(df_suma_reperc_por_fondo['reperc_fondo'].tolist())
                print("linea 253 serie_suma_reperc_por_fondo")
                print(serie_suma_reperc_por_fondo)

                #input("linea 256" )
                df_suma_porcentaje_por_fondo   =pd.DataFrame(pd.Series(df_inner_detallados.groupby('fondo')['porcentaje'].sum()), columns=['porcentaje'])
                print("linea 258 df_suma_porcentaje_por_fondo")
                print(df_suma_porcentaje_por_fondo) 
                serie_suma_porcentaje_por_fondo = pd.Series(df_suma_porcentaje_por_fondo['porcentaje'].tolist()) 
                print("linea 223 serie_suma_porcentaje_por_fondo")
                print(serie_suma_porcentaje_por_fondo)

                #input("linea 264 df_n_tickers_por_fondo")    
                ##calcular el número de tickers por fondo
                df_n_tickers_por_fondo = pd.DataFrame(df_inner_detallados)
                n_tickers_por_fondo = df_n_tickers_por_fondo.groupby('fondo')['ticker'].count().reset_index()
                print("linea 268 n_tickers_por_fondo")
                print(n_tickers_por_fondo)
                print("linea 270")  
                serie_n_tickers_por_fondo = pd.Series(n_tickers_por_fondo['ticker'].tolist())
                print("linea 272 serie_n_tickers_por_fondo")
                print(serie_n_tickers_por_fondo)

                #input("linea 76" )
                df_suma_porcentaje_por_fondo   =pd.DataFrame(pd.Series(df_inner_detallados.groupby('fondo')['porcentaje'].sum()), columns=['porcentaje'])
                print("linea 258 df_suma_porcentaje_por_fondo")
                print(df_suma_porcentaje_por_fondo) 


                print("linea 81 cuenta de n trues de menos2_5")
                trues_menos2_5 = df_inner_detallados[(df_inner_detallados['menos2_5']==True) ].groupby('fondo')['menos2_5'].size()
                print(trues_menos2_5)
                
                #input( " ***linea 84 n trues -2.5 por fondo")

                print(" linea 87  cuenta % trues de -1.5")
                trues_menos1_5 = df_inner_detallados[(df_inner_detallados['menos1_5']==True) ].groupby('fondo')['menos1_5'].size() 
                print(trues_menos1_5)
                
                #input( " ***linea 84 n trues -1.5 por fondo")

                print(" linea 87  cuenta  n trues de +1.5")
                trues_mas1_5 = df_inner_detallados[(df_inner_detallados['mas1_5']==True) ].groupby('fondo')['mas1_5'].size()
                print(trues_mas1_5)
                
                #input( " ***linea 84 n trues 1.5 por fondo")




               
                npor_var = df_inner_detallados['por_var'].astype(float)
                        
                print("linea 207 npor_var")
                print(npor_var) 
                print("linea 209")
                menos2_5 = [number <(-0.025) for number in npor_var]
                menos1_5 = [number <(-0.015) for number in npor_var]
                mas1_5 =   [number >(0.015) for number in npor_var]

                int_menos2_5 = pd.Series(menos2_5)
                int_menos1_5 = pd.Series(menos1_5)  
                int_mas1_5   = pd.Series(mas1_5)  

                print("linea 214 menos2_5: ")
                print(menos2_5)
                print("linea 215 menos1_5")
                print(menos1_5) 
                print("linea 217 mas1_5")  
                print(mas1_5)   
                #input("linea 219") 
                df_menos2_5 = pd.DataFrame(int_menos2_5, columns=["menos2_5"])
                df_menos1_5 = pd.DataFrame(int_menos1_5, columns=["menos1_5"])
                df_mas1_5 = pd.DataFrame(int_mas1_5, columns=["mas1_5"]) 
                print("linea 100 df_menos2_5")
                print(df_menos2_5)
                print("linea 102 df_menos1_5")
                print(df_menos1_5)
                print("linea 104 df_mas1_5")
                print(df_mas1_5)

                serie_fecha = pd.Series([self.fecha_actual_formateada]*len(fondos))
                serie_momento = pd.Series([self.momento_actual_formateada]*len(fondos))



                # mezclar df_fondos con los otros dataframes
                df_resumencsv = pd.DataFrame()
                df_resumencsv['fecha'] = serie_fecha
                print("linea 308")
                print(df_resumencsv['fecha'])    
                df_resumencsv['fondo'] = df_fondos['fondo']
                print("linea 311")
                print(df_resumencsv['fondo'])
                df_resumencsv['var_fon'] = serie_suma_reperc_por_fondo  
                print("linea 314")
                print(df_resumencsv['var_fon'])
                df_resumencsv['peso_fon'] = serie_suma_porcentaje_por_fondo
                print("linea 317")
                print(df_resumencsv['peso_fon'])
                df_resumencsv['n_tickers'] = serie_n_tickers_por_fondo
                print("linea 320")
                print(df_resumencsv['n_tickers'])
                df_resumencsv["momento"] = serie_momento
                print("linea 323")
                print(df_resumencsv['momento'])
                df_resumencsv['Fondo'] = df_fondos['fondo']
                print("linea 326")
                print(df_resumencsv['Fondo'])
                df_resumencsv['menos2_5'] = pd.merge(df_resumencsv,trues_menos2_5, on='fondo', how= 'left')['menos2_5']  
                print(df_resumencsv['menos2_5'])
                df_resumencsv['menos1_5'] = (pd.merge(df_resumencsv,trues_menos1_5, on='fondo', how='left'))['menos1_5']
                print("linea 332")
                print(df_resumencsv['menos1_5'])
                df_resumencsv['mas1_5'] =   (pd.merge(df_resumencsv,trues_mas1_5, on='fondo', how='left'))['mas1_5']
                print("linea 335")
                print(df_resumencsv['mas1_5'])
                df_resumencsv['porc_menos2_5'] = round( df_resumencsv['menos2_5']/df_resumencsv['n_tickers'],2)
                print(df_resumencsv['porc_menos2_5'])
                df_resumencsv['porc_menos1_5'] = round(df_resumencsv['menos1_5']/df_resumencsv['n_tickers'],2)
                print("linea 332")
                print(df_resumencsv['porc_menos1_5'])
                df_resumencsv['porc_mas1_5'] =   round(df_resumencsv['mas1_5']/df_resumencsv['n_tickers'],2)
                print("linea 335")
                print(df_resumencsv['porc_mas1_5'])

                print("linea 179 resultado final")

                print(df_resumencsv)    
                df_resumencsv.to_csv(resumencsv_inner_detallado, sep=';', decimal='.', index=False)  
                df_resumencsv.to_csv(resumencsv, sep=';', decimal='.', index=False, mode='a', header=False)          
                #añadir 
                input()

class datosprecedentes():
        
        def mostrardatosanteriores(self):
             
            ultimoresumencsv = pd.read_csv(resumencsv, header = 0, index_col =0, sep=';',decimal='.', encoding='ISO-8859-1')
            print(ultimoresumencsv)
            input("linea 301")
        
        def mostrardetalledatosanteriores(self):
             
            tickercsvdatos = pd.read_csv(tikercsv, header = 0, index_col =0, sep=';',decimal='.', encoding='ISO-8859-1')
            print(tickercsvdatos.columns)
            fondos = pd.Series(tickercsvdatos['fondo'].unique())
            print(fondos)    

            fondoelegido = input("¿De que fondo quiere los datos? FIN para finalizar").upper()
            while fondoelegido != "FIN":
                while fondoelegido not in fondos & fondoelegido != "FIN":
                    print("El fondo no existe")
                    fondoelegido = input("¿De que fondo quiere los datos?").upper() 
                
                fondoelegido = input("¿De que fondo quiere los datos? FIN para finalizar").upper()
                print(tickercsvdatos[tickercsvdatos['fondo']==fondoelegido])
                input("linea 308")

            







class construirtickercvs():

    data=[["Senuelo",0.0, 0.0]]  
    dfcot_ac = pd.DataFrame(data, columns=["ticker","precio","por_var"])
    dffinal = pd.DataFrame(data, columns=["ticker","precio", "por_var"])

    def fecha_actual_formateada(self):
        return datetime.now().strftime("%d-%m-%Y")
    
    def momento_actual_formateada(self):
        return datetime.now().strftime("%H:%M:%S")     
    
    def decirtickersunicos(self):
        dfprovisional= pd.read_csv(archivotickers, header = 0, index_col =1, sep=';',decimal='.', encoding='ISO-8859-1')
        print(dfprovisional.columns)
        df = dfprovisional.ticker
        print(df)
        tickersunicos= dfprovisional['ticker'].unique().tolist()
        print(tickersunicos)
        print("linea 128")
        datfo= datos_fon()
       
        
        contador = 1
        for dacci in tickersunicos:
           print(dacci)
           print("linea 135 contador ",contador)
           contador +=1
           if contador%60== 0:
               ti.sleep(10) 
           dfcot_ac = datfo.cot_acc(dacci)
           
           ##print(dfcot_ac)
           ##print ("longitud de dataframe ", len(dffinal))
           ##xdf = len(dffinal)  
           ##print( "linea 118 ",xdf)  
           ## añadimos lineas al dataframe dffinal
           self.dffinal = pd.concat([self.dffinal,dfcot_ac], ignore_index= False)
           ## dfcot_acc = pd.DataFrame(dacci,marketPriceArmp,changePercentA)
        print("linea 148")
        print(self.dffinal)
        df_inner = pd.merge(dfprovisional, self.dffinal,  on='ticker', how='inner')
        print("linea 151")
        print(df_inner) 
        print("linea 153")
        #input("linea 154    ")
        print(df_inner[["accIon"]])
        print("linea 147")
        print(df_inner["porcentaje"].astype(float)) 
        porcentaje = df_inner["porcentaje"].astype(float) 
        por_var = df_inner["por_var"].astype(float)
        df_variacion_accion = pd.DataFrame(pd.Series(porcentaje * por_var), columns=["reperc_fondo"])
        print("linea 149")      
        print(df_variacion_accion)
        print("linea 151")
        #añadir  la lista variación_accion al dataframe df_inner
        df_inner_detallados= pd.DataFrame(df_inner)
        df_inner_detallados['reperc_fondo'] =  df_variacion_accion
        df_inner_detallados.columns = ["Idorden", 'fondo', 'accion','ticker','porcentaje', 'mes', 'a??o', 'precio', 'por_var', 'reperc_fondo'] 
        print("linea 157 df_inner_detallados")
        print(df_inner_detallados)
        #input("linea 159")

        dfid= pd.DataFrame(df_inner_detallados)
        dtcsv = pd.DataFrame()                  
        ## construimos tickercsv.csv con dtcsv
        n_casos = len(df_inner_detallados)
        fecha = str(self.fecha_actual_formateada())
        print("linea 173")  
        print(fecha)
        serie_fecha_dtcsv = pd.Series([fecha]*n_casos)

        #input("linea 181 serie_fecha_dtcsv")

        print("linea 183")
        dtcsv['Fecha'] = serie_fecha_dtcsv
        dtcsv['Fondo'] = dfid['fondo']
        dtcsv['Ticker'] = dfid['ticker']
        dtcsv['Accion'] = dfid['accion']
        dtcsv['Porcentaje'] = dfid['porcentaje']    
        dtcsv['Modif_porc'] = dfid['por_var'] 
        dtcsv['Peso_absoluto'] = dfid['reperc_fondo']
        dtcsv['Precio'] = dfid['precio']    
        dtcsv['Banco'] = pd.Series(['IBERCAJA']*n_casos)
        dtcsv['CNMV'] = pd.Series(['NOSE']*n_casos) 

        print("linea 189")
        print(dtcsv)    
        dtcsv.to_csv(tikercsv, sep=';', decimal='.', index=False)         
        #input("linea 198 tickercsv.csv")
        # Lista de DataFrames a combinar
      

        # Usar reduce para hacer merge de todos los DataFrames en la lista
        #df_inner_detallados = reduce(lambda left, right: pd.merge(left, right, on ='fondo'), dataframes)

        npor_var = df_inner['por_var'].astype(float)
        
        print("linea 207 npor_var")
        print(npor_var) 
        print("linea 209")
        menos2_5 = [number <(-0.025) for number in npor_var]
        menos1_5 = [number <(-0.015) for number in npor_var]
        mas1_5 =   [number >(0.015) for number in npor_var]

        int_menos2_5 = menos2_5
        int_menos1_5 = menos1_5  
        int_mas1_5 = mas1_5  

        print("linea 214 menos2_5: ")
        print(menos2_5)
        print("linea 215 menos1_5")
        print(menos1_5) 
        print("linea 217 mas1_5")  
        print(mas1_5)   
        #input("linea 219") 
        '''
        df_menos2_5 = pd.DataFrame([int_menos2_5], columns=["menos2_5"])
        df_menos1_5 = pd.DataFrame([int_menos1_5], columns=["menos1_5"])
        df_mas1_5 = pd.DataFrame ([int_mas1_5], columns=["mas1_5"]) 
        print(df_menos2_5)
        print(df_menos1_5)  
        print(df_mas1_5)
        '''
        ## solo se puede hacer merge con dos df df_inner_detallados = pd.merge(df_inner_detallados, df_menos2_5, df_menos1_5, df_mas1_5, on='fondo', how = 'inner')
        print("linea 224")
        #mezclar los DataFrames
        df_inner_detallados['menos2_5'] = pd.Series(menos2_5)
        df_inner_detallados['menos1_5'] = pd.Series(menos1_5)
        df_inner_detallados['mas1_5']   = pd.Series(mas1_5) 
        print("linea 238")
        print(df_inner_detallados)   
        print("linea 240")
        # Lista de DataFrames a combinar
        ##dataframes = [df_inner_detallados, df_menos2_5, df_menos1_5, df_mas1_5]

        # Usar reduce para hacer merge de todos los DataFrames en la lista
        #df_inner_detallados = reduce(lambda left, right: pd.merge(left, right, on ='fondo'), dataframes)

        df_inner_detallados.columns = ["Idorden", 'fondo', 'accion','ticker','porcentaje', 'mes', 'a??o', 'precio', 'por_var', 'reperc_fondo', 'menos2_5', 'menos1_5', 'mas1_5']      
        print("linea 237 df_inner_detallados")  
        print(df_inner_detallados)
        df_inner_detallados.to_csv("C:/Auxiliares/df_inner_detallados.csv", sep=';', decimal='.', index=False)
        print("linea 239 df_inner_detallados convertido en fichero csv")
        
        #input("linea 240 df_inner_detallados")
        ##calcular un dataframe que sume los valores de cada campo por fondo
        fondos = pd.Series(df_inner_detallados['fondo'].unique()) 
        print("linea 241 fondos")
        print(fondos)

        df_fondos = pd.DataFrame(pd.Series(df_inner_detallados['fondo'].unique()), columns=['fondo']) 
        print("linea 246 df_fondos")
        print(df_fondos)

        df_suma_reperc_por_fondo = pd.DataFrame(pd.Series( df_inner_detallados.groupby('fondo')['reperc_fondo'].sum()), columns=['reperc_fondo'])
        print("linea 250 df_suma_reperc_por_fondo" )
        print(df_suma_reperc_por_fondo)
        serie_suma_reperc_por_fondo = pd.Series(df_suma_reperc_por_fondo['reperc_fondo'].tolist())
        print("linea 253 serie_suma_reperc_por_fondo")
        print(serie_suma_reperc_por_fondo)
        
        #input("linea 256" )
        df_suma_porcentaje_por_fondo   =pd.DataFrame(pd.Series(df_inner_detallados.groupby('fondo')['porcentaje'].sum()), columns=['porcentaje'])
        print("linea 258 df_suma_porcentaje_por_fondo")
        print(df_suma_porcentaje_por_fondo) 
        serie_suma_porcentaje_por_fondo = pd.Series(df_suma_porcentaje_por_fondo['porcentaje'].tolist()) 
        print("linea 223 serie_suma_porcentaje_por_fondo")
        print(serie_suma_porcentaje_por_fondo)

        #input("linea 264 df_n_tickers_por_fondo")    
        ##calcular el número de tickers por fondo
        df_n_tickers_por_fondo = pd.DataFrame(df_inner_detallados)
        n_tickers_por_fondo = df_n_tickers_por_fondo.groupby('fondo')['ticker'].count().reset_index()
        print("linea 268 n_tickers_por_fondo")
        print(n_tickers_por_fondo)
        print("linea 270")  
        serie_n_tickers_por_fondo = pd.Series(n_tickers_por_fondo['ticker'].tolist())
        print("linea 272 serie_n_tickers_por_fondo")
        print(serie_n_tickers_por_fondo)
       
        #input("linea 275 casos positivos y totales menos2_5")
        casos_positivos = 0
        casos_totales = 0
        condicion_menos2_5 = pd.DataFrame()
        df_menos2_5 = pd.DataFrame()
        for fondo in df_inner_detallados['fondo'].unique():
            for n_true in df_inner_detallados["menos2_5"]:
                #print("linea 279")
                if (n_true == True):## & (fondo == df_inner_detallados['fondo'].item):
                   casos_positivos += 1
                casos_totales += 1
                fondo   =  fondo ## df_inner_detallados['fondo']
                porc_menos2_5 =  casos_positivos/casos_totales
                df_condicion_menos2_5 = pd.DataFrame([[fondo,porc_menos2_5]], columns=['fondo', 'menos2_5'])
            
            print("linea 290 print df_condicion_menos2_5")
            print(df_condicion_menos2_5)
            df_menos2_5 = pd.concat([df_menos2_5, df_condicion_menos2_5])
            df_condicion_menos2_5 = pd.DataFrame()
            print("linea 294 print df_menos2_5 por fondo ", fondo)  
            print(df_menos2_5)
            casos_positivos = 0
            casos_totales = 0
        print("linea 259 print df_menos2_5 totales")
        print(df_menos2_5)  
        serie_df_menos2_5 = pd.Series(df_menos2_5['menos2_5'].tolist())
        
        #input("linea 298 casos positivos y totales menos1_5")
        casos_positivos = 0
        casos_totales = 0
        condicion_menos1_5 = pd.DataFrame()
        df_menos1_5 = pd.DataFrame()
        for fondo in df_inner_detallados['fondo'].unique():
            for n_true in df_inner_detallados["menos1_5"]:
                if (n_true == True):## & (fondo == df_inner_detallados['fondo'].item()):
                   casos_positivos += 1
                casos_totales += 1
                fondo   =   fondo
                porc_menos1_5=   casos_positivos/casos_totales 
                df_condicion_menos1_5 = pd.DataFrame([[fondo,porc_menos1_5]], columns=['fondo', 'menos1_5'])
            df_menos1_5 = pd.concat([df_menos1_5, df_condicion_menos1_5])
            df_condicion_menos1_5 = pd.DataFrame()
            print("linea 270 df_menos1_5 por fondo ", fondo)
            print(df_menos1_5)
            casos_positivos = 0
            casos_totales = 0
        print("linea 280 df_menos1_5 totales")
        print(df_menos1_5)
        serie_df_menos1_5 = pd.Series(df_menos1_5['menos1_5'].tolist())

        #input("linea 286 casos positivos y totales mas1_5")    
        casos_positivos = 0
        casos_totales = 0
        condicion_mas1_5 = pd.DataFrame()
        df_mas1_5 = pd.DataFrame(['fondo'], ['mas1_5'])
        for fondo in df_inner_detallados['fondo'].unique():
            for n_true in df_inner_detallados["mas1_5"]:
                if (n_true == True):## & (fondo == df_inner_detallados['fondo'].item()):
                   casos_positivos += 1
                casos_totales += 1
                fondo   =   fondo
                porc_mas1_5 =   casos_positivos/casos_totales
                df_condicion_mas1_5 = pd.DataFrame([[fondo,porc_mas1_5]], columns=['fondo', 'mas1_5'])
            df_mas1_5 = pd.concat([df_mas1_5, df_condicion_mas1_5]) 
            df_condicion_mas1_5 = pd.DataFrame()       
            print("linea 297 df_mas1_5 por fondo ", fondo)  
            print(df_mas1_5)
            casos_positivos = 0
            casos_totales = 0
        print("linea 301 df_mas1_5 totales")
        print(df_mas1_5)    
        serie_df_mas1_5 = pd.Series(df_mas1_5['mas1_5'].tolist())
             

        
        n_fondos = len(fondos)  
        fecha = str(self.fecha_actual_formateada())
        print("linea 196")  
        print(fecha)
        serie_fecha = pd.Series([fecha]*n_fondos)
        df_serie_fecha = pd.DataFrame(serie_fecha)
        
        ##añadir momento=   
        print("linea 199")  
        momento = str(self.momento_actual_formateada())
        print("linea 343 c momento")
        print(momento)
        serie_momento = pd.Series([momento]*n_fondos)
        df_serie_momento = pd.DataFrame(serie_momento)           
        print("linea 199")
        print(serie_momento)

        ##  df.loc[df['B'] > 6, 'A']
        
        # mezclar df_fondos con los otros dataframes
        df_resumencsv = pd.DataFrame()
        df_resumencsv['fecha'] = df_serie_fecha
        print("linea 308")
        print(df_resumencsv['fecha'])    
        df_resumencsv['fondo'] = df_fondos['fondo']
        print("linea 311")
        print(df_resumencsv['fondo'])
        df_resumencsv['var_fon'] = serie_suma_reperc_por_fondo  
        print("linea 314")
        print(df_resumencsv['var_fon'])
        df_resumencsv['peso_fon'] = serie_suma_porcentaje_por_fondo
        print("linea 317")
        print(df_resumencsv['peso_fon'])
        df_resumencsv['n_tickers'] = serie_n_tickers_por_fondo
        print("linea 320")
        print(df_resumencsv['n_tickers'])
        df_resumencsv["momento"] = df_serie_momento
        print("linea 323")
        print(df_resumencsv['momento'])
        df_resumencsv['Fondo'] = df_fondos['fondo']
        print("linea 326")
        print(df_resumencsv['Fondo'])
        df_resumencsv['menos2_5'] = (pd.merge(df_resumencsv,df_menos2_5, on='fondo', how='inner'))['menos2_5']
        print("linea 329")
        print(df_resumencsv['menos2_5'])
        df_resumencsv['menos1_5'] = (pd.merge(df_resumencsv,df_menos1_5, on='fondo', how='inner'))['menos1_5']
        print("linea 332")
        print(df_resumencsv['menos1_5'])
        df_resumencsv['mas1_5'] =   (pd.merge(df_resumencsv,df_mas1_5, on='fondo', how='inner'))['mas1_5']
        print("linea 335")
        print(df_resumencsv['mas1_5'])
      
        print(df_resumencsv)    
        df_resumencsv.to_csv(resucsv, sep=';', decimal='.', index=False)            
        #añadir 
        input()

        return tickersunicos
        
    def actualizar_resumenhistoricocsv(self):
         
        df_rhcsv = pd.read_csv(rhcsv, header = 0,  sep=';',decimal='.', encoding='ISO-8859-1')
        print("linea 350")
        print(df_rhcsv.tail(9))
        ##df_rhcsv.columns = ['fecha', 'fondo', 'var_fon', 'peso_fon', 'n_tickers', 'momento', 'Fondo', 'menos2_5', 'menos1_5', 'mas1_5']
        #df = df[df['A'] <= 10]
        print(df_rhcsv.columns)
        df_viejos = pd.DataFrame(df_rhcsv[df_rhcsv['fecha']<self.fecha_actual_formateada()])
        print("linea 354")
        df_resumencsv = pd.read_csv(resucsv, header = 0, sep=';',decimal='.', encoding='ISO-8859-1')
        print("linea 357")  
        print(df_resumencsv)
        print(df_viejos.tail( 25))
        print("linea 392")

        #juntados df_viejos y df_resumencsv
     
        df_renovadosrhcsv = pd.concat([df_viejos, df_resumencsv]  , ignore_index= False)
        print("linea 359") 
        print(df_renovadosrhcsv.tail(25))
        df_renovadosrhcsv.to_csv(rhcsv, sep=';', decimal='.', index=False) 








    def cabeceratikercsv(self):
        
        ##borrado de fichero
        hmt = open(tikercsv, 'w')
        cabecera = "Fecha;Fondo;Ticker;Accion;Porcentaje;Variacion;Peso;Precio;Banco;CNMV\n"
        ##print("CABECERA DE HISTORICO ",cabecera)
        hmt.write(cabecera)
        hmt.close()
    

    
    def cuerpotikercsv(self, dicfontic):

        ##cotiz_dacci[dacci]=[dacci,marketPriceArmp,changePercentA]
        hmc= open(tikercsv,'a')
        
        ##claveunicasorted = sorted(dicfontic.keys())

        for claveunica in dicfontic.keys(): ## debes esta el tickers.csv ordenado por fondos y porcentajes:
            
            if tiempooperacionnewyork ==False: ##True: ##False: ##False: 
                    #True: ##//no carga usa y descuajeringa Pru1ods
                    ##print("121")
                    if "^" in dicfontic[claveunica][2] or "." in claveunica:
                        tic =dicfontic[claveunica][4]
            ##print("133 ",tic)
                        part=float(dicfontic[claveunica][5])
                        ##print("135 ",part)
                        vari=float(cotiz_dacci[tic][2])

                        precio=float(cotiz_dacci[tic][1])
                        ##print("140 ",precio)
                        if  "ALPHA" not in claveunica:########and "BESTIDEAS" not in claveunica: ##### and "^" not in claveunica:
                            lineacuerpo = ""+str(datetime.now())+";"+dicfontic[claveunica][2]+";"+ dicfontic[claveunica][4]+";"+dicfontic[claveunica][3]+";"+dicfontic[claveunica][5]+";"+str(vari)+";"+str(vari*part)+";"+str(precio) +";"+"IBERCAJA"+";"+"NOSE"+"\n"
                            hmc.write(lineacuerpo)
                        ##print("linea 93 "+ lineacuerpo)
            
                                ### nueveymedia_list_dacci.append(dacci)
            else:
                ###print("125")

        ###set_dacci=set(list_dacci)

                tic =dicfontic[claveunica][4]
                ##print("133 ",tic)
                part=float(dicfontic[claveunica][5])
                ##print("135 ",part)
                vari=float(cotiz_dacci[tic][2])

                precio=float(cotiz_dacci[tic][1])
                ##print("140 ",precio)
                if  "ALPHA" not in claveunica:### and "BESTIDEAS" not in claveunica: ##### and "^" not in claveunica:
                    lineacuerpo = ""+str(datetime.now())+";"+dicfontic[claveunica][2]+";"+ dicfontic[claveunica][4]+";"+dicfontic[claveunica][3]+";"+dicfontic[claveunica][5]+";"+str(vari)+";"+str(vari*part)+";"+str(precio) +";"+"IBERCAJA"+";"+"NOSE"+"\n"
                    hmc.write(lineacuerpo)
                ##print("linea 93 "+ lineacuerpo)

        hmc.close()

class ver_comp():

    
    def ver_c(self): ##,ave):

        vercomposicion='BOLSAESPANA'

        
        while vercomposicion!='':

            vercomposicion= vercomposicion.upper()

            for fon in datos_fon.lista_fondos: ##dictaccfon: 

                if vercomposicion in fon:

                    n_acciones_fondo =0

                    lista_datos_fondo=[]

                    valorparticipaciones =0.0 

                    valorpesoglobal=0.0          


                    datos_fon.peso_acumulado=0.0

                    ####datos_fon.variacion_ponderada=0.0000
                    
                    n_acciones_fondo=0

                    n_acciones_fondo_menos_2_5 =  0

                    n_acciones_fondo_menos_1_5 =  0


                    print("Fondo analizado","\t\t", "Part.", "\t", "Var","\t", "Peso","\t","Acción","\t","Precio","\t","por -2.5","\t","por -1.5")

                    for daccikey in datos_fon.dicaccfoncl[fon]:

                        if tiempooperacionnewyork ==False: ##False: 
                #True: ##//no carga usa y descuajeringa Pru1ods
               
                            if "^" in fon or "." in daccikey: 

                                if vercomposicion in fon:

                                        n_acciones_fondo =n_acciones_fondo+1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")
                                        
                                        var_ac=round(cotiz_dacci[daccikey][2]*100,3)

                                       
                                        peso_var_ac=round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)
                                        precio =round(cotiz_dacci[daccikey][1],4)

                                        print(("{:}\t\t{:}\t{:5.3f}\t{:5.3f}\t{:10}\t{:7.4f}").format(fon,peso_accion_fondo, var_ac,peso_var_ac,cotiz_dacci[daccikey][0],precio))
                                        
                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),    3)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)                    
                        else:
                             if vercomposicion in fon:
    
                                        n_acciones_fondo =n_acciones_fondo+1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")
                                        
                                        var_ac=round(cotiz_dacci[daccikey][2]*100,3)
                                        peso_var_ac=round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)
                                        precio =round(cotiz_dacci[daccikey][1],4)

                                        print(("{:}\t\t{:}\t{:5.3f}\t{:5.3f}\t{:10}\t{:7.4f}").format(fon,peso_accion_fondo, var_ac,peso_var_ac,cotiz_dacci[daccikey][0],precio))
                                        
                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),    3)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,3)                    
                        
                        if var_ac < -2.5:
                                            n_acciones_fondo_menos_2_5 +=1

                        if var_ac < -1.5:
                                            n_
                                            acciones_fondo_menos_1_5 +=1
                                    

                    print("numero de acciones ", n_acciones_fondo, " peso de participaciones ",round(valorparticipaciones,2), " variacion global ",round(valorpesoglobal/100,4), " porc menor a 2.5 ", round( n_acciones_fondo_menos_2_5/n_acciones_fondo*100, 3)," porc menor a 1.5 ", round( n_acciones_fondo_menos_1_5/n_acciones_fondo*100,3) )   
 
            
            vercomposicion = input("Ver composicion del fondo =")



class mostrarchartfondo():

    fonvariacion={}

    '''
    def mcf(self):

        ##alprint ("linea 124 ")

        ki = open(rhcsv,'r',encoding="utf8", errors='ignore')

        lineas = ki.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        for linea in lineas:

            if "fondo" in linea or 'Fondo' in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            ##print("linea 141 ",linea)

            trozos= linea.split(';')
            
            datos_accion_sinorden =[]

            if "Fondo" not in trozos[1] and "fondo" not in trozos[1]:

                for fn in trozos[1]:

                    acciones_fondo={}

                  


                    datos_accion_sinorden.append(trozos[4]) ##var porcentual

                
                    mostrarchartfondo.fonvariacion[trozos[4]]=datos_accion_sinorden

              
        ki.close()   
    
        return mostrarchartfondo.fonvariacion
    '''
    def antiguocf(self):

        df = pd.read_csv(rhcsv, header =0, index_col =9, sep=';',decimal='.')

        nombrefondos = df['fondo'] ##ondo?

        eleccionfondo = 'esp'    

        while eleccionfondo !='':

            mayusculasf =eleccionfondo.upper()
            
            if mayusculasf =='':
                break
           
            for ni in nombrefondos:
                if mayusculasf in "TODOS":
                    ddfalfa= df.groupby('fondo').get_group(ni) ##fecha por Fondo
                    ##print("linea 194 ", ni)
                    estadisticadfalfa= ddfalfa['var_fon'].describe() ##Peso por Var_porc
                
                    ##print(estadisticadfalfa)

                                   
                    l=ddfalfa['var_fon'] ##peso por Var_porc
                
                    cs= l.cumsum()
                    
                    n = ddfalfa['var_fon'].count() ##peso por Var_porc
                
                    y=list(range(n))
                    


                    Var_p=list(ddfalfa['var_fon'])[-1]

                    ##print("ultima variación ",Var_p)
                    cad_titulo = ni+"  Variación: "+str(round(float(Var_p),4))

                    fig, ax = plt.subplots()
                    ax.plot(y,l)
                    ax.plot(y,cs)
                    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

                    ax.set_title(cad_titulo, loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                    plt.show()

                    

                if mayusculasf in  ni:
                    dfalfa= df.groupby('fondo').get_group(ni)
                    ##print(ni)
                    estadisticadfalfa= dfalfa['var_fon'].describe()
                
                    ##print(estadisticadfalfa)
                
                    input(" Estadistica")
                    l=dfalfa['var_fon']

                    cs= l.cumsum()
                    
                    n = dfalfa['var_fon'].count()
                
                    y=list(range(n))
                    
                    Var_p=list(dfalfa['var_fon'])[-1]

                    print("ultima variación ",Var_p)
                    cad_titulo = ni+" "+str(round(float(Var_p),4))

                    fig, ax = plt.subplots()
                    ax.plot(y,l)
                    ax.plot(y,cs)
                    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

                    ax.set_title(cad_titulo, loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                    plt.show()

                    eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")

                    mayusculasf =eleccionfondo.upper()
                    
                    if mayusculasf =='':
                        break

              

            eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")
  
            mayusculasf =eleccionfondo.upper()
            
            if mayusculasf =='':
            
                break


   
class dicacc():
    
    def cvf(self):
        
        fat = open(archivotickers, 'r',encoding="utf8", errors='ignore')

        lineas = fat.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        num_fon=0 ## numero fondo
        num_acc=0 ## "numero accion"


        for linea in lineas:

            if "fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            trozos= linea.split(';')
            

            if "Fondo" not in trozos[2]:    

                acciones_fondo={}

                datos_accion_sinorden =[]


                datos_accion_sinorden.append(trozos[2]) ##fondo

                datos_accion_sinorden.append(trozos[4]) ##accion

                datos_accion_sinorden.append(trozos[5]) ##peso accion fondo

                stri = ""+trozos[2]+"_"+trozos[4]

                
                acciones_fondo[stri]= {0:datos_accion_sinorden[0],1:datos_accion_sinorden[1], 2:datos_accion_sinorden[2]}

                dictacciones[trozos[4]]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7])

                num_acc =num_acc+1
                for t2 in dictacciones.values():

                    if t2 == trozos[2]:
                        claveunica = ""+trozos[2]+"_"+trozos[4]
                        s[claveunica]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],"trozos8","trozos9","trozos10","trozos11")
                        print(dicfontic[claveunica])
                        input("406")
                    num_fon = num_fon +1
                
       

       

        fat.close()     
        csflist=[]
        csflist=[num_fon, num_acc]
        return acciones_fondo


class dicaccfonclase():
    
    def cvf(self):
        
        dicaccfoncl={}

        fat = open(archivotickers, 'r',encoding="utf8", errors='ignore')

        lineas = fat.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        num_fon=0 ## numero fondo
        num_acc=0 ## "numero accion"


        for linea in lineas:

            if "Fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            trozos= linea.split(';')
            
                                                                    
            trozos8=0.0 ##precio
            trozos9=0.0 ##variacion

        
            if "fondo" not in trozos[2]:

                

                fondossinorden[trozos[2]]=0

                dictacciones[trozos[4]]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],trozos8,trozos9)

                num_acc =num_acc+1
                if True: ##for t2 in dictacciones.values():

                    if True: ##t2 == trozos[2]:
                        claveunica =trozos[2]+"_"+trozos[4]
                        dicfontic[claveunica]=[trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],trozos8,trozos9]
                       
                    num_fon = num_fon +1
                
        listadicaccfon=[]

        dicaccfoncl={}

        for fon in sorted(fondossinorden.keys()):
        
            

            for linea in lineas:

                trozos2 = linea.split(";")
                ##print(trozos2)
                ##print("165")
           
                if trozos2[2]==fon:
                    
                    listadicaccfon.append(trozos2[4])
                    ##print(fon, " ",listadicaccfon)
                    ##print ("171")
            dicaccfoncl[fon]=listadicaccfon
            ##print(dicaccfoncl[fon])
           
            listadicaccfon=[]
        lista_fondos =sorted(fondossinorden.keys())
        
        fat.close()   

        csflist=[]
        csflist=[num_fon, num_acc]
        '''
        ctv=construirtikercvs()
        ctv.cabeceratikercsv()
        fg=dicaccfonclase()
        fgcvf=fg.cvf()
        ctv.cuerpotikercsv(fgcvf[0])
        '''
        return [dicfontic,dicaccfoncl,lista_fondos]   ##dicaccfon


class datos_fon(): 


    el = dicacc()
    
    dicaccfon=  el.cvf()

    cl=dicaccfonclase()  ## listado de acciones de un fondo

    dictaccfon = cl.cvf() ##dicfontic acciones_fondo dict clave unica

    dictfontic = cl.cvf()[0]         ## dicfontic claveunica acciones
    dicaccfoncl=cl.cvf()[1] ## diccionario accuibes del fondo
    lista_fondos = cl.cvf()[2]

    tuli =dicacc()

    acciones_fondo = tuli.cvf()

    peso_acumulado= 0.0

    variacion_ponderada =0.0

    peso_accion_fondo=0.0
    
    changePercentA=0.0

    abi = "" ##accion

    abidic= {}
     


    def cot_acc(self, dacci):
                        
                        changePercentA=0.0

                        if  sabadoodomingo:
                            print("Hoy es fin de semana y no hay cotización")
                        else:
                            


                            url = "https://query1.finance.yahoo.com/v8/finance/chart/"+str(dacci)

                            r = requests.get(url,  headers={'User-agent': 'Mozilla/5.0'})
                            contenido   = r.json()

                            data = json.dumps(contenido)

                            ##print(data)

                            if "regularMarketPrice" not in data:

                                print(dacci," no encontrado")
                                input("no encontrada")
                                next
                            

                            else:
                                
                                ##print( " ", dacci," 511")
                                busqueda =""
                                
                                symb = ""
                                
                                            
                                symbA = dacci
            
                                busqueda = "regularMarketPrice"
                                
                                mlidot = data.index(busqueda)

                                posterior = "fiftyTwoWeekHigh"

                                print (data)
                                       
                            
                                variableA = data[mlidot+len(busqueda)+2: data.index(posterior)-3]
                
                                marketPriceArmp = float(variableA)
                                               
                                busqueda = "\"previousClose\":"
                                
                                rmlidot = data.index(busqueda)

                                posterior = "scale"
                        
                                variableA = float(data[rmlidot+len(busqueda)+1: data.index(posterior)-3])

                                changePercentA = float((marketPriceArmp-float(variableA))/float(variableA))

                                data=[[dacci,marketPriceArmp,changePercentA]]  

                                dfcot_acc = pd.DataFrame(data, columns=["ticker","precio", "por_var"])
                                print("\n", dfcot_acc , "****datos recuperados***************","\n")  
                                return dfcot_acc                  

    def dat_acc(self):

        peso_accion_fondo=0.0

        datosaccenelfondo={}

        
        list_dacci=[]

        nueveymedia_list_dacci = [] 


        for fon in fondossinorden:
        
            for dacci in datos_fon.dicaccfoncl[fon]:
                
                if dacci != "ticker":
                  print(dacci)
                  print("656")
                  list_dacci.append(dacci)
           
        if tiempooperacionnewyork ==False: ##False: 
                #True: ##//no carga usa y descuajeringa Pru1ods
            for dacci in list_dacci:    
                if "^" in fon or "." in dacci: 
                    nueveymedia_list_dacci.append(dacci)
        else:

            for dacci in list_dacci:
                nueveymedia_list_dacci.append(dacci)

        ##print(nueveymedia_list_dacci) 
        ##input("642")       
            
        numerodeaccion=1

        ##print(list_dacci)

        ##print("590")
        
        ###set_dacci=set(list_dacci)

        ##print(set_dacci)

        ##print ("596")   
        
        
        ###set_dacci=set(list_dacci)

        list_dacci_sin_duplicados = []

        list_dacci_sin_duplicados =list(nueveymedia_list_dacci)

        ##print(list_dacci_sin_duplicados)

        ##print("604 list_dacci_sin_duplicados")

        list_dacci_sin_duplicados.sort()

        ##print(list_dacci_sin_duplicados)
        ##print("sort 697")

        set_dacci=set(list_dacci_sin_duplicados)

        ##print(set_dacci) ##list_dacci_sin_duplicados)
        ##print("701")
        list_dacci_sorted = list(set_dacci)
        list_dacci_sorted.sort()
        print(list_dacci_sorted)
        ##input("705 set_dacci")

        #acciones_ordenadas = acciones_ordenadas.sort(reverse=False, key=any)
        vez_respiro = 0

        for dacci in list_dacci_sorted: ##list_dacci_sin_duplicados:##(dicc_dacci.keys()).sort(): ##datos_fon.dicaccfoncl[fon]: 
                    ##print(" 573 ", dacci)
                    ##print("número de acción",numerodeaccion, " ", dacci)

                    ##numerodeaccion= numerodeaccion +1

                    vez_respiro = vez_respiro +1

                    if vez_respiro%60 == 0:
                       
                        print("respiro")
                        ##input("respiro")
                        ti.sleep(11)

                    if tiempooperacionnewyork ==False: ##False: 
                        #True: ##//no carga usa y descuajeringa Pru1ods
                        

                        if "^" in dacci or "." in dacci: ##fon zv

                            cotiz_deacci=datos_fon.cot_acc(self,dacci) ##cotiz_deacci

                            print("número de acción no usa ",numerodeaccion, " ", dacci)

                            numerodeaccion= numerodeaccion +1

                    else:

                        cotiz_deacci=datos_fon.cot_acc(self,dacci) ##cotiz_deacci
                        
                        print("número de acción incluido usa ",numerodeaccion, " ", dacci)

                        numerodeaccion= numerodeaccion +1

                    ##print(cotiz_deacci)

        print("numero de acciones sin repetición ")
        print( len(list_dacci_sin_duplicados))        
        ##input("677")
        for fon in datos_fon.lista_fondos: ##dictaccfon: 

            n_acciones_fondo =0

            lista_datos_fondo=[]

            
            datos_fon.peso_acumulado=0.0

            ####datos_fon.variacion_ponderada=0.0000
            #####print(datos_fon.dicaccfoncl[fon])
            #####print(fon)
            ##input(689)

            for daccikey in nueveymedia_list_dacci: ###set_dacci:
                
                if daccikey in datos_fon.dicaccfoncl[fon]:

                    n_acciones_fondo =n_acciones_fondo+1
                
                    if True:
                        for fon in datos_fon.lista_fondos: ##dictaccfon: 

                            n_acciones_fondo =0

                            lista_datos_fondo=[]

                            valorparticipaciones =0.0 

                            valorpesoglobal=0.0          

                            n_acciones_menos_1_5 = 0

                            n_acciones_menos_2_5 = 0


                            datos_fon.peso_acumulado=0.0

                            ####datos_fon.variacion_ponderada=0.0000
                            
                            n_acciones_fondo=0

                            for daccikey in datos_fon.dicaccfoncl[fon]:

                                if daccikey in list_dacci_sin_duplicados:

                                ###if True:

                                        n_acciones_fondo =n_acciones_fondo+1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")

                                        ##print("Fondo ","\t\t", "\t", "Part.", "\t", "Var","\t", "Peso","\t","Accion","\t","Precio")
                    
                                        

                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),    3)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2]),3)   

                                        if cotiz_dacci[daccikey][2] < -2.5/100.0:
                                            n_acciones_menos_2_5 = n_acciones_menos_2_5 + 1 

                                        if cotiz_dacci[daccikey][2] < -1.5/100.0:
                                            n_acciones_menos_1_5 = n_acciones_menos_1_5 + 1

                                
                            
                            lista_datos_fondo.append(fon)
                            lista_datos_fondo.append(n_acciones_fondo)
                            lista_datos_fondo.append(valorparticipaciones)
                            lista_datos_fondo.append(valorpesoglobal)
                            if n_acciones_fondo ==0 or n_acciones_fondo == None:
                                n_acciones_fondo = 1
                            lista_datos_fondo.append(round(n_acciones_menos_1_5/n_acciones_fondo*100.0,3)) ##(n_acciones_menos_1_5/n_acciones_fondo)
                            lista_datos_fondo.append(round(n_acciones_menos_2_5/n_acciones_fondo*100.0,3)) ##(n_acciones_menos_2_5)  
                            
                            datos_resumen_fon[fon]=lista_datos_fondo
            
            lista_datos_fondo =[]
    
                
        
                    
                    
                    
                    
                    
                    
                    
                    
                       
                       
                       
                       
        return [datos_resumen_fon, datosaccenelfondo] ##resumen y detalle               
                
         


class manejarhistorico():
    
    contador =0
    
    txtlistadohistoricobak=[]

    def chuparmh(self): ##re dic datos hoy

        historicocotizapython = rhcsv   

              
    

        h = open(rhcsv, 'r',encoding="utf8", errors='ignore')

        lineah= h.readlines()

        saltarcabecera =0

        for line in lineah:
            
            saltarcabecera = saltarcabecera +1
      
            if saltarcabecera==1:
                continue

            trozoslin=line.split(';')

            Fecha = trozoslin[0]
            fondo = trozoslin[1]
            por_var = trozoslin[2]
            peso = trozoslin[3]
            n = trozoslin[4]
            actualizacion = trozoslin[5]
            Fondo = trozoslin[6]
            menos2_5 = trozoslin[7]
            menos1_5 = trozoslin[8]
            mas1_5 = trozoslin[9]

            print("linea 554 ",Fecha, fondo, por_var, peso, n, actualizacion, Fondo, menos2_5, menos1_5, mas1_5)
            
            if (not (trozoslin[0] is None)) and len(trozoslin[0])>4:##and ('/' in trozoslin[0]) :

                if '-' in Fecha:

                    primerslash = Fecha.index('-')
                    segundoslash = Fecha.rfind('-')

                    diahoyprimerguion= (diahoy).index('-')
                    diahoysegundoguion = ( diahoy).rfind("-")

                    #print("linea 718 ano historico",str(int(trozoslin[0][0:primerslash])))
                    #print("linea 719 mes historico ",str((trozoslin[0][primerslash+1:segundoslash])))
                    #print("linea 720 dia historico", str(int (trozoslin[0][segundoslash+1:])))

                    anoh=(int(Fecha[0:primerslash])) ##aqui hemos cambiado diah por anoh al ser guion
                    mesh=(int(Fecha[0][primerslash+1:segundoslash]))
                    diah=(int (Fecha[segundoslash+1:])) ##aqui hemos cambiado anoh por diah al ser guion



                    anohoy =(int(diahoy[0:diahoyprimerguion]))
                    meshoy=(int(diahoy[diahoyprimerguion+1: diahoysegundoguion]))
                    diahoynum= (int(diahoy[diahoysegundoguion+1:]))

                    
                    ##print("linea 561 dia hoy  ",(diahoynum))
                    ##print("linea 562 meshoy ",(mesh))
                    ##print("lineahoy 563 anohoy ", (anoh))

                    ##print("linea 574 ", trozoslin[1], trozoslin[0])

                    #print(("linea 739 con guiones ",(datetime.isoweekday(datetime(anoh,mesh,diah)))), "  ", datetime(anoh,mesh,diah), " today ",datetime(anohoy,meshoy,diahoynum))
                            

                    if  (datetime(anoh,mesh,diah)<datetime(anohoy, meshoy, diahoynum)):
                         

            
                        registro = Fecha+";"+fondo+";"+por_var+";"+peso.replace(',','.')+";"+n.replace(',','.')
                        registro = registro +";;\n"

                        ##print("linea 568 ",registro)
                        manejarhistorico.txtlistadohistoricobak.append(registro)
                        ##print("linea 554 ",txtlistadohistoricobak)
                        itemhistorico.append([Fecha,fondo,por_var,peso,n]) 


                if '/' in trozoslin[0]:    
                   
                    primerslash = Fecha.index('/')
                    segundoslash = Fecha.rfind('/')

                    diahoyprimerguion= (diahoy).index('-')
                    diahoysegundoguion = ( diahoy).rfind("-")

                    #print("linea 760 dia historico",str(int(trozoslin[0][0:primerslash])))
                    #print("linea 761 mes historico ",str((trozoslin[0][primerslash+1:segundoslash])))
                    #print("linea 762 ano historico", str(int (trozoslin[0][segundoslash+1:])))

                    diah=(int(Fecha[1:primerslash]))
                    mesh=(int(Fecha[primerslash+1:segundoslash]))
                    anoh=(int (Fecha[segundoslash+1:-1]))



                    anohoy =(int(diahoy[0:diahoyprimerguion]))
                    meshoy=(int(diahoy[diahoyprimerguion+1: diahoysegundoguion]))
                    diahoynum= (int(diahoy[diahoysegundoguion+1:]))

                    
                    ##print("linea 561 dia hoy  ",(diahoynum))
                    ##print("linea 562 meshoy ",(mesh))
                    ##print("lineahoy 563 anohoy ", (anoh))

                    ##print("linea 574 ", trozoslin[1], trozoslin[0])

                    #print(("linea 781",(datetime.isoweekday(datetime(anoh,mesh,diah)))), "  ", datetime(anoh,mesh,diah), " yesteday  ",(datetime.today()-timedelta(days=0, seconds=0, microseconds=0,           milliseconds=0, minutes=0, hours=23, weeks=0)))
                            

                    if   ((datetime.isoweekday(datetime(anoh,mesh,diah)))<6) and datetime(anoh,mesh,diah)<(datetime.today()-timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=23, weeks=0)):
                        registro = Fecha+";"+fondo+";"+por_var+";"+peso.replace(',','.')+";"+n.replace(',','.')
                        registro = registro +";;\n"
                        ##print("linea 568 ",registro)
                        manejarhistorico.txtlistadohistoricobak.append(registro)
                        ##print("linea 554 ",txtlistadohistoricobak)
                        itemhistorico.append(Fecha,fondo,por_var,peso,n,actualizacion,Fondo,menos2_5, menos1_5, mas1_5)
    
        h.close()
        return manejarhistorico.txtlistadohistoricobak

    def recrearficheromh(self):
        
        ##borrado de fichero
        hm = open(rhcsv, 'w')
        cabecera=( 'Fecha'+";"+'fondo'+";"+'por_var'+";"+'peso'+';'+'n'+";"+"actualizacion"+";"+"Fondo"+";"+"menos2_5"+";"+"menos1_5"+";"+"mas_1_5"+'\n')
        ##print("CABECERA DE HISTORICO ",cabecera)
        hm.write(cabecera)
        hm.close()
        

    def incorporarmh(self):  ##manejarhistorico.txtlistadohistoricobak historico

    
        
        #reconstitución de fichero
               
        h = open(rhcsv, 'a')

        for registro in manejarhistorico.txtlistadohistoricobak:
            ##print("linea 609 ", registro)
            ll=h.write(registro)
            #print("576 ", ll)
            ##print("642",registro)

        h.close()

    def incorporarhoy(self):      

        re = datos_resumen_fon
        
        h= open(rhcsv,'a')

        for cad in re.keys():
            #print("linea 283 ", cad)
            if  sabadoodomingo:
                print("Hoy es fin de semana y no hay cotización")
            else: #elimina los de hoy  y fines para que no se dupliquen
         
                recad=datos_resumen_fon[cad]
                ##print(recad)
                cadenaretxt= str(diahoy)+";"+str(recad[0])+";"+str(recad[1])+";"+str(recad[2])+";"+str(recad[3])+";"+momentohoy+";"+str(recad[0]+";"+str(recad[5])+";" +str(recad[4])+";"+str(recad[6])+"\n")
                ##print ("REGISTROS DE HOY ",cadenaretxt)

                ##print ("589 ",cadenaretxt)
                
                h.write(cadenaretxt)
                itemhistorico.append(re[cad])
        
        h.close()

       

class preguntarchartfondo():

    mayusculasf =""


    ## fufu =mostrarchartfondo()
    def pcf(self):
        
        repetir = 'S'

        while repetir in 'SI':

            eleccionfondo ='BOLSAESPANA'

            ##eleccionfondo = 'si'    

            while eleccionfondo !='':
              
                mayusculasf =eleccionfondo.upper()
                if mayusculasf =='':
                    repetir ="no"
                    break
                
                
        
            repetir = input("De qué fondo desea ver más gráficos?")

       


class maino():
    saltarheader2=0
    
    def creaccionnombresfondos(self):
        
        

        fsog = open(archivonombresfondos,'w')

        fsog.close()

        ##print ("646 fichero renovado ", archivonombresfondos)

    def anadidosfondos(self):

        ##print("650 ejecutando anadidosfondos")
               
        arcnomfon =archivonombresfondos

        er = dicaccfonclase()
        listafondos = er.cvf()[2]
   
        fso = open(arcnomfon, 'a')

    

        for fond9 in listafondos: ##archivo nombres fondos
            
            cadfon =fond9+"\n"
            py =fso.write(cadfon)
          
        fso.close()

    
    def creacotizahoypython(self):


        f = cotizahoypython
        ##if os.path.isfile(f):
            ##  os.remove(f)

        chp = cotizahoypython

        g=open(chp,'w')
        
        g.write( 'Fecha'+";"+'Fondo'+";"+'n'+";"+'Peso'+';'+'Var_porc'+";"+"Actualizacion"+";"+"porc_1_5"+";"+"porc_2_5"+'\n')

        g.close()

    def anadircotizahoypython(self):
        
       
        cothoypyt = cotizahoypython


        re = datos_resumen_fon

        ##print (re)

        gi = open(cothoypyt, 'a')


        for resumen in re:
        
            ##print(resumen)

            listado = re[resumen]
            
            ##print(listado)

            linea_resumen = ""+str(diahoy)+";"+str(listado[0])+";"+ str(listado[1])+";" +str(listado[2])+";"+str(listado[3])+";" +str(momentohoy)+";" +str(listado[4])+";" +str(listado[5])+"\n"

            ##print(linea_resumen)

            ilo = gi.write (linea_resumen)
            
      
        gi.close()
        
        if os.path.isfile(resucsv):
            os.remove(resucsv)



        resumcsv = open(resucsv,'w')
        resumcsv.close()

        resumcsv = open(resucsv,'a')

        resumcsv.write("dia;fondo;n;peso;var_por;actualizacion;porc_1_5;porc_2_5\n")

        for resumen in re:
            
            ##print(resumen)

            listado = re[resumen]
            
            ##print(listado)

            linea_resumen = ""+str(diahoy)+";"+str(listado[0])+";"+ str(listado[1])+";" +str(listado[2])+";"+str(listado[3])+";" +str(momentohoy)+";" +str(listado[4])+";" +str(listado[5])+"\n"

            ##print(linea_resumen)

            ilo = resumcsv.write (linea_resumen)
            
      
        resumcsv.close()

    def pantallahoy(self):

        h = open(cotizahoypython, 'r',encoding="utf8", errors='ignore')

        lineah= h.readlines()

        eliminadorcabeza=0;

        for line in lineah:

            campos= line.split(";")
            
            if eliminadorcabeza==0:
                eliminadorcabeza= eliminadorcabeza +1
                fecha = str(campos[0])
                fondos = campos[1],
                n=campos[2]
              
              
                
                
              
                print('{:3}\t\t{:4}\t{:4}\t{:4}\t{:}\t\t{:4}\t{:4}'.format(str(campos[0]),str(campos[2]),str(campos[3]),str(campos[4]),campos[1],str(campos[6]),str(campos[7])))
                next

                       
            else: 

                pesof=round(float(campos[3]),4)
                variacionf=round(float(campos[4]),4)
                fecha = str(campos[0])
                fondos = campos[1]
                n=str(int(campos[2]))
                var = str(round(float(campos[3]),2))
                


                ##print(pesof,  "  var: ",variacionf)

                print('{:3}\t{:4}\t{:4}\t{:4}\t{:10}\t\t{:4}\t{:4}'.format(fecha,n,pesof,variacionf,fondos,str(campos[6]),str(campos[7])))
                
                ##print(str(campos[0]),'\t',campos[1],'\t',str(campos[2]),'\t',str(pesof), '\t',str(variacionf))
        ##print(tabulate(lineah, headers = ['fecha','fondo','n','Peso','Variacion']))
        h.close()

    def procesomanejarhistorico(self):
       
      
        mhu=manejarhistorico()
        bu =mhu.mh()



class mainje():  

    def maindef(self): 
        #actualizardatos  = input("Actualizar datos? (s) ")
        if True: ##actualizardatos in "Sisi":      
            momentoinicio = str(datetime.now())

            print(momentoinicio)
            print("trabajando ...")
            trabajarresumencsv = datosprecedentes()
            trabajarresumencsv.mostrardatosanteriores()
            print("linea 1827")
            trabajarresumencsv.mostrardetalledatosanteriores()
            print("linea 1829") 
            if False: ##numdiasemana>5:
                print("el fin de semana esto no actualiza")
                input("854")
                exit()
            actualizar = input("Actualizar datos? (s) ")
            if actualizar in "Sisi":

                ej0 = construirtickercvs()
                mej01 = ej0.decirtickersunicos()
                mej02 = ej0.actualizar_resumenhistoricocsv() 

            mhejecutar =manejarhistorico()
            meje1= mhejecutar.chuparmh()
            meje2= mhejecutar.recrearficheromh()
            meje3= mhejecutar.incorporarmh()
        
            meje4= mhejecutar.incorporarhoy();
            print(momentoinicio)
            momentofinalizacion = str(datetime.now())
            print(momentofinalizacion)
            input("873")
            hy=ver_comp()
            hy.ver_c(ejec0[1])


            

            input("quieres ver la actualización?")
                  
          
            
            
            '''
            
            
            
            gir = datos_fon()
            ejec0 = gir.dat_acc() ##da datos_resume_fon
            ctv=construirtikercvs()
            ctv.cabeceratikercsv()
            fg=dicaccfonclase()
            fgcvf=fg.cvf()
            #### construccion cotizacion acciones fgctv.cuerpotikercsv(fgcvf[0])
            ejecutar = maino()
            ejec1 = ejecutar.creaccionnombresfondos()
            ejec2 = ejecutar.anadidosfondos()
            ejec3= ejecutar.creacotizahoypython()
            ejec4= ejecutar.anadircotizahoypython()
            ejec5= ejecutar.pantallahoy()
            '''     
            mhejecutar =manejarhistorico()
            meje1= mhejecutar.chuparmh()
            meje2= mhejecutar.recrearficheromh()
            meje3= mhejecutar.incorporarmh()
        
            meje4= mhejecutar.incorporarhoy();
            print(momentoinicio)
            momentofinalizacion = str(datetime.now())
            print(momentofinalizacion)
            input("873")
            hy=ver_comp()
            hy.ver_c(ejec0[1])

        repetir = input( " 875 Quiere ver el gráfico de algún fondo (n = ninguno) ")
        while repetir not in "Nn":
            ##io = preguntarchartfondo()
            ##iou= io.pcf()
            jijo=mostrarchartfondo()
            ##jijomcf=jijo.mcf( )   
            jijomoc0= jijo.antiguocf()
            
            repetir = input( " 883 Quiere ver el gráfico de algún fondo (n = ninguno) ")

    momentohoy = str(datetime.now())
    print(momentohoy)



cl= mainje()
cl.maindef()



   
