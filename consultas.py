from sqlalchemy.orm import sessionmaker
from baseDatos import baseDatos
import pandas as pd


Session = sessionmaker(bind = baseDatos.engine)
session = Session()
conn = baseDatos.engine.raw_connection()
#cursor = conn.cursor()
class consulta():

    df=pd.DataFrame()
    
    def __init__(self):
        super().__init__() 
        pass

    def df_consulta(self, c):
        consulta.df=pd.read_sql_query(c, con=conn) #toma como parametro la c que es el string de la consulta, la ejecuta en la base de datos y luego crea un dataframe con los datos generados
        return consulta.df
        
        
#conn.close()

