from collections import OrderedDict
import re
import pandas as pd
from tkinter import Tk, Label, Button, Frame,  messagebox, filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL
import os.path
from sqlalchemy import create_engine


class baseDatos():
    #Creación de los documentos de clase para que pueda accederse a los datos almacenados en los mismos, adicional se inicializa con un dataframe vacio para que puedan ser llenados posteriormente
    wos=pd.DataFrame() 
    scopus = pd.DataFrame()
    scielo  = pd.DataFrame()
    completo  = pd.DataFrame()
    ARTICULO = pd.DataFrame()
    FINANCIAMIENTO_ARTICULO = pd.DataFrame()
    FINANCIAMIENTO = pd.DataFrame()
    INSTITUCION_ARTICULO = pd.DataFrame()
    INSTITUCION = pd.DataFrame()
    PAIS = pd.DataFrame()
    BDKEY_ARTICULO  = pd.DataFrame()
    BDKEYWORD = pd.DataFrame()
    CATEGORIA_ARTICULO = pd.DataFrame()
    CATEGORIA = pd.DataFrame()
    SUB_CATEGORIA = pd.DataFrame()
    AUTOR_ARTICULO = pd.DataFrame() 
    AUTOR = pd.DataFrame()
    AUKEY_ARTICULO = pd.DataFrame()
    AU_KEYWORD = pd.DataFrame()
    FUENTE = pd.DataFrame()
    OA_ARTICULO = pd.DataFrame()
    OPEN_ACCESS = pd.DataFrame()
    engine= ''
    md=object
    df_paises=pd.read_excel("bd_paises.xlsx")
   
   
    def __init__(self):
        super().__init__()

    #Ejecución de cada botón almacenado en la interfaz donde se llama la función método para poder leer el archivo, llenar el atributo de clase y seleccionar las columnas deseadas para la realización del código
    def ejecutar_wos(self):
        baseDatos.wos=self.seleccionar_archivo(self, '*.txt')  #retorna un df
        baseDatos.wos = pd.DataFrame(baseDatos.wos, columns=['TI', 'AU', 'DE', 'ID', 'WC', 'SO', 'AB', 'Z9', 'C3', 'PU', 'C1', 'SN', 'EI', 'BN', 'DI', 'FU', 'OA', 'PY', 'LA', 'WE', 'UT', 'DT'])

        baseDatos.wos=baseDatos.wos.rename(columns={'TI' : 'Titulo' , 'AU' : 'Nombre_autor' , 'DE' : 'Autor_keyword' , 'ID' : 'palabras_clave_base_de_datos' , 'WC' : 'categorias' , 'SO' : 'Nombre_fuente' , 'AB' : 'Resumen' , 'Z9' : 'Citas_recibidas' , 'PU' : 'Editorial' , 'C1' : 'paises' , 'SN' : 'ISSN' , 'EI' : 'eISSN' , 'BN' : 'ISBN' , 'DI' : 'DOI' , 'FU' : 'financiamiento' , 'OA' : 'open_access' , 'PY' : 'Anio' , 'LA' : 'Idioma' , 'WE' : 'Base_de_datos' , 'UT' : 'Num_acceso' , 'DT' : 'Tipo_de_documento'})        
        return baseDatos.wos
    
    def ejecutar_scopus(self):
        baseDatos.scopus
        baseDatos.scopus=self.seleccionar_archivo(self,'*.csv')  #retorna un df
        baseDatos.scopus = pd.DataFrame(baseDatos.scopus, columns=['Title', 'Authors', 'Author Keywords', 'Index Keywords', 'Source title', 'Abstract', 'Cited by', 'Affiliations', 'Publisher', 'ISSN', 'ISBN', 'DOI', 'Funding Details', 'Sponsors', 'Open Access', 'Year', 'Language of Original Document', 'Source', 'EID', 'Document Type'])
        #columnas=['Titulo' , 'Nombre_autor' , 'Autor_keyword' , 'palabras_clave_base_de_datos' , 'categorias' , 'Nombre_fuente' , 'Resumen' , 'Citas_recibidas' , 'Editorial' , 'paises' , 'ISSN' , 'eISSN' , 'ISBN' , 'DOI' , 'financiamiento' , 'open_access' , 'Anio' , 'Idioma' , 'Base_de_datos' , 'Num_acceso' , 'Tipo_de_documento']
        #baseDatos.scopus= baseDatos.scopus.reindex(columns = columnas)
        aux = pd.DataFrame(baseDatos.scopus, columns=['Funding Details', 'Sponsors'])
        aux=aux.fillna('[No disponible]')
        aux = aux.rename(columns={'Funding Details':'funding'})
        aux['financiamiento']=aux['funding'].str.cat(aux['Sponsors'], sep='|') #separa financiamiento de sponsor
        baseDatos.scopus['financiamiento'] = aux['financiamiento']
        
        baseDatos.scopus = pd.DataFrame(baseDatos.scopus, columns=['Title', 'Authors', 'Author Keywords', 'Index Keywords', 'Source title', 'Abstract', 'Cited by', 'Affiliations', 'Publisher', 'ISSN', 'ISBN', 'DOI', 'financiamiento', 'Open Access', 'Year', 'Language of Original Document', 'Source', 'EID', 'Document Type'])
        
        baseDatos.scopus=baseDatos.scopus.rename(columns={'Title' : 'Titulo' , 'Authors' : 'Nombre_autor' , 'Author Keywords' : 'Autor_keyword' , 'Index Keywords' : 'palabras_clave_base_de_datos' , 'Source title' : 'Nombre_fuente' , 'Abstract' : 'Resumen' , 'Cited by' : 'Citas_recibidas' , 'Publisher' : 'Editorial' , 'Affiliations' : 'paises' , 'ISSN' : 'ISSN' , 'ISBN' : 'ISBN' , 'DOI' : 'DOI' , 'Open Access' : 'open_access' , 'Year' : 'Anio' , 'Language of Original Document' : 'Idioma' , 'Source' : 'Base_de_datos' , 'EID' : 'Num_acceso' , 'Document Type' : 'Tipo_de_documento'})
        baseDatos.scopus['Nombre_categoria']="[No disponible]"
        baseDatos.scopus['categorias']="[No disponible]"
        print(baseDatos.scopus)

        return baseDatos.scopus

    def ejecutar_scielo(self):
        baseDatos.scielo
        baseDatos.scielo=self.seleccionar_archivo(self,'*.txt')  #retorna un df
        

        baseDatos.scielo = pd.DataFrame(baseDatos.scielo, columns=['TI', 'AU', 'DE', 'EC', 'SC', 'SO', 'AB', 'Z9', 'C1', 'PU', 'SN', 'DI', 'OA', 'PY', 'LA', 'C2', 'UT', 'DT'])
        baseDatos.scielo['financiamiento'] = '[No disponible]'
        baseDatos.scielo=baseDatos.scielo.rename(columns={'TI' : 'Titulo' , 'AU' : 'Nombre_autor' , 'DE' : 'Autor_keyword' , 'EC' : 'palabras_clave_base_de_datos' , 'SC' : 'categorias' , 'SO' : 'Nombre_fuente' , 'AB' : 'Resumen' , 'Z9' : 'Citas_recibidas' , 'PU' : 'Editorial' , 'C1' : 'paises' , 'SN' : 'ISSN' , 'DI' : 'DOI' , 'OA' : 'open_access' , 'PY' : 'Anio' , 'LA' : 'Idioma' , 'C2' : 'Base_de_datos' , 'UT' : 'Num_acceso' , 'DT' : 'Tipo_de_documento'})
        return baseDatos.scielo
    
    #Ventana para seleccionar los archivos la cuál pide como parámetro la extensión del mismo para su posterior filtro, esta función retorna el dataframe del archivo después de llamar al método para pasar a dataframe
    def seleccionar_archivo(self, ext):
        archivo = filedialog.askopenfilename(title='Abrir archivo...', filetypes=[("Archivos"+ext, ext)])
        return self.pasar_dataframe(self, archivo)
        
    #Método para pasar a dataframe el archivo, recibe como parámetro la ruta
    def pasar_dataframe(self, archivo):
        if os.path.splitext(archivo)[1] == ".csv": #mediante la función "splitext" se pasa el archivo a una tupla cuya segunda posición es la extensión del archivo para así poder saber qué pasos utilizar para poder pasarlo a un dataframe
            df=pd.read_csv(archivo)
        elif os.path.splitext(archivo)[1] == ".txt":
            df=pd.read_csv(archivo, sep='\t')
        else:
            messagebox.showinfo('Error', "Por favor seleccione un archivo valido")  #si la extensión no es ninguna de las permitidas se arroja un error     
        return df

    #Una vez llenados los atributos de clase se procede a concatenar los dataframes principales (wos, scopus, scielo)
    #se ejecuta este comando con el botón "aceptar" de la interfaz
    
    def concatenar (self):
        baseDatos.completo
        baseDatos.completo=pd.concat([baseDatos.wos, baseDatos.scielo, baseDatos.scopus])
        self.limpiar(self) #se llama esta función para proceder a la limpieza de los datos

        return

    #Limpieza de los datos que se van a incluir en más tablas para así "normalizarlos"
    def limpiar(self):
        baseDatos.completo.reset_index(drop=True, inplace=True) #drop borra inplace reemplaza y así se tienen los ID resueltos
        baseDatos.completo=baseDatos.completo.fillna({'Citas_recibidas':0.0})
        baseDatos.completo=baseDatos.completo.fillna('[No disponible]')#llenar los valores vacios con...
        #filled_df = student_df.fillna({'Age': 17, 'Income(in $)': 300})
        """ baseDatos.completo['Autor_keyword']=baseDatos.completo['Autor_keyword'].str.upper()
        baseDatos.completo['Autor_keyword']=baseDatos.completo['Autor_keyword'].str.translate(str.maketrans('áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN')) #Pasa los valores de la columna a un str donde se empieza a reemplazar los valores
        baseDatos.completo['BD_keyword']=baseDatos.completo['BD_keyword'].str.translate(str.maketrans('áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN')) #reemplaza, lo pone en la listatranslate(str.maketrans('áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN')) #reemplaza, lo pone en la lista
        baseDatos.completo['BD_keyword']=baseDatos.completo['BD_keyword'].str.upper()
        baseDatos.completo['Categorias']=baseDatos.completo['Categorias'].str.upper()
        baseDatos.completo['Categorias']=baseDatos.completo['Categorias'].str.translate(str.maketrans('áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN')) 
        baseDatos.completo['Autores']=baseDatos.completo['Autores'].str.translate(str.maketrans('áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'))  """
        self.creacion_tablas(self)


    #Método que llama a funciones para la creación de las tablas
    def creacion_tablas(self):
        self.tabla_fuente(self)
        self.tabla_articulo(self)
        self.tabla_oa(self)
        self.tablas_auKey(self)
        self.tablas_autores(self)
        self.tablas_categoria(self)
        self.tablas_BdKey(self)
        self.tablas_pais_institucion(self)
        self.tablas_financiamiento(self)
        self.descargas(self)
        
#Creación tabla FUENTE
    def tabla_fuente(self):
        baseDatos.FUENTE=pd.DataFrame(baseDatos.completo, columns=['Nombre_fuente', 'ISSN', 'eISSN', 'ISBN'])
        #baseDatos.FUENTE=baseDatos.FUENTE.drop_duplicates(['ISSN']) #funciona perfectamente,  ahora como pongo el formato ####-#### para que normalice más, no todos tienen issn
        baseDatos.FUENTE=baseDatos.FUENTE.drop_duplicates(['Nombre_fuente']) #¿Lo incluyo o solo con el ISSN, también lo hago con ISBN?
        baseDatos.FUENTE = baseDatos.FUENTE.sort_values('Nombre_fuente', axis=0,ascending=True) #ordena alfabéticamente
        baseDatos.FUENTE.reset_index(drop=True, inplace=True) #vuelve a poner indices
        baseDatos.FUENTE=baseDatos.FUENTE.fillna('[No disponible]')
        baseDatos.FUENTE = baseDatos.FUENTE.rename_axis('ID_fuente')
        

#Creación tabla ARTICULO
    def tabla_articulo(self):
        baseDatos.ARTICULO=pd.DataFrame(baseDatos.completo, columns=['Titulo', 'Resumen', 'Citas_recibidas', 'DOI', 'Editorial', 'Base_de_datos', 'Idioma', 'Anio', 'Num_acceso', 'Tipo_de_documento'])
        
        indices=[]
        for j in baseDatos.completo.Nombre_fuente:
            indices.append([baseDatos.FUENTE.index[baseDatos.FUENTE['Nombre_fuente']==j]][0][0]) #busca dentro de la columna autor de tabla autores la j y pasa el indice a la columna

        baseDatos.ARTICULO['ID_fuente']=indices #llena la columna de articulo con lo que se hizo en completo
        baseDatos.ARTICULO=baseDatos.ARTICULO.rename_axis('ID_art')
#Creación tablas open access
    def tabla_oa(self):
        oa=baseDatos.completo.open_access.tolist()
        tablaoa=[]
        tablaoa_art=[]
        cont=0
        for i in oa:
            aux=i.split(", ")
            for j in aux:
                f=str(j)
                j=j.upper()
                if j.find("GREEN")!=-1:
                    j = "GREEN"
                tablaoa.append(j)
                tablaoa_art.append([cont, j])
            cont+=1
        
        tablaoa = list(set(tablaoa))
        baseDatos.OPEN_ACCESS=pd.DataFrame(tablaoa).rename(columns={0:'Tipo_oa'})
        baseDatos.OPEN_ACCESS=baseDatos.OPEN_ACCESS.rename_axis('ID_oa')
        baseDatos.OA_ARTICULO=pd.DataFrame(tablaoa_art).rename(columns={0:'ID_art', 1:'oa'})

        indices=[]
        cont=0
        for j in baseDatos.OA_ARTICULO.oa:
            indices.append([baseDatos.OPEN_ACCESS.index[baseDatos.OPEN_ACCESS['Tipo_oa']==j]][0][0]) #busca dentro de la columna autor de tabla autores la j y pasa el indice a la columna

        baseDatos.OA_ARTICULO['ID_oa']=indices
        baseDatos.OA_ARTICULO=pd.DataFrame(baseDatos.OA_ARTICULO, columns=['ID_art', 'ID_oa'])
        baseDatos.OA_ARTICULO=baseDatos.OA_ARTICULO.rename_axis('ID_oa_art')

   
#creación tabla AuKey_articulo(baseDatos.AUKEY_ARTICULO) y AuKey (baseDatos.AU_KEYWORD)
    def tablas_auKey(self):

        auKey = baseDatos.completo.Autor_keyword.tolist()

        cont=0
        tabAuKey=[]
        for i in auKey:
            aux=i.split("; ")
            for j in aux:
                j = re.sub(r'[^\w\s]','',j)
                tabAuKey.append([cont, j])
            cont=cont+1
        baseDatos.AUKEY_ARTICULO = pd.DataFrame(tabAuKey)
        baseDatos.AUKEY_ARTICULO =  baseDatos.AUKEY_ARTICULO.rename(columns={0:'ID_art', 1:'Autor_keyword'})

        baseDatos.AU_KEYWORD = pd.DataFrame(list(OrderedDict.fromkeys(baseDatos.AUKEY_ARTICULO.Autor_keyword.tolist())))
        baseDatos.AU_KEYWORD = baseDatos.AU_KEYWORD.sort_values(0,ascending=True)
        baseDatos.AU_KEYWORD = baseDatos.AU_KEYWORD.rename(columns={0:"Autor_keyword"})
        baseDatos.AU_KEYWORD.reset_index(drop=True, inplace=True)
        baseDatos.AU_KEYWORD= baseDatos.AU_KEYWORD.rename_axis('ID_auKey')

        indices=[]

        for j in baseDatos.AUKEY_ARTICULO.Autor_keyword:
            indices.append([baseDatos.AU_KEYWORD.index[baseDatos.AU_KEYWORD['Autor_keyword']==j]][0][0])
        baseDatos.AUKEY_ARTICULO['ID_aukey']=indices
        baseDatos.AUKEY_ARTICULO= pd.DataFrame(baseDatos.AUKEY_ARTICULO, columns=['ID_art','ID_aukey'])
        baseDatos.AUKEY_ARTICULO= baseDatos.AUKEY_ARTICULO.rename_axis('ID_aukey_art')


#creación tabla AUTOR_ARTICULO(baseDatos.AUTOR_ARTICULO) y Autor (baseDatos.AUTOR)
    def tablas_autores(self): 
        autores=baseDatos.completo.Nombre_autor.tolist() #lista de autores
        tabAut=[]
        cont=0
        for i in autores:
            if cont < len(baseDatos.wos.index)+len(baseDatos.scielo.index):
                aux=i.split("; ") #separa los autores por ;
            else:
                aux=i.split(", ")
            for j in aux:
                j=re.sub(r'[^\w\s]','',j) #quita , y caracteres especiales
                tabAut.append([cont, j])
            cont=cont+1

        baseDatos.AUTOR_ARTICULO=pd.DataFrame(tabAut)
        baseDatos.AUTOR_ARTICULO=baseDatos.AUTOR_ARTICULO.rename(columns={0:'ID_art', 1:'Nombre_autor'}) #cambia nombres
        

        baseDatos.AUTOR = pd.DataFrame(list(OrderedDict.fromkeys(baseDatos.AUTOR_ARTICULO.Nombre_autor.tolist()))) #quita duplicados los pasa a una linea y los mete dentro del df
        baseDatos.AUTOR = baseDatos.AUTOR.sort_values(0,ascending=True) #ordena alfabéticamente
        baseDatos.AUTOR = baseDatos.AUTOR.rename(columns={0:'Nombre_autor'}) #cambia nombre de lo ingresado en el 105
        baseDatos.AUTOR.reset_index(drop=True, inplace=True) #vuelve a poner indices
        baseDatos.AUTOR = baseDatos.AUTOR.rename_axis('ID_au')

        indices=[]
        for j in baseDatos.AUTOR_ARTICULO.Nombre_autor:
            indices.append([baseDatos.AUTOR.index[baseDatos.AUTOR['Nombre_autor']==j]][0][0]) #busca dentro de la columna autor de tabla autores la j y pasa el indice a la columna

        baseDatos.AUTOR_ARTICULO['ID_au']=indices
        baseDatos.AUTOR_ARTICULO= pd.DataFrame(baseDatos.AUTOR_ARTICULO, columns=['ID_art','ID_au'])
        baseDatos.AUTOR_ARTICULO= baseDatos.AUTOR_ARTICULO.rename_axis('ID_aut_art')

#creación tabla categoria_articulo(baseDatos.CATEGORIA_ARTICULO), categoria (baseDatos.CATEGORIA) y sub_categoria (baseDatos.SUB_CATEGORIA)
    def tablas_categoria(self):
        categoria=baseDatos.completo.categorias.tolist()
        cont=0
        tabCatego=[]
        for i in categoria:
            if i != "[No disponible]":
                aux=i.split("; ")
                for j in aux:
                    if j.find(", ")!= -1:
                        aux2=j.split(", ") 
                        tabCatego.append([cont, aux2[0], aux2[1]])
                    elif j != "[No disponible]":
                        tabCatego.append([cont, j, "[No disponible]"])
            else: 
                tabCatego.append([cont, "[No disponible]", "[No disponible]"])
                    
            cont=cont+1
        baseDatos.CATEGORIA_ARTICULO = pd.DataFrame(tabCatego)
        baseDatos.CATEGORIA_ARTICULO =  baseDatos.CATEGORIA_ARTICULO.rename(columns={0:'ID_art', 1:'Nombre_categoria', 2:'Nombre_subcategoria'})


        categoria=list(OrderedDict.fromkeys(baseDatos.CATEGORIA_ARTICULO.Nombre_categoria.tolist()))#quitar duplicados

        baseDatos.CATEGORIA = pd.DataFrame(categoria)
        baseDatos.CATEGORIA = baseDatos.CATEGORIA.sort_values(0, ascending=True)
        baseDatos.CATEGORIA = baseDatos.CATEGORIA.rename(columns={0:'Nombre_categoria'})
        baseDatos.CATEGORIA.reset_index(drop=True, inplace=True)
        baseDatos.CATEGORIA=baseDatos.CATEGORIA.rename_axis('ID_cat')


        categoria=list(OrderedDict.fromkeys(baseDatos.CATEGORIA_ARTICULO.Nombre_subcategoria.tolist()))
        baseDatos.SUB_CATEGORIA = pd.DataFrame(categoria)
        baseDatos.SUB_CATEGORIA = baseDatos.SUB_CATEGORIA.sort_values(0, ascending=True)
        baseDatos.SUB_CATEGORIA = baseDatos.SUB_CATEGORIA.rename(columns={0:'Nombre_subcategoria'})
        baseDatos.SUB_CATEGORIA.reset_index(drop=True, inplace=True)
        baseDatos.SUB_CATEGORIA=baseDatos.SUB_CATEGORIA.rename_axis('ID_subcat')

        indices=[]
        for j in baseDatos.CATEGORIA_ARTICULO.Nombre_categoria:
            aux='"'+j+'"'
            indices.append([baseDatos.CATEGORIA_ARTICULO.index[baseDatos.CATEGORIA_ARTICULO['Nombre_categoria']==j]][0][0])
        baseDatos.CATEGORIA_ARTICULO['ID_cat']=indices

        indices=[]
        for j in baseDatos.CATEGORIA_ARTICULO.Nombre_subcategoria:
            aux='"'+j+'"'
            indices.append([baseDatos.CATEGORIA_ARTICULO.index[baseDatos.CATEGORIA_ARTICULO['Nombre_subcategoria']==j]][0][0])
        baseDatos.CATEGORIA_ARTICULO['ID_subcat']=indices
        baseDatos.CATEGORIA_ARTICULO=pd.DataFrame(baseDatos.CATEGORIA_ARTICULO, columns={'ID_art', 'ID_cat', 'ID_subcat'})
        baseDatos.CATEGORIA_ARTICULO= baseDatos.CATEGORIA_ARTICULO.rename_axis('ID_cat_art')
        
#creación tabla BdKey_articulo(baseDatos.BDKEY_ARTICULO) y BdKeyword (baseDatos.BDKEYWORD) 
    def tablas_BdKey(self):
        inKey = baseDatos.completo.palabras_clave_base_de_datos.tolist()
        cont=0
        tabIndexKey=[]
        for i in inKey:
            aux=i.split("; ")
            for j in aux:
                j =  re.sub(r'[^\w\s]','',j)
                tabIndexKey.append([cont, j])
            cont=cont+1
        baseDatos.BDKEY_ARTICULO = pd.DataFrame(tabIndexKey)
        baseDatos.BDKEY_ARTICULO =  baseDatos.BDKEY_ARTICULO.rename(columns={0:'ID_art', 1:'BD_keyword'})

        baseDatos.BDKEYWORD = pd.DataFrame(list(OrderedDict.fromkeys(baseDatos.BDKEY_ARTICULO.BD_keyword.tolist())))
        baseDatos.BDKEYWORD = baseDatos.BDKEYWORD.sort_values(0,ascending=True)
        baseDatos.BDKEYWORD = baseDatos.BDKEYWORD.rename(columns={0:"BD_keyword"})
        baseDatos.BDKEYWORD = baseDatos.BDKEYWORD.rename_axis('ID_bdKey')

        indices=[]
        for j in baseDatos.BDKEY_ARTICULO.BD_keyword:
            indices.append([baseDatos.BDKEYWORD.index[baseDatos.BDKEYWORD['BD_keyword']==j]][0][0])
        baseDatos.BDKEY_ARTICULO['ID_bdKey']=indices
        baseDatos.BDKEY_ARTICULO=pd.DataFrame(baseDatos.BDKEY_ARTICULO, columns={'ID_art', 'ID_bdKey'})
        baseDatos.BDKEY_ARTICULO= baseDatos.BDKEY_ARTICULO.rename_axis('ID_bdKey_art')

    def busca_pais(self, texto:str):
        for index, fila in baseDatos.df_paises.iterrows():
            if texto.find(str(fila['Country'])) != -1:
                return str(fila['Code'])+"; "+ str(fila['Country'])
            elif texto.find(str(fila['Esp'])) != -1:
                return str(fila['Code'])+"; "+ str(fila['Country'])
            elif texto.find(str(fila['Por'])) != -1:
                return str(fila['Code'])+"; "+ str(fila['Country'])
        return "[No disponible]"
            
#Creación tablas institución y país
    def tablas_pais_institucion(self):
        
        instituciones=baseDatos.completo.paises.tolist()
        tabla_art_ins=[]
        aux=''      
        cont=0
        i_aux=[]
        pais=""
        for i in instituciones:
            i=str(i)
            can=i.count('[') #cuenta la cantidad de [existentes para eliminar lo que hay dentro]

            for k in range(can):
                if i.find('[')!=-1 and i.find(']')!=1: #Se elimina lo que hay dentro de los [] donde se encuentra el autor
                    ini=i.index('[')
                    fin=i.index(']')

                    for l in range(ini, fin+1):
                        aux+=i[l]
                    i=i.replace(aux, '')
                    aux=''

            
            full=i.split("; ")
            for j in full:

                ins=j.split(", ")

                if cont < len(baseDatos.wos.index)+len(baseDatos.scielo.index): #Si está entre wos o scielo
                    #separa las instituciones por , donde esta la institución, sigue el pais (ins)
                    pais=self.busca_pais(self, str(ins[-1]))
                    #lograr que si solo hay un registro entonces omita el pais
                    if len(ins)==1:
                        tabla_art_ins.append([cont, ins[0].strip(), '[No disponible]'])#strip elimina los espacios en blanco a los extremos de la cadena
                    else:
                        tabla_art_ins.append([cont, ins[0].strip(), pais])#strip elimina los espacios en blanco a los extremos de la cadena
                else: #Si está en Scopus
                    pais=self.busca_pais(self, str(ins[-1]))
                    aux1=len(tabla_art_ins)
                    for k in ins:
                        k=str(k)
                        if k.find('Univ')!=-1:
                            tabla_art_ins.append([cont, ins[ins.index(k)], pais])
                            i_aux.append(ins[ins.index(k)])
                            break
                        elif k.find('Instit')!=-1:
                            tabla_art_ins.append([cont, ins[ins.index(k)], pais])
                            i_aux.append(ins[ins.index(k)])
                            break
                        elif k.find('College')!=-1:
                            tabla_art_ins.append([cont, ins[ins.index(k)], pais])
                            i_aux.append(ins[ins.index(k)])
                            break
                        elif k.find('School')!=-1:
                            tabla_art_ins.append([cont, ins[ins.index(k)], pais])
                            i_aux.append(ins[ins.index(k)])
                            break
                        elif k.find('Politec')!=-1:
                            tabla_art_ins.append([cont, ins[ins.index(k)], pais])
                            i_aux.append(ins[ins.index(k)])
                            break
                        elif k.find('Research')!=-1:
                            tabla_art_ins.append([cont, ins[ins.index(k)], pais])
                            i_aux.append(ins[ins.index(k)])
                            break
                    if len(tabla_art_ins) == aux1:#Si sigue igual es porque no añadió nada
                        tabla_art_ins.append([cont, ins[0], pais])
            cont=cont+1

        for m in range(len(tabla_art_ins)):
            a=tabla_art_ins[m][2] in i_aux
            if a == True:
                tabla_art_ins[m][2]="[No disponible]"

              

        baseDatos.INSTITUCION_ARTICULO=pd.DataFrame(tabla_art_ins)
        baseDatos.INSTITUCION_ARTICULO=baseDatos.INSTITUCION_ARTICULO.rename(columns={0:'ID_art', 1:'Nombre_institucion', 2 : 'pais'})
        baseDatos.INSTITUCION_ARTICULO=baseDatos.INSTITUCION_ARTICULO.drop_duplicates()
        baseDatos.INSTITUCION_ARTICULO.reset_index(drop=True, inplace=True)
        baseDatos.INSTITUCION_ARTICULO=baseDatos.INSTITUCION_ARTICULO.rename_axis('ID_institucion_art')
        
        codigos=[]
        paises=[]
        for pais in baseDatos.INSTITUCION_ARTICULO.pais:
            pais=str(pais)
            aux=pais.split("; ")
            codigos.append(aux[0])
            paises.append(aux[-1])
        
        baseDatos.PAIS = pd.DataFrame(list(OrderedDict.fromkeys(baseDatos.INSTITUCION_ARTICULO.pais.tolist())))
        baseDatos.PAIS['Codigo'] = list(OrderedDict.fromkeys(codigos))
        baseDatos.PAIS['Nombre_pais'] = list(OrderedDict.fromkeys(paises))
        baseDatos.PAIS=baseDatos.PAIS.rename(columns={0:'Pais'})
        baseDatos.PAIS=baseDatos.PAIS.rename_axis('ID_pais')
        
        indices=[]
        for j in baseDatos.INSTITUCION_ARTICULO.pais:
            indices.append([baseDatos.PAIS.index[baseDatos.PAIS['Pais']==j]][0][0])
        baseDatos.INSTITUCION_ARTICULO['ID_pais']=indices
        baseDatos.INSTITUCION=pd.DataFrame(baseDatos.INSTITUCION_ARTICULO, columns={'Nombre_institucion', 'ID_pais'})
        baseDatos.INSTITUCION=baseDatos.INSTITUCION.drop_duplicates('Nombre_institucion')
        baseDatos.INSTITUCION=baseDatos.INSTITUCION.rename_axis('ID_institucion')
        baseDatos.INSTITUCION=baseDatos.INSTITUCION.fillna("[No disponible]")

        #baseDatos.INSTITUCION=pd.DataFrame(baseDatos.INSTITUCION, columns={'ID_institucion', 'Nombre_institucion', 'ID_pais'})

        indices=[]
        for j in baseDatos.INSTITUCION_ARTICULO.Nombre_institucion:
            indices.append([baseDatos.INSTITUCION.index[baseDatos.INSTITUCION['Nombre_institucion']==j]][0][0])
        baseDatos.INSTITUCION_ARTICULO['ID_institucion']=indices
        
        baseDatos.INSTITUCION_ARTICULO=pd.DataFrame(baseDatos.INSTITUCION_ARTICULO, columns={'ID_art', 'ID_institucion'})
        baseDatos.PAIS=pd.DataFrame(baseDatos.PAIS, columns={'Codigo', 'Nombre_pais'})
        
        return
    #Creación tablas financiamiento
    def tablas_financiamiento(self):
        fin=baseDatos.completo.financiamiento.tolist()
        finan=[]
        cont=0
        
        for j in fin:
            if j != '[No disponible]' and j !='[No disponible]|[No disponible]':
                if cont < len(baseDatos.wos.index):
                    f=j.split('; ')
                    for i in f:
                        i=str(i)
                        aux, acro, num='','',''
                        if i.find('[')!=-1:
                            ini=i.index('[')
                            fin=i.index(']')
                            for l in range(ini+1, fin):
                                aux+=i[l]
                            num=aux        
                            i=i.replace(i[ini]+aux+i[fin], '')
                            
                            aux=''
                        if i.find('(')!=-1:
                            ini=i.index('(')
                            fin=i.index(')')
                            for l in range(ini+1, fin):
                                aux+=i[l]
                            acro=aux
                            i=i.replace(i[ini]+aux+i[fin], '')
                            aux=''
                        finan.append([cont, i, num,  acro])
                if cont>len(baseDatos.wos.index)+len(baseDatos.scielo.index):
                    sponsor=j.split('|') #es porque está en scopus y separa instituciones|sponsor

                    for i in range(len(sponsor)):
                        if i == 0:
                            #if sponsor[i].find("; "): f=sponsor[i].split('; ')
                            f=sponsor[i]
                            f = f.replace(u'\xa0', u' ')
                            f=f.split('; ') #bien
                            for n in f:
                                if len(f)==1: n=f
                                n=str(n)
                                n=n.replace("['",'')
                                n=n.replace("']",'')
                                n=n.replace('["','')
                                n=n.replace('"]','')
                                aux=n.split(": ")#dos puntos es porque después está el número que se va a omitir, solo se trabajará con la primera posición
                                n=aux[0]

                                if n.find(", ")==-1: #si no hay , entonces solo hay un registro
                                    if re.compile("[A-Z]+").fullmatch(n) or re.compile("[A-Z0-9-/_‐. ]+").fullmatch(n): #la primera es para encontrar acronimos la segunda numeros, no cuenta cuando elnumero tiene minusculas. Esto lo q ue hace es descartarlas.
                                        continue
                                    else:         
                                        finan.append([cont,n,"[No disponible]", "[No disponible]"]) #mete la insitución y rellena con...
                                else: #si tiene comas entonces
                                    num="[No disponible]"
                                    name="[No disponible]"
                                    acro="[No disponible]"
                                    ins_a=n.split(', ')#separa comas
                                    for k in ins_a:
                                        k=str(k)
                                        if re.compile("[A-Z0-9-/ ]+").fullmatch(k) or re.compile("[A-Z]+").fullmatch(k) : #No toma acronimos con espacio  debo contar si la mayoria es mayuscula o minuscula para saber si es acro o num
                                            acro=k                
                                        elif ins_a[0]==k: #el nombre de la institucion de financiamiento está en la primera posición
                                            name=k
                                    if name!="[No disponible]": finan.append([cont,name, num, acro])
                            
                    """ f=sponsor[1].split(';') #falta la parte del sponsor.
                    f=str(f)
                    for 
                    if f.find("(")!=-1:
                        print("hay parentesis")
                    else """

            else: 
                finan.append([cont, '[No disponible]', '[No disponible]', '[No disponible]'])
            cont+=1
        #df=df.isin([0, 2]).drop() posible forma de eliminar
        baseDatos.FINANCIAMIENTO_ARTICULO = pd.DataFrame(finan)
        baseDatos.FINANCIAMIENTO_ARTICULO =  baseDatos.FINANCIAMIENTO_ARTICULO.rename(columns={0:'ID_art', 1:'Institucion', 2:'Numero', 3:'Acronimo'})
        print(baseDatos.FINANCIAMIENTO_ARTICULO)
        baseDatos.FINANCIAMIENTO = pd.DataFrame(finan)
        baseDatos.FINANCIAMIENTO =  baseDatos.FINANCIAMIENTO.rename(columns={0:'ID_art', 1:'Institucion', 2:'Numero', 3:'Acronimo'})
        baseDatos.FINANCIAMIENTO = baseDatos.FINANCIAMIENTO.sort_values('Institucion',0,ascending=True)
        baseDatos.FINANCIAMIENTO=pd.DataFrame(baseDatos.FINANCIAMIENTO, columns=['Institucion', 'Acronimo'])
        baseDatos.FINANCIAMIENTO = baseDatos.FINANCIAMIENTO.rename_axis('ID_fin')
        baseDatos.FINANCIAMIENTO = baseDatos.FINANCIAMIENTO.drop_duplicates()
        

        indices=[]
        for j in baseDatos.FINANCIAMIENTO_ARTICULO.Institucion:
            indices.append([baseDatos.FINANCIAMIENTO.index[baseDatos.FINANCIAMIENTO['Institucion']==j]][0][0])
        baseDatos.FINANCIAMIENTO_ARTICULO['ID_fin']=indices
        baseDatos.FINANCIAMIENTO_ARTICULO=pd.DataFrame(baseDatos.FINANCIAMIENTO_ARTICULO, columns=['ID_art', 'ID_fin'])
        baseDatos.FINANCIAMIENTO_ARTICULO= baseDatos.FINANCIAMIENTO_ARTICULO.rename_axis('ID_fin_art')



    #Creación de la base de datos
    def descargas(self):
        import Modelo as md
        baseDatos.md=md
               
        baseDatos.engine = create_engine(md.archivo)
        

        baseDatos.ARTICULO.to_sql("ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.BDKEY_ARTICULO.to_sql("BDKEY_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.BDKEYWORD.to_sql("BDKEYWORD", con=baseDatos.engine, if_exists="append")
        baseDatos.CATEGORIA_ARTICULO.to_sql("CATEGORIA_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.CATEGORIA.to_sql("CATEGORIA", con=baseDatos.engine, if_exists="append")
        baseDatos.SUB_CATEGORIA.to_sql("SUB_CATEGORIA", con=baseDatos.engine, if_exists="append")
        baseDatos.AUTOR.to_sql("AUTOR", con=baseDatos.engine, if_exists="append")
        baseDatos.AUTOR_ARTICULO.to_sql("AUTOR_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.AU_KEYWORD.to_sql("AU_KEYWORD", con=baseDatos.engine, if_exists="append")
        baseDatos.AUKEY_ARTICULO.to_sql("AUKEY_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.FUENTE.to_sql("FUENTE", con=baseDatos.engine, if_exists="append")
        baseDatos.OA_ARTICULO.to_sql("OA_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.OPEN_ACCESS.to_sql("OPEN_ACCESS", con=baseDatos.engine, if_exists="append")
        baseDatos.INSTITUCION_ARTICULO.to_sql("INSTITUCION_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.INSTITUCION.to_sql("INSTITUCION", con=baseDatos.engine, if_exists="append")
        baseDatos.PAIS.to_sql("PAIS", con=baseDatos.engine, if_exists="append")
        baseDatos.FINANCIAMIENTO_ARTICULO.to_sql("FINANCIAMIENTO_ARTICULO", con=baseDatos.engine, if_exists="append")
        baseDatos.FINANCIAMIENTO.to_sql("FINANCIAMIENTO", con=baseDatos.engine, if_exists="append")