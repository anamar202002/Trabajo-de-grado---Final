from tkinter import filedialog
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
archivo=''

#cada clase crea una tabla diferente con sus atributos
class articulo (Base):
    __tablename__ = "ARTICULO"
    ID_art = Column(Integer, primary_key=True)
    Titulo = Column(String)
    ID_fuente = Column(Integer, ForeignKey("FUENTE.ID_fuente", ondelete="CASCADE"))
    Resumen = Column(String)
    Citas_recibidas = Column(String)
    DOI = Column(String)
    Editorial = Column(String)
    Base_de_datos = Column(String)
    Idioma = Column(String)
    Num_acceso=Column(String)
    Tipo_de_documento=Column(String)
    Anio = Column(Integer)


#Financiamiento
class financiamiento_articulo(Base):
    __tablename__="FINANCIAMIENTO_ARTICULO"
    ID_fin_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_fin = Column(Integer, ForeignKey("FINANCIAMIENTO.ID_fin", ondelete="CASCADE"))

class financiamiento(Base):
    __tablename__="FINANCIAMIENTO"
    ID_fin = Column(Integer, primary_key=True)
    Institucion = Column(String)
    Acronimo = Column(String)
    

#Institución y país
class institucion_articulo(Base):
    __tablename__="INSTITUCION_ARTICULO"
    ID_institucion_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_institucion = Column(Integer, ForeignKey("INSTITUCION.ID_institucion", ondelete="CASCADE"))

class institucion (Base):
    __tablename__="INSTITUCION"
    ID_institucion = Column(Integer, primary_key=True)
    Nombre_institucion = Column(String)
    ID_pais = Column(Integer, ForeignKey("PAIS.ID_pais", ondelete="CASCADE"))

class pais (Base):
    __tablename__="PAIS"
    ID_pais = Column(Integer, primary_key=True)
    Codigo = Column(String)
    Nombre_pais = Column(String)

#Palabra clave de la base de datos 
class bdKey_articulo (Base):
    __tablename__="BDKEY_ARTICULO"
    ID_bdKey_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_bdKey = Column(Integer, ForeignKey("BDKEYWORD.ID_bdKey", ondelete="CASCADE"))

class bdKeyword (Base):
    __tablename__="BDKEYWORD"
    ID_bdKey = Column(Integer, primary_key=True)
    BD_keyword = Column(String)

#Categorias y subcategorias

class categoria_articulo (Base):
    __tablename__="CATEGORIA_ARTICULO"
    ID_cat_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_cat = Column(Integer, ForeignKey("CATEGORIA.ID_cat", ondelete="CASCADE"))
    ID_subcat = Column(Integer, ForeignKey("SUB_CATEGORIA.ID_subcat", ondelete="CASCADE"))

class categoria (Base):
    __tablename__="CATEGORIA"
    ID_cat = Column(Integer, primary_key=True)
    Nombre_categoria = Column(String)

class sub_categoria(Base):
    __tablename__="SUB_CATEGORIA"
    ID_subcat = Column(Integer, primary_key=True)
    Nombre_subcategoria = Column(String)

#Autor

class autor_articulo (Base):
    __tablename__="AUTOR_ARTICULO"
    ID_aut_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_au = Column(Integer, ForeignKey("AUTOR.ID_au", ondelete="CASCADE"))

class autor (Base):
    __tablename__="AUTOR"
    ID_au = Column(Integer, primary_key=True)
    Nombre_autor = Column(String)

#Palabras clave del autor

class auKey_articulo (Base):
    __tablename__="AUKEY_ARTICULO"
    ID_aukey_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_aukey = Column(Integer, ForeignKey("AU_KEYWORD.ID_auKey", ondelete="CASCADE"))

class auKey (Base):
    __tablename__="AU_KEYWORD"
    ID_auKey = Column(Integer, primary_key=True)
    Autor_keyword = Column(String)

#Revista o libro
class fuente (Base):
    __tablename__="FUENTE"
    ID_fuente = Column(Integer, primary_key=True)
    Nombre_fuente = Column(String)
    ISSN = Column(String)
    eISSN = Column(String)
    ISBN = Column(String)

#Open access

class oa_articulo (Base):
    __tablename__="OA_ARTICULO"
    ID_oa_art = Column(Integer, primary_key=True)
    ID_art = Column(Integer, ForeignKey("ARTICULO.ID_art", ondelete="CASCADE"))
    ID_oa = Column(Integer, ForeignKey("OPEN_ACCESS.ID_oa", ondelete="CASCADE"))

class open_access (Base):
    __tablename__="OPEN_ACCESS"
    ID_oa = Column(Integer, primary_key=True)
    Tipo_oa = Column(String)



#Se ejecuta cuándo se importa la clase, permite guardar el modelo de datos .db dentro del lugar que desea el usuario, crea el motor y guarda lo que se hizo anteriormente
if __name__ != "__main__": #lo voy a ejecutar desde otro lugar
    archivo = filedialog.asksaveasfilename(title='Guardar base de datos...', defaultextension='.db', filetypes=[('Base de datos', '*.db')]) #va título, directorio de inicio (raíz) tipos que soporta //  initialdir='/', para inicializar el directorio en el puro inicio
    if not archivo.endswith('.db'):
            archivo += '.db'
    archivo=str(archivo)

    archivo=archivo.replace('/', '\\')        
    archivo='sqlite:///'+archivo
    engine = create_engine(archivo, echo=True)
    Base.metadata.create_all(engine)