import webbrowser 
from baseDatos import baseDatos
from tkinter import BOTH, Frame, Tk, Toplevel, ttk, Label, Button, CENTER
import tkinter
from PIL import ImageTk, Image


class program (Tk):
    def __init__(self):        
        super(program, self).__init__()
        
    def bienvenida(self):
        self.iconify()
        self.v_selector = Toplevel(self)#Será una ventana emergente
        self.v_selector.title('Bienvenida')#Título de la ventana
        self.v_selector.geometry('450x550') #Tamaño de la ventana

        Label(self.v_selector, text="Bienvenid@", font=("Verdana",20)).pack(pady=15)
        Label(self.v_selector, text="Bienvenid@ a XXXXX un programa que facilitará la labor investigativa \na la hora de analizar documentos para la realización de estados \ndel arte y/o ejercicios bibliométricos.").pack(padx=30)
        Label(self.v_selector, text="Dentro de XXXXX existirán diferentes funcionalidades como: \npoder exportar todas las tablas a un Excel si se quiere \ntener más comodidad, permite filtrar con doble clic en los \nregistros de varias tablas para poder ver los título de los documentos, \ncontiene leyes bibliométricas como lo son “Bradford y Lotka”, \nnubes de palabras con las palabras claves, \nmapa coroplético de la producción por países y demás \ngráficos útiles para el análisis de los documentos.\n\n\n El primer paso es seleccionar los archivos \nde Web of Sciences, Scopus y Scielo. \nDespués pedirá guardar la base de datos en un \narchivo .db donde se encuentra la información de los registros. \n ¡Y listo, ya puedes empezar a usar XXXX!").pack(padx=30, pady=6)
        Button(self.v_selector, text='¿Cómo ingresar los datos?', command=self.datos).pack(padx=60, pady=10)
        Button(self.v_selector, text='Continuar al selector de archivos', command=self.selector_archivos).pack(padx=60)
        
    def datos(self):
        self.v_selector.geometry('1000x650') #Tamaño de la ventana
        self.v_selector.configure(bg='lightblue1')
        self.clearFrame(self.v_selector)
        Label(self.v_selector, text="Para saber cómo exportar los archivos seleccione la base de datos desea utilizar y siga los pasos").pack(padx=60, pady=25)
        Button(self.v_selector, text='Web of Science \nScielo', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_wos.png"), 
            Button(self.v_selector, text='Siguiente', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_wos1.png"), 
            Button(self.v_selector, text='Siguiente', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_wos2.png"),
            Button(self.v_selector, text='Siguiente', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_wos3.png"), 
            Button(self.v_selector, text='¿Cómo ingresar los datos?', command=self.datos).pack(padx=60, pady=25)
            ]).pack(padx=60, pady=25)]).pack(padx=60, pady=25)]).pack(padx=60, pady=25)]).pack(padx=60, pady=25)
        Button(self.v_selector, text='Scopus', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_scopus.png"), 
            Button(self.v_selector, text='Siguiente', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_scopus1.png"), 
            Button(self.v_selector, text='Siguiente', command=lambda:[self.clearFrame(self.v_selector), self.imagenes(self.v_selector, "ex_scopus2.png"),
            Button(self.v_selector, text='¿Cómo ingresar los datos?', command=self.datos).pack(padx=60, pady=25)
            ]).pack(padx=60, pady=25)]).pack(padx=60, pady=25)]).pack(padx=60, pady=25)
        
        Button(self.v_selector, text='Continuar al selector de archivos', command=self.selector_archivos).pack(padx=60, pady=25)

        

    def selector_archivos(self):
        #botones iniciales para la carga de los documentos.
        self.clearFrame(self.v_selector)
        self.v_selector.configure(bg='lightblue1')
        self.v_selector.geometry('350x350') #Tamaño de la ventana
        #Se crea una instancia de la clase base de datos para poder acceder a sus métodos y atributos
        Button(self.v_selector, text='Seleccione el archivo de Web of Science', command=lambda:[baseDatos.ejecutar_wos(baseDatos)]).pack(padx=60, pady=25)
        Button(self.v_selector, text='Seleccione el archivo de Scopus', command=lambda:[baseDatos.ejecutar_scopus(baseDatos)]).pack(padx=60, pady=25)
        Button(self.v_selector, text='Seleccione el archivo de Scielo', command=lambda:[baseDatos.ejecutar_scielo(baseDatos)]).pack(padx=60, pady=25)
        Button(self.v_selector, text='Continuar', command=lambda:[baseDatos.concatenar(baseDatos),self.inicializa(), self.v_selector.destroy()]).pack(padx=60, pady=25)

    def inicializa (self):
        from Funcionalidades import autores, revistas, instituciones, palabras, pais, general
        import Funcionalidades
        from consultas import consulta
        self.funcionalidades=Funcionalidades
        self.c=consulta
        self.autores=autores
        self.instituciones=instituciones
        self.revistas=revistas
        self.palabra=palabras
        self.paises=pais
        self.general=general


        self.state("zoomed")
               
        pestañas_f=Frame(self, bg="cornflower blue")
        pestañas_f.place(relheight=0.1, relwidth=1, relx=0, rely=0.9)
        self.principal_f=Frame(self)
        self.principal_f.place(relx=0, rely=0, relheight=0.9, relwidth=1)
        
        
        ttk.Button(pestañas_f, text="Corpus documental", command=lambda:[self.clearFrame(self.principal_f), self.corpus_documental()]).place(relwidth=0.1, relheight=0.4, relx=0.02, rely=0.2) #comando para el predeterminado, tendrá las columnas más relevantes y la opción de seleccionar las columnas deseadas de TODAS las tablas
        
        ttk.Button(pestañas_f, text="Artículos", command=lambda:[self.clearFrame(self.principal_f), self.pasar_tabla('SELECT * FROM ARTICULO', self.principal_f, "Artículos")]).place(relwidth=0.1, relheight=0.4, relx=0.13, rely=0.2) #comando para mostrar la tabla de articulos  "ARTICULO"
        ttk.Button(pestañas_f, text="Autores e instituciones", command=lambda:[self.clearFrame(self.principal_f), self.graficos_autores_instituciones()]).place(relwidth=0.1, relheight=0.4, relx=0.24, rely=0.2) #comando para mostrar los autores
        ttk.Button(pestañas_f, text="Revistas", command=lambda:[self.clearFrame(self.principal_f), self.graficos_revistas()]).place(relwidth=0.1, relheight=0.4, relx=0.35, rely=0.2) #comando para mostrar los autores
        ttk.Button(pestañas_f, text="Palabras", command=lambda:[self.clearFrame(self.principal_f), self.palabras()]).place(relwidth=0.1, relheight=0.4, relx=0.46, rely=0.2) #comando para mostrar los autores
        ttk.Button(pestañas_f, text="Paises", command=lambda:[self.clearFrame(self.principal_f), self.mapa()]).place(relwidth=0.1, relheight=0.4, relx=0.57, rely=0.2) #comando para mostrar los paises en un mapa
        ttk.Button(pestañas_f, text="Graficos general", command=lambda:[self.clearFrame(self.principal_f), self.graficos_general()]).place(relwidth=0.1, relheight=0.4, relx=0.68, rely=0.2) #comando para mostrar los paises en un mapa

    def corpus_documental(self):
        titulo=Frame(self.principal_f)
        titulo.place(relwidth=1, relheight=0.1, relx=0, rely=0.01)
        
        texto = tkinter.StringVar()
        texto.set("Corpus documental")        
        Label(titulo, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)


        modelo_f=Frame(self.principal_f)
        modelo_f.place(relwidth=0.7, relheight=1-0.16, relx=0.27, rely=0.12)

        self.opc_f=Frame(self.principal_f, bg="lightblue1")
        self.opc_f.place(relwidth=0.25, relheight=0.94, relx=0.025, rely=0.015)
        self.imagenes(modelo_f, "modelo.png")
        Button(self.opc_f, text="Modelo entidad-relación \n (utilizado para la creación \n de la base de datos) ", command=lambda:[self.clearFrame(modelo_f), self.imagenes(modelo_f, "modelo.png")]).pack(padx=10, pady=20, ipadx=10, ipady=10)
        Label(self.opc_f, text="Los registros para cada base de datos son los siguientes:", bg="lightblue1").pack()
        texto.set("Web of Science con "+str(len(baseDatos.wos))+ " registros")
        Button(self.opc_f, text=texto.get(), command=lambda:[self.clearFrame(modelo_f), self.tabla(modelo_f, baseDatos.wos, "Web of Science")]).pack(padx=10, pady=10, ipadx=10, ipady=5)
        texto.set("Scopus con "+str(len(baseDatos.scopus))+ " registros")
        Button(self.opc_f, text=texto.get(), command=lambda:[self.clearFrame(modelo_f), self.tabla(modelo_f, baseDatos.scopus, "Scopus")]).pack(padx=10, pady=10, ipadx=10, ipady=5)
        texto.set("Scielo con "+str(len(baseDatos.scielo))+ " registros")
        Button(self.opc_f, text=texto.get(), command=lambda:[self.clearFrame(modelo_f), self.tabla(modelo_f, baseDatos.scielo, "Scielo")]).pack(padx=10, pady=10, ipadx=10, ipady=5)
        Label(self.opc_f, text="Tras unión de todos los registros quedó: ", bg="lightblue1").pack()
        texto.set("Un archivo compilado con "+str(len(baseDatos.completo))+ " registros")
        Button(self.opc_f, text=texto.get(), command=lambda:[self.clearFrame(modelo_f), self.tabla(modelo_f, baseDatos.completo, "Completo")]).pack(padx=10, pady=10, ipadx=10, ipady=5)
        
        Button(self.opc_f, text="Continuar a la limpieza ", command=lambda:[
            self.clearFrame(self.opc_f),
            Label(self.opc_f, text="Tras la limpieza de los datos se logran recuperar : ", bg="lightblue1").pack(padx=10, pady=10, ipadx=10, ipady=5),
            texto.set("•"+str(len(baseDatos.INSTITUCION))+ " instituciones pertenecientes a " + str(len(self.c.df_consulta(self.c, "SELECT DISTINCT Titulo  from INSTITUCION, INSTITUCION_ARTICULO, ARTICULO WHERE INSTITUCION.ID_institucion = INSTITUCION_ARTICULO.ID_institucion and ARTICULO.ID_art = INSTITUCION_ARTICULO.ID_art AND INSTITUCION.Nombre_institucion != '[No disponible]'")))+ " registros"),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.AUTOR))+ " autores"),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.PAIS)-1)+ " paises pertenecientes a " + str(len(self.c.df_consulta(self.c, "SELECT DISTINCT Nombre_institucion from INSTITUCION, PAIS WHERE INSTITUCION.ID_pais= PAIS.ID_pais AND PAIS.Nombre_pais !=  '[No disponible]'")))+ " instituciones, \n no se recuperaron todos los paises \n de las instituciones por datos incompletos"),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.CATEGORIA))+ " categorias (Scopus no tiene categorías)" ),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.SUB_CATEGORIA))+ " subcategorias (Web of Science \n es el único con subcategorías)" ),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.AU_KEYWORD))+ " palabras clave del autor" ),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.BDKEYWORD))+ " palabras clave de la base de datos" ),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.FINANCIAMIENTO)-1)+ " patrocinadores pertenecientes a " + str(len(self.c.df_consulta(self.c, "SELECT DISTINCT Titulo from FINANCIAMIENTO_ARTICULO, ARTICULO, FINANCIAMIENTO where FINANCIAMIENTO_ARTICULO.ID_art = ARTICULO.ID_art AND FINANCIAMIENTO.ID_fin = FINANCIAMIENTO_ARTICULO.ID_fin AND FINANCIAMIENTO.Institucion != '[No disponible]'"))) + " registros"),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.FUENTE)) + " revistas"),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),
            texto.set("•"+str(len(baseDatos.OPEN_ACCESS)) + " tipos de acceso abierto"),
            Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10),

            Button(self.opc_f, text="Exportar todas las tablas \n del modelo a archivos de excel", command=self.exportar).pack(padx=10, pady=20, ipadx=10, ipady=10),
            Button(self.opc_f, text="Atras", command=self.corpus_documental).pack(padx=10, pady=20)
        ]).pack(padx=10, pady=10, ipadx=10, ipady=10)
   
    def exportar(self):
        texto = tkinter.StringVar()
        texto.set(self.funcionalidades.guardar_modelo_excel()) 
        txt = tkinter.Text(self.opc_f, height=20)
        txt.insert(1.0, texto.get())
        txt.pack(anchor="w", padx=10)
        txt.configure(bg=self.opc_f.cget('bg'), relief="flat")
        txt.configure(state="disabled")
        #Label(self.opc_f, text=texto.get(), bg="lightblue1").pack(anchor="w", padx=10)


    
    def imagenes(self, frame, nombregraf:str):
        self.p=nombregraf
        img=Image.open(nombregraf)
        if nombregraf == "modelo.png":
            img=img.resize((int(self.winfo_width()*0.7), int(((self.winfo_height()*0.87)*0.84))), Image.Resampling.LANCZOS)
        img=ImageTk.PhotoImage(img)
        panel=Label(frame, image=img)
        panel.image=img
        panel.place(relx=0, rely=0, relheight=1, relwidth=1)

    def pasar_tabla(self, con, frame, titulo):
        self.c.df_consulta(self.c, con)
        self.tabla(frame, self.c.df, titulo)
   
    def graficos_autores_instituciones(self):
        
        self.clearFrame(self.principal_f)
        titulo1=Frame(self.principal_f)
        titulo1.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.01)
        
        texto = tkinter.StringVar()
        texto.set("Instituciones más productivas")        
        Label(titulo1, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)


        titulo2=Frame(self.principal_f)
        titulo2.place(relwidth=0.4, relheight=0.1, relx=0.55, rely=0.01)

        texto.set("Autores más productivos")        
        Label(titulo2, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)

        linea=Frame(self.principal_f, bg="black")
        linea.place(relwidth=0.001, relheight=1, relx=0.5, rely=0)
        graf2=Frame(self.principal_f)
        graf2.place(relwidth=0.45, relheight=1-0.16, relx=0.525, rely=0.12)

        graf1=Frame(self.principal_f)
        graf1.place(relwidth=0.45, relheight=1-0.16, relx=0.025, rely=0.12)
        
        img = Image.open("institucionesMasProductivas.jpg")
        img=img.resize((int(self.winfo_width()*0.45), int(((self.winfo_height()*0.87)*0.84)*0.9)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
  
        panel = ttk.Button(graf1, image = img, command=lambda:[webbrowser.open("AutoresMasCitados.html")])        
        panel.image=img
        panel.place(relx=0, rely=0, relheight=0.9, relwidth=1)
        
        img = Image.open("AutoresMasProductivos.jpg")
        img=img.resize((int(self.winfo_width()*0.45), int(((self.winfo_height()*0.87)*0.84)*0.9)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf2, image = img, command=lambda:[webbrowser.open("AutoresMasProductivos.html")])        
        panel.image=img
        panel.place(relx=0, rely=0, relheight=0.9, relwidth=1)
        
        img = Image.open("tabla.png")
        img=img.resize((int((self.winfo_width()*0.45)*0.1), int(((self.winfo_height()*0.87)*0.84)*0.1)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel = ttk.Button(graf2, image = img, command=lambda:[self.tabla_ventana_emergente(self.autores.df_au_pro, "Producción por autor")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0.9, rely=0.9, relheight=0.1, relwidth=0.1)
              
        panel = ttk.Button(graf1, image = img, command=lambda:[self.tabla_ventana_emergente(self.instituciones.df_ins_pro, "Producción por institución")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0.9, rely=0.9, relheight=0.1, relwidth=0.1)

        lotka_b=ttk.Button(self.principal_f, text="->", command=self.lotka)
        lotka_b.place(rely=0.45, relx=0.98, relheight=0.15, relwidth=0.02)

    def lotka(self):
        self.clearFrame(self.principal_f)
        titulo=Frame(self.principal_f)
        titulo.place(relwidth=1, relheight=0.1, relx=0, rely=0.01)
        
        texto = tkinter.StringVar()
        texto.set("Lotka")        
        Label(titulo, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)


        linea=Frame(self.principal_f, bg="black")
        linea.place(relwidth=0.001, relheight=1, relx=0.5, rely=0.1)
        self.graf2=Frame(self.principal_f)
        self.graf2.place(relwidth=0.45, relheight=1-0.16, relx=0.525, rely=0.12)

        self.graf1=Frame(self.principal_f)
        self.graf1.place(relwidth=0.45, relheight=1-0.16, relx=0.025, rely=0.12)
        
        atras=ttk.Button(self.principal_f, text="<-", command=self.graficos_autores_instituciones)
        atras.place(rely=0.45, relx=0, relheight=0.15, relwidth=0.02)

        img = Image.open("Lotka.jpg")
        img=img.resize((int(self.winfo_width()*0.45), int(((self.winfo_height()*0.87)*0.84)*0.7)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)


        panel = ttk.Button(self.graf1, image = img, command=lambda:[webbrowser.open("Lotka.html")])        
        panel.image=img
        panel.place(relx=0, rely=0, relheight=0.7, relwidth=1)

        tabla_f = Frame(self.graf1)
        tabla_f.place(relx=0.5, rely=0.7, relheight=0.3, relwidth=0.5)
        self.tabla(tabla_f, self.autores.df_lotka, 0)



        trabajos = tkinter.Entry(self.graf1, width=25)
        trabajos.place(relx=0.2, rely=0.8, relheight=0.03, relwidth=0.1)
        tkinter.Label(self.graf1,text=f'Digite la cantidad de trabajos para saber cuántos \n autores lo han publicado').place(relx=0, rely=0.72)
        Button(self.graf1, text="Calcular", command=lambda:[tkinter.Label(self.graf1, text=self.autores.calculo_lotka(self.autores, int(trabajos.get()))).place(relx=0, rely=0.88, relheight=0.05, relwidth=0.5)]).place(relx=0.2, rely=0.84, relheight=0.03, relwidth=0.1)

        tkinter.Label(self.graf2, text="SE VA EXPLICAR DE QUÉ TRATA LA LEY DE LOTKA").place(relx=0, rely=0, relheight=0.4, relwidth=1)
        tkinter.Label(self.graf2, text="AUTORES ÉLITE").place(relx=0, rely=0.41, relheight=0.05, relwidth=0.5)
        tkinter.Label(self.graf2, text="ARTÍCULOS DEL AUTOR: ").place(relx=0.5, rely=0.41, relheight=0.05, relwidth=0.3)

        f_au_elite=Frame(self.graf2)
        f_au_elite.place(relx=0.01, rely=0.5, relheight=0.5, relwidth=0.48)
        self.tv_elite=self.tabla(f_au_elite, self.autores.df_au_elite, 0)
        self.tv_elite.bind("<Double-1>", self.click_elite)
        
        self.f_au_art=Frame(self.graf2)
        self.f_au_art.place(relx=0.51, rely=0.5, relheight=0.5, relwidth=0.48)
        tkinter.Label(self.graf1,text=f'Estos calculos que Lotka propusó serán más exáctos \n cuando se está analizando una temática específica').place(relx=0, rely=0.9)

    def click_elite(self, e):
        item = self.tv_elite.selection()
        self.autores.filtro(self.autores, self.tv_elite.item(item, "values")[0])
        self.tabla(self.f_au_art, self.autores.filtrado_df, 0)
        tkinter.Label(self.graf2, text=self.tv_elite.item(item, "values")[0]).place(relx=0.8, rely=0.41, relheight=0.05, relwidth=0.2)
    
        

    def graficos_revistas(self):
        
        self.clearFrame(self.principal_f)
        titulo1=Frame(self.principal_f)
        titulo1.place(relwidth=0.4, relheight=0.1, relx=0.05, rely=0.01)
        
        texto = tkinter.StringVar()
        texto.set("Revistas más citadas")        
        Label(titulo1, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)


        titulo2=Frame(self.principal_f)
        titulo2.place(relwidth=0.4, relheight=0.1, relx=0.55, rely=0.01)

        texto.set("Revistas más productivas")        
        Label(titulo2, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)

        linea=Frame(self.principal_f, bg="black")
        linea.place(relwidth=0.001, relheight=1, relx=0.5, rely=0)
        graf2=Frame(self.principal_f)
        graf2.place(relwidth=0.45, relheight=1-0.16, relx=0.525, rely=0.12)

        graf1=Frame(self.principal_f)
        graf1.place(relwidth=0.45, relheight=1-0.16, relx=0.025, rely=0.12)
        
        img = Image.open("RevistasMasCitados.jpg")
        img=img.resize((int(self.winfo_width()*0.45), int(((self.winfo_height()*0.87)*0.84)*0.9)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
  
        panel = ttk.Button(graf1, image = img, command=lambda:[webbrowser.open("RevistasMasCitados.html")])        
        panel.image=img
        panel.place(relx=0, rely=0, relheight=0.9, relwidth=1)
        
        img = Image.open("RevistasMasProductivos.jpg")
        img=img.resize((int(self.winfo_width()*0.45), int(((self.winfo_height()*0.87)*0.84)*0.9)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf2, image = img, command=lambda:[webbrowser.open("RevistasMasProductivos.html")])        
        panel.image=img
        panel.place(relx=0, rely=0, relheight=0.9, relwidth=1)
        
        img = Image.open("tabla.png")
        img=img.resize((int((self.winfo_width()*0.45)*0.1), int(((self.winfo_height()*0.87)*0.84)*0.1)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel = ttk.Button(graf2, image = img, command=lambda:[self.tabla_ventana_emergente(self.revistas.df_rev_pro, "Producción por revista")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0.9, rely=0.9, relheight=0.1, relwidth=0.1)
              
        panel = ttk.Button(graf1, image = img, command=lambda:[self.tabla_ventana_emergente(self.revistas.df_rev_cit, "Citación por revista")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0.9, rely=0.9, relheight=0.1, relwidth=0.1)

        bradford_b=ttk.Button(self.principal_f, text="->", command=self.bradford)
        bradford_b.place(rely=0.45, relx=0.98, relheight=0.15, relwidth=0.02)
    
    def bradford(self):
        self.clearFrame(self.principal_f)
        titulo=Frame(self.principal_f)
        titulo.place(relwidth=1, relheight=0.1, relx=0, rely=0.01)
        
        texto = tkinter.StringVar()
        texto.set("Ley de Bradford")        
        Label(titulo, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)


        linea=Frame(self.principal_f)
        linea.place(relwidth=0.001, relheight=1, relx=0.35, rely=0.13)
        self.graf2=Frame(self.principal_f)
        self.graf2.place(relwidth=0.6, relheight=1-0.16, relx=0.375, rely=0.12)

        self.graf1=Frame(self.principal_f)
        self.graf1.place(relwidth=0.3, relheight=1-0.16, relx=0.025, rely=0.12)
        
        atras=ttk.Button(self.principal_f, text="<-", command=self.graficos_revistas)
        atras.place(rely=0.45, relx=0, relheight=0.15, relwidth=0.02)

        zona3_b = Button(self.graf1, bg="lightblue1", command=lambda:[self.zona_tabla("Zona 3")])
        zona3_b.place(relheight=1, relwidth=1, relx=0, rely=0)

        zona2_b = Button(self.graf1, bg="CadetBlue2", command=lambda:[self.zona_tabla("Zona 2")])
        zona2_b.place(relheight=0.7, relwidth=0.7, relx=0.2, rely=0.25)

        zona1_b = Button(self.graf1, bg="CadetBlue3", command=lambda:[self.zona_tabla("Zona 1")])
        zona1_b.place(relheight=0.4, relwidth=0.4, relx=0.4, rely=0.5)
        #[revista, %, articulos, %]
        rev=str(self.revistas.zonas_b[2][0]) + " Revistas (" + str(self.revistas.zonas_b[2][1]) + "%)"
        art=str(self.revistas.zonas_b[2][2]) + " Artículos (" + str(self.revistas.zonas_b[2][3]) + "%)"
        Label(self.graf1, text=rev).place(relheight=0.05, relwidth=0.3, relx=0.06, rely=0.1)
        Label(self.graf1, text=art).place(relheight=0.05, relwidth=0.3, relx=0.06, rely=0.15)
        Label(self.graf1, text="Zona 3").place(relx=0.05, rely=0.05)

        rev=str(self.revistas.zonas_b[1][0]) + " Revistas (" + str(self.revistas.zonas_b[1][1]) + "%)"
        art=str(self.revistas.zonas_b[1][2]) + " Artículos (" + str(self.revistas.zonas_b[1][3]) + "%)"
        Label(self.graf1, text=rev).place(relheight=0.05, relwidth=0.3, relx=0.5, rely=0.35)
        Label(self.graf1, text=art).place(relheight=0.05, relwidth=0.3, relx=0.5, rely=0.4)
        Label(self.graf1, text="Zona 2").place(relx=0.3, rely=0.35)

        rev=str(self.revistas.zonas_b[0][0]) + " Revistas (" + str(self.revistas.zonas_b[0][1]) + "%)"
        art=str(self.revistas.zonas_b[0][2]) + " Artículos (" + str(self.revistas.zonas_b[0][3]) + "%)"
        Label(self.graf1, text=rev).place(relheight=0.05, relwidth=0.3, relx=0.55, rely=0.6)
        Label(self.graf1, text=art).place(relheight=0.05, relwidth=0.3, relx=0.55, rely=0.65)
        Label(self.graf1, text="Zona 1").place(relx=0.5, rely=0.55)

        tkinter.Label(self.graf2, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.").place(relx=0, rely=0, relheight=0.4, relwidth=1)
        tkinter.Label(self.graf2, text="REVISTAS ZONA: ").place(relx=0, rely=0.41, relheight=0.05, relwidth=0.3)
        tkinter.Label(self.graf2, text="ARTICULOS DE LA REVISTA: ").place(relx=0.5, rely=0.41, relheight=0.05, relwidth=0.2)

    def zona_tabla(self, zona):
        Label(self.graf2, text=zona).place(relx=0.3, rely=0.41, relheight=0.05, relwidth=0.2)
        f_revistas=Frame(self.graf2)
        f_revistas.place(relx=0.01, rely=0.5, relheight=0.5, relwidth=0.3)
        self.tv_revistas=self.tabla(f_revistas, self.revistas.filtro_zona(self.revistas, zona), 0)
        self.tv_revistas.bind("<Double-1>", self.click_revista)
        
        self.f_rev_art=Frame(self.graf2)
        self.f_rev_art.place(relx=0.32, rely=0.5, relheight=0.5, relwidth=0.68)

    def click_revista(self, e):
        item = self.tv_revistas.selection()
        self.revistas.filtro(self.revistas, self.tv_revistas.item(item, "values")[0])
        self.tabla(self.f_rev_art, self.revistas.filtrado_df, 0)
        tkinter.Label(self.graf2, text=self.tv_revistas.item(item, "values")[0]).place(relx=0.7, rely=0.41, relheight=0.05, relwidth=0.2)
        
    def palabras(self):
        titulo=Frame(self.principal_f)
        titulo.place(relwidth=1, relheight=0.1, relx=0, rely=0.01)
        
        texto = tkinter.StringVar()
        texto.set("Palabras clave")        
        Label(titulo, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)


        linea=Frame(self.principal_f)
        linea.place(relwidth=0.001, relheight=1, relx=0.25, rely=0.13)
        nube_f=Frame(self.principal_f)
        nube_f.place(relwidth=0.7, relheight=1-0.16, relx=0.27, rely=0.12)

        opc_f=Frame(self.principal_f)
        opc_f.place(relwidth=0.2, relheight=1-0.16, relx=0.025, rely=0.12)
     
        Button(opc_f, text="Autor (keywords)", command=lambda:[self.graficos(nube_f, "au_keys.png")]).place(relx=0.07, rely=0.05)
        Button(opc_f, text="Base de datos (keywords)", command=lambda:[self.graficos(nube_f, "bd_keys.png")]).place(relx=0.07, rely=0.1)

        self.t_palabras=Frame(opc_f)
        self.t_palabras.place(relx=0.05, rely=0.15, relheight=0.8, relwidth=0.9)
        
    def graficos(self, frame, nombregraf:str):
        self.p=nombregraf
        img=Image.open(nombregraf)
        img=img.resize((int(self.winfo_width()*0.7), int(((self.winfo_height()*0.87)*0.84))), Image.Resampling.LANCZOS)
        img=ImageTk.PhotoImage(img)
        panel=Label(frame, image=img)
        panel.image=img
        panel.place(relx=0, rely=0, relheight=1, relwidth=1)
        if self.p.find("au") != -1:
            self.tv_palabras=self.tabla(self.t_palabras, self.palabra.Autor_keyword, "Autor")
        elif self.p.find("bd")!=-1:
            self.tv_palabras=self.tabla(self.t_palabras, self.palabra.BD_keyword, "Base de datos")
        self.tv_palabras.bind("<Double-1>", self.click_palabra)

    def click_palabra(self, e):
        item = self.tv_palabras.selection()
        self.palabra.filtro(self.palabra, self.tv_palabras.item(item, "values")[0], self.p)
        self.tabla_ventana_emergente(self.palabra.filtrado_df, "Filtrado por :"+str(self.tv_palabras.item(item, "values")[0]))

    def mapa(self):

        self.titulo_f=Frame(self.principal_f)
        self.titulo_f.place(relwidth=0.6, relheight=0.1, relx=0.2, rely=0.01)
        Label(self.titulo_f, text="Producción por países", font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)

        
        graf=Frame(self.principal_f)
        graf.place(relheight=0.84, relwidth=0.96, relx=0.015, rely=0.12)


        img = Image.open("mapa.jpg")
        #img=img.resize((int(self.winfo_width()*0.8), int(self.winfo_height()*0.84)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf, image = img, command=lambda:[webbrowser.open("mapa.html")])        
        panel.image=img
        panel.place(relx=0, rely=0, relheight=1, relwidth=1)

        img = Image.open("tabla.png")
        img=img.resize((int((self.winfo_width()*0.96)*0.1), int((self.winfo_height()*0.84)*0.2)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel = ttk.Button(graf, image = img, command=lambda:[self.tabla_ventana_emergente(self.paises.df_pais, "Producción por país")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0.9, rely=0.8, relheight=0.2, relwidth=0.1)
        
    def graficos_general(self):

        self.clearFrame(self.principal_f)
        
        graf1=Frame(self.principal_f)
        graf1.place(relwidth=0.45, relheight=0.48, relx=0.025, rely=0.01)

        graf2=Frame(self.principal_f)
        graf2.place(relwidth=0.45, relheight=0.48, relx=0.525, rely=0.01)
       
        Frame(self.principal_f, bg= "black").place(relwidth=0.001, relheight=1, relx=0.5, rely=0)
        Frame(self.principal_f, bg= "black").place(relwidth=1, relheight=0.001, relx=0, rely=0.5)

        graf3=Frame(self.principal_f)
        graf3.place(relwidth=0.45, relheight=0.48, relx=0.025, rely=0.51)

        graf4=Frame(self.principal_f)
        graf4.place(relwidth=0.45, relheight=0.48, relx=0.525, rely=0.51)

        
        img = Image.open("Tipo_de_documento.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        panel = ttk.Button(graf1, image = img, command=lambda:[webbrowser.open("Tipo_de_documento.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)
        
        img = Image.open("anios.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf2, image = img, command=lambda:[webbrowser.open("anios.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)

        img = Image.open("Tipo_oa.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf3, image = img, command=lambda:[webbrowser.open("Tipo_oa.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)

        img = Image.open("InstitucionFinanciamiento.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf4, image = img, command=lambda:[webbrowser.open("InstitucionFinanciamiento.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)

        canvas_1 = tkinter.Canvas(graf1, width = 12, height = 50)
        canvas_1.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_1.create_text(20, 180, text = "Tipo documental", angle = 90, anchor = "w")

        canvas_2 = tkinter.Canvas(graf2, width = 12, height = 50)
        canvas_2.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_2.create_text(20, 180, text = "Años", angle = 90, anchor = "w")

        canvas_3 = tkinter.Canvas(graf3, width = 12, height = 50)
        canvas_3.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_3.create_text(20, 180, text = "Tipo de acceso abierto", angle = 90, anchor = "w")

        canvas_4 = tkinter.Canvas(graf4, width = 12, height = 50)
        canvas_4.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_4.create_text(20, 180, text = "Financiemiento", angle = 90, anchor = "w")

        img = Image.open("tabla.png")
        img=img.resize((int((self.winfo_width()*0.45)*0.1), int(((self.winfo_height()*0.87)*0.48)*0.2)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel = ttk.Button(graf1, image = img, command=lambda:[self.tabla_ventana_emergente(self.general.df_tipo_doc, "Tipo documental")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)

        panel = ttk.Button(graf2, image = img, command=lambda:[self.tabla_ventana_emergente(self.general.df_anio, "Producción por anio")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)

        panel = ttk.Button(graf3, image = img, command=lambda:[self.tabla_ventana_emergente(self.general.df_oa, "Tipo de acceso abierto")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)

        panel = ttk.Button(graf4, image = img, command=lambda:[self.tabla_ventana_emergente(self.general.df_financiamiento, "Financiemiento")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)

        ttk.Button(self.principal_f, text="->", command=self.graficos_general2).place(rely=0.45, relx=0.98, relheight=0.15, relwidth=0.02)
    
    def graficos_general2(self):

        self.clearFrame(self.principal_f)
        
        graf1=Frame(self.principal_f)
        graf1.place(relwidth=0.45, relheight=0.48, relx=0.025, rely=0.01)

        graf2=Frame(self.principal_f)
        graf2.place(relwidth=0.45, relheight=0.48, relx=0.525, rely=0.01)
       
        Frame(self.principal_f, bg="black").place(relwidth=0.001, relheight=1, relx=0.5, rely=0)
        Frame(self.principal_f, bg="black").place(relwidth=1, relheight=0.001, relx=0, rely=0.5)

        graf3=Frame(self.principal_f)
        graf3.place(relwidth=0.45, relheight=0.48, relx=0.025, rely=0.51)

        graf4=Frame(self.principal_f)
        graf4.place(relwidth=0.45, relheight=0.48, relx=0.525, rely=0.51)

        
        img = Image.open("Nombre_categoria.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        
        panel = ttk.Button(graf1, image = img, command=lambda:[webbrowser.open("Nombre_categoria.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)
        
        img = Image.open("Idioma.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf2, image = img, command=lambda:[webbrowser.open("Idioma.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)

        img = Image.open("ColaboracionPaises.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf3, image = img, command=lambda:[webbrowser.open("ColaboracionPaises.html")])        
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)

        img = Image.open("citasarticulos.jpg")
        img=img.resize((int((self.winfo_width()*0.45)*0.9), int((self.winfo_height()*0.87)*0.48)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
  
        panel = ttk.Button(graf4, image = img, command=lambda:[webbrowser.open("citasarticulos.html")])
        panel.image=img
        panel.place(relx=0.1, rely=0, relheight=1, relwidth=0.9)


        canvas_1 = tkinter.Canvas(graf1, width = 12, height = 50)
        canvas_1.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_1.create_text(20, 180, text = "Categorias", angle = 90, anchor = "w")

        canvas_2 = tkinter.Canvas(graf2, width = 12, height = 50)
        canvas_2.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_2.create_text(20, 180, text = "Idiomas", angle = 90, anchor = "w")

        canvas_3 = tkinter.Canvas(graf3, width = 12, height = 50)
        canvas_3.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_3.create_text(20, 180, text = "Colaboración paises", angle = 90, anchor = "w")

        canvas_4 = tkinter.Canvas(graf4, width = 12, height = 50)
        canvas_4.place(relx=0, rely=0, relheight=1, relwidth=0.1)
        canvas_4.create_text(20, 280, text = "Citas recibidas por los documentos \n según año de publicación", angle = 90, anchor = "w")

        img = Image.open("tabla.png")
        img=img.resize((int((self.winfo_width()*0.45)*0.1), int(((self.winfo_height()*0.87)*0.48)*0.2)), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)

        panel = ttk.Button(graf1, image = img, command=lambda:[self.tabla_ventana_emergente(self.general.df_categoria, "Categorías")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)

        panel = ttk.Button(graf2, image = img, command=lambda:[self.tabla_ventana_emergente(self.general.df_idioma, "Idiomas")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)

        panel = ttk.Button(graf3, image = img, command=lambda:[self.tabla_ventana_emergente(self.paises.df_colaboracion, "Colaboración paises")])#incluir comando que abre el treeview con todo el df usado por el grafico,opcion arriba de ver el grafico completo
        panel.image=img        
        panel.place(relx=0, rely=0.8, relheight=0.2, relwidth=0.1)


        ttk.Button(self.principal_f, text="<-", command=self.graficos_general).place(rely=0.45, relx=0, relheight=0.15, relwidth=0.02)
   
    def tabla(self, frame, df, titulo):
        
        if titulo != 0:
            self.titulo_f=Frame(frame)
            self.titulo_f.place(relwidth=1, relheight=0.1, relx=0, rely=0.01)
            
            self.tabla_f=Frame(frame)
            self.tabla_f.place(relheight=1-0.16, relwidth=0.96, relx=0.015, rely=0.12)
            
            self.scrolly_f=Frame(frame)
            self.scrolly_f.place(relheight=1-0.12, relwidth=0.02,rely=0.12, relx=1-0.01)
            self.scrollx_f=Frame(frame)
            self.scrollx_f.place(relheight=0.02, relwidth=1-0.01,rely=1-0.02, relx=0)
            texto = tkinter.StringVar()
            texto.set(titulo)        
            Label(self.titulo_f, text=texto.get(), font=("Verdana",24), anchor="center").place(rely=0, relx=0, relheight=1, relwidth=1)
        else:
            self.tabla_f=Frame(frame)
            self.tabla_f.place(relheight=0.99, relwidth=1-0.01, relx=0, rely=0)
            
            self.scrolly_f=Frame(frame)
            self.scrolly_f.place(relheight=1, width=10,rely=0, relx=1-0.01)
            self.scrollx_f=Frame(frame)
            self.scrollx_f.place(height=10, relwidth=1-0.01,rely=1-0.02, relx=0)
        self.tv=ttk.Treeview(self.tabla_f)
        self.tv.place(relheight=0.95, relwidth=1, relx=0, rely=0)
        self.tv["columns"]=list(df.columns)
        self.tv["show"]="headings"
        Button(self.tabla_f, text="Exportar", command=lambda:[self.funcionalidades.guardar_df(df)]).place(relx=0, rely=0.95, relwidth=1, relheight=0.05)


        #Llenar nombres columnas
        for col in self.tv["columns"]:
            self.tv.heading(col, text=col)
        
        #Llenar registros filas
        for index, row in df.iterrows():
            self.tv.insert("", 'end', text=index, values=list(row))
        
        #creación y funcionamiento del scroll
        scrolly=tkinter.Scrollbar(self.scrolly_f, orient="vertical", command=self.tv.yview)
        scrollx=tkinter.Scrollbar(self.scrollx_f, orient="horizontal", command=self.tv.xview)
        scrollx.pack(side="bottom", fill=BOTH, expand=True)
        scrolly.pack(side="right", fill=BOTH, expand=True)
        self.tv.configure(xscrollcommand=scrollx.set)
        self.tv.configure(yscrollcommand=scrolly.set)

        return self.tv
    
    def tabla_ventana_emergente(self, df, titulo:str):
        self.df=df
        self.titulo=titulo
        self.v_tabla = Toplevel(self)
        self.v_tabla.title(titulo)
        self.v_tabla.geometry('650x350')

        self.titulo_f=Frame(self.v_tabla)
        self.titulo_f.place(relwidth=0.6, relheight=0.08, relx=0.2, rely=0.001)
        
        self.tabla_f=Frame(self.v_tabla)
        self.tabla_f.place(relheight=1-0.13, relwidth=0.96, relx=0.015, rely=0.12)
        
        self.scrolly_f=Frame(self.v_tabla)
        self.scrolly_f.place(relheight=1-0.12, relwidth=0.01,rely=0.12, relx=1-0.01)
        self.scrollx_f=Frame(self.v_tabla)
        self.scrollx_f.place(relheight=0.02, relwidth=1-0.01,rely=1-0.02, relx=0)
        
        self.llenar_arbol_emergente(self.df, titulo, 1)

    def llenar_arbol_emergente(self, df, titulo:str, ventana): # la ventana dira si es la principal o la secundaria con filtro para la interacción del boton de atras
        
        self.clearFrame(self.titulo_f)
        texto = tkinter.StringVar()
        texto.set(titulo)        
        Label(self.titulo_f, text=texto.get(), font=("Verdana",24)).place(rely=0, relx=0, relheight=1, relwidth=1)

        self.clearFrame(self.tabla_f)
        self.tv1=ttk.Treeview(self.tabla_f)
        self.tv1.place(relheight=0.95, relwidth=1, relx=0, rely=0)

        self.tv1["columns"]=list(df.columns)
        self.tv1["show"]="headings"

        #Llenar nombres columnas
        for col in self.tv1["columns"]:
            self.tv1.heading(col, text=col)
        
        #Llenar registros filas
        for index, row in df.iterrows():
            self.tv1.insert("", 'end', text=index, values=list(row))
        
        #creación y funcionamiento del scroll
        self.clearFrame(self.scrolly_f)
        self.clearFrame(self.scrollx_f)
        scrolly=tkinter.Scrollbar(self.scrolly_f, orient="vertical", command=self.tv1.yview)
        scrollx=tkinter.Scrollbar(self.scrollx_f, orient="horizontal", command=self.tv1.xview)
        scrollx.pack(side="bottom", fill=BOTH, expand=True)
        scrolly.pack(side="right", fill=BOTH, expand=True)
        self.tv1.configure(xscrollcommand=scrollx.set)
        self.tv1.configure(yscrollcommand=scrolly.set)

        if ventana==2:
            atras=ttk.Button(self.v_tabla, text="<-", command=lambda:[self.llenar_arbol_emergente(self.df, self.titulo, 1)])
            atras.place(relx=0, rely=0, width=35, height=35)
            Button(self.tabla_f, text="Exportar", command=lambda:[self.funcionalidades.guardar_df(self.df_filtro)]).place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
        elif ventana == 1:
            atras=ttk.Button(self.v_tabla, text="<-", command=lambda:[self.v_tabla.destroy()])
            atras.place(relx=0, rely=0, width=35, height=35)
            Button(self.tabla_f, text="Exportar", command=lambda:[self.funcionalidades.guardar_df(self.df)]).place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
        #si el titulo contiene aut entonces:
        if titulo.find("autor") != -1:
            self.tv1.bind("<Double-1>", self.click_autor)
        elif titulo.find("revista") != -1:
            self.tv1.bind("<Double-1>", self.click_revista_emergente)
        elif titulo.find("instituc") != -1:
            self.tv1.bind("<Double-1>", self.click_instituciones)
        elif titulo.find("país") != -1:
            self.tv1.bind("<Double-1>", self.click_pais)
        elif titulo.find("paises") != -1:
            self.tv1.bind("<Double-1>", self.click_colab_paises)
        elif titulo.find("anio") != -1:
            self.tv1.bind("<Double-1>", self.click_anio)
        elif titulo.find("Tipo documental") != -1:
            self.tv1.bind("<Double-1>", self.click_tipo_doc)
        elif titulo.find("acceso abierto") != -1:
            self.tv1.bind("<Double-1>", self.click_tipo_oa)
        elif titulo.find("Financiemiento") != -1:
            self.tv1.bind("<Double-1>", self.click_financiamiento)
        elif titulo.find("Categorías") != -1:
            self.tv1.bind("<Double-1>", self.click_Categorías)
        elif titulo.find("Idiomas") != -1:
            self.tv1.bind("<Double-1>", self.click_Idiomas)
        
    def click_Idiomas(self, e):
        self.df_filtro=self.general.filtro_idioma(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)

    def click_Categorías(self, e):
        self.df_filtro=self.general.filtro_categoria(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)

    def click_financiamiento(self, e):
        self.df_filtro=self.general.filtro_financiamiento(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)

    def click_tipo_oa(self, e):
        self.df_filtro=self.general.filtro_Tipo_OA(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)

    def click_tipo_oa(self, e):
        self.df_filtro=self.general.filtro_Tipo_OA(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)

    def click_tipo_doc(self, e):
        self.df_filtro=self.general.filtro_Tipo_Doc(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)

    def click_anio(self, e):
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.df_filtro=self.general.filtro_anio(self.general, self.tv1.item(self.tv1.selection(), "values")[0])
        self.llenar_arbol_emergente(self.df_filtro, titulo, 2)
        
    def click_colab_paises(self, e):
        self.paises.filtro_colaboracion(self.paises, self.tv1.item(self.tv1.selection(), "values")[2])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[2]
        self.df_filtro=self.paises.df_filtrado_colaboracion
        self.llenar_arbol_emergente(self.paises.df_filtrado_colaboracion, titulo, 2)
        
    def click_pais(self, e):
        self.paises.filtro(self.paises, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.df_filtro=self.paises.df_filtrado
        self.llenar_arbol_emergente(self.paises.df_filtrado, titulo, 2)
        
    def click_instituciones(self, e):
        self.instituciones.filtro(self.instituciones, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.df_filtro=self.instituciones.filtrado_df
        self.llenar_arbol_emergente(self.instituciones.filtrado_df, titulo, 2)
        
    def click_revista_emergente(self, e):
        self.revistas.filtro(self.revistas, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.df_filtro=self.revistas.filtrado_df
        self.llenar_arbol_emergente(self.revistas.filtrado_df, titulo, 2)
        
    def click_autor(self, e):
        self.autores.filtro(self.autores, self.tv1.item(self.tv1.selection(), "values")[0])
        titulo="Filtrado por : " + self.tv1.item(self.tv1.selection(), "values")[0]
        self.df_filtro=self.autores.filtrado_df
        self.llenar_arbol_emergente(self.autores.filtrado_df, titulo, 2)
        
    def clearFrame(self, frame:Frame):
    # destroy all widgets from frame
        for widget in frame.winfo_children():
            widget.destroy()
        

if __name__ == '__main__':
    
    app = program()
    app.bienvenida()
    app.resizable(width=True, height=True)
    app.mainloop()
