import pandas as pd
from datetime import datetime

resumencsv_inner_detallados = "c:/Auxiliares/df_inner_detallados.csv"
resumencsv= "c:/Auxiliares/resumencsv.csv"

class cuerpo():

        fecha_actual_formateada = None
        momento_actual_formateada = None

        def __init__(self):
        
                self.fecha_actual_formateada   = datetime.now().strftime("%d-%m-%Y")
                self.momento_actual_formateada = datetime.now().strftime("%H:%M:%S")     
        



        def mostrar(self):

                df_inner_detallados = pd.read_csv(resumencsv_inner_detallados,header = 0, index_col =0, sep=';',decimal='.', encoding='ISO-8859-1')
                print(df_inner_detallados)

                print(df_inner_detallados.columns)

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
                df_resumencsv.to_csv(resumencsv_inner_detallados, sep=';', decimal='.', index=False)  
                df_resumencsv.to_csv(resumencsv, sep=';', decimal='.', index=False, mode='a', header=False)          
                #añadir 
                input()





instancia = cuerpo()
e1= instancia.mostrar()