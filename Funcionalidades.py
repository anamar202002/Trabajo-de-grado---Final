import plotly.graph_objects as go
from tkinter import filedialog
import pandas as pd
from plotly.subplots import make_subplots
from consultas import consulta
import plotly.express as px
import numpy as np
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from baseDatos import baseDatos
#plotly y panel permite exportar a html

class graficos():
    def __init__(self):
        pass
    
    def treemap(self, valores: list, leyenda: list, nombre_graf: str):
        for i in range(len(valores)):
            leyenda[i]=leyenda[i]+" ("+str(valores[i])+")"
        df=pd.DataFrame(dict(leyenda=leyenda, valores=valores))
        fig=px.treemap(df, path=[px.Constant("all"),'leyenda'], values='valores')
        fig.update_traces(root_color='lightgrey')
        fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))#las margenes en 0 evita los espacios en blanco fuera del grafico
        fig.write_image(nombre_graf+".jpg")
        fig.write_html(nombre_graf+".html")
        #fig.show() #treemap plotly

    def barchart(self, valores:list, leyenda:list, nombre_graf:str):
        df=pd.DataFrame(dict(leyenda=leyenda, valores=valores))
        fig = px.bar(df, y='valores', x='leyenda', text='leyenda')
        fig.update_layout(showlegend=False)
        fig.write_image(nombre_graf+".jpg")
        fig.write_html(nombre_graf+".html")
        #fig.show()
    
    def lotka(self, trabajos:list, autores:list):

        fig = go.Figure(
            data = [
                go.Scatter(x=trabajos, y=autores, name="Autores"),
                go.Scatter(x=trabajos, y=trabajos, name="Trabajos"),
            ],
            layout = {"xaxis": {"title": "Trabajos"}, "yaxis": {"title": "Autores"}, "title": "Lotka"}
        )
        fig.write_image("Lotka.jpg")
        fig.write_html("Lotka.html")

    def nubes_palabras(self, df, columna, nombre_graf):
        t=[]
        text = " ".join(review for review in df[columna].astype(str))

        stopwords = set(STOPWORDS)
        stopwords.update(["x", "y", "your", "yours", "yourself", "yourselves", "you", "yond", "yonder", "yon", "ye", "yet", "z", "zillion", "j", "u", "umpteen", "usually", "us", "username", "uponed", "upons", "uponing", "upon", "ups", "upping", "upped", "up", "unto", "until", "unless", "unlike", "unliker", "unlikest", "under", "underneath", "use", "used", "usedest", "r", "rath", "rather", "rathest", "rathe", "re", "relate", "related", "relatively", "regarding", "really", "res", "respecting", "respectively", "q", "quite", "que", "qua", "n", "neither", "neaths", "neath", "nethe", "nethermost", "necessary", "necessariest", "necessarier", "never", "nevertheless", "nigh", "nighest", "nigher", "nine", "noone", "nobody", "nobodies", "nowhere", "nowheres", "no", "noes", "nor", "nos", "no-one", "none", "not", "notwithstanding", "nothings", "nothing", "nathless", "natheless", "t", "ten", "tills", "till", "tilled", "tilling", "to", "towards", "toward", "towardest", "towarder", "together", "too", "thy", "thyself", "thus", "than", "that", "those", "thou", "though", "thous", "thouses", "thoroughest", "thorougher", "thorough", "thoroughly", "thru", "thruer", "thruest", "thro", "through", "throughout", "throughest", "througher", "thine", "this", "thises", "they", "thee", "the", "then", "thence", "thenest", "thener", "them", "themselves", "these", "therer", "there", "thereby", "therest", "thereafter", "therein", "thereupon", "therefore", "their", "theirs", "thing", "things", "three", "two", "o", "oh", "owt", "owning", "owned", "own", "owns", "others", "other", "otherwise", "otherwisest", "otherwiser", "of", "often", "oftener", "oftenest", "off", "offs", "offest", "one", "ought", "oughts", "our", "ours", "ourselves", "ourself", "out", "outest", "outed", "outwith", "outs", "outside", "over", "overallest", "overaller", "overalls", "overall", "overs", "or", "orer", "orest", "on", "oneself", "onest", "ons", "onto", "a", "atween", "at", "athwart", "atop", "afore", "afterward", "afterwards", "after", "afterest", "afterer", "ain", "an", "any", "anything", "anybody", "anyone", "anyhow", "anywhere", "anent", "anear", "and", "andor", "another", "around", "ares", "are", "aest", "aer", "against", "again", "accordingly", "abaft", "abafter", "abaftest", "abovest", "above", "abover", "abouter", "aboutest", "about", "aid", "amidst", "amid", "among", "amongst", "apartest", "aparter", "apart", "appeared", "appears", "appear", "appearing", "appropriating", "appropriate", "appropriatest", "appropriates", "appropriater", "appropriated", "already", "always", "also", "along", "alongside", "although", "almost", "all", "allest", "aller", "allyou", "alls", "albeit", "awfully", "as", "aside", "asides", "aslant", "ases", "astrider", "astride", "astridest", "astraddlest", "astraddler", "astraddle", "availablest", "availabler", "available", "aughts", "aught", "vs", "v", "variousest", "variouser", "various", "via", "vis-a-vis", "vis-a-viser", "vis-a-visest", "viz", "very", "veriest", "verier", "versus", "k", "g", "go", "gone", "good", "got", "gotta", "gotten", "get", "gets", "getting", "b", "by", "byandby", "by-and-by", "bist", "both", "but", "buts", "be", "beyond", "because", "became", "becomes", "become", "becoming", "becomings", "becominger", "becomingest", "behind", "behinds", "before", "beforehand", "beforehandest", "beforehander", "bettered", "betters", "better", "bettering", "betwixt", "between", "beneath", "been", "below", "besides", "beside", "m", "my", "myself", "mucher", "muchest", "much", "must", "musts", "musths", "musth", "main", "make", "mayest", "many", "mauger", "maugre", "me", "meanwhiles", "meanwhile", "mostly", "most", "moreover", "more", "might", "mights", "midst", "midsts", "h", "huh", "humph", "he", "hers", "herself", "her", "hereby", "herein", "hereafters", "hereafter", "hereupon", "hence", "hadst", "had", "having", "haves", "have", "has", "hast", "hardly", "hae", "hath", "him", "himself", "hither", "hitherest", "hitherer", "his", "how-do-you-do", "however", "how", "howbeit", "howdoyoudo", "hoos", "hoo", "w", "woulded", "woulding", "would", "woulds", "was", "wast", "we", "wert", "were", "with", "withal", "without", "within", "why", "what", "whatever", "whateverer", "whateverest", "whatsoeverer", "whatsoeverest", "whatsoever", "whence", "whencesoever", "whenever", "whensoever", "when", "whenas", "whether", "wheen", "whereto", "whereupon", "wherever", "whereon", "whereof", "where", "whereby", "wherewithal", "wherewith", "whereinto", "wherein", "whereafter", "whereas", "wheresoever", "wherefrom", "which", "whichever", "whichsoever", "whilst", "while", "whiles", "whithersoever", "whither", "whoever", "whosoever", "whoso", "whose", "whomever", "s", "syne", "syn", "shalling", "shall", "shalled", "shalls", "shoulding", "should", "shoulded", "shoulds", "she", "sayyid", "sayid", "said", "saider", "saidest", "same", "samest", "sames", "samer", "saved", "sans", "sanses", "sanserifs", "sanserif", "so", "soer", "soest", "sobeit", "someone", "somebody", "somehow", "some", "somewhere", "somewhat", "something", "sometimest", "sometimes", "sometimer", "sometime", "several", "severaler", "severalest", "serious", "seriousest", "seriouser", "senza", "send", "sent", "seem", "seems", "seemed", "seemingest", "seeminger", "seemings", "seven", "summat", "sups", "sup", "supping", "supped", "such", "since", "sine", "sines", "sith", "six", "stop", "stopped", "p", "plaintiff", "plenty", "plenties", "please", "pleased", "pleases", "per", "perhaps", "particulars", "particularly", "particular", "particularest", "particularer", "pro", "providing", "provides", "provided", "provide", "probably", "l", "layabout", "layabouts", "latter", "latterest", "latterer", "latterly", "latters", "lots", "lotting", "lotted", "lot", "lest", "less", "ie", "ifs", "if", "i", "info", "information", "itself", "its", "it", "is", "idem", "idemer", "idemest", "immediate", "immediately", "immediatest", "immediater", "in", "inwards", "inwardest", "inwarder", "inward", "inasmuch", "into", "instead", "insofar", "indicates", "indicated", "indicate", "indicating", "indeed", "inc", "f", "fact", "facts", "fs", "figupon", "figupons", "figuponing", "figuponed", "few", "fewer", "fewest", "frae", "from", "failing", "failings", "five", "furthers", "furtherer", "furthered", "furtherest", "further", "furthering", "furthermore", "fourscore", "followthrough", "for", "forwhy", "fornenst", "formerly", "former", "formerer", "formerest", "formers", "forbye", "forby", "fore", "forever", "forer", "fores", "four", "d", "ddays", "dday", "do", "doing", "doings", "doe", "does", "doth", "downwarder", "downwardest", "downward", "downwards", "downs", "done", "doner", "dones", "donest", "dos", "dost", "did", "differentest", "differenter", "different", "describing", "describe", "describes", "described", "despiting", "despites", "despited", "despite", "during", "c", "cum", "circa", "chez", "cer", "certain", "certainest", "certainer", "cest", "canst", "cannot", "cant", "cants", "canting", "cantest", "canted", "co", "could", "couldst", "comeon", "comeons", "come-ons", "come-on", "concerning", "concerninger", "concerningest", "consequently", "considering", "e", "eg", "eight", "either", "even", "evens", "evenser", "evensest", "evened", "evenest", "ever", "everyone", "everything", "everybody", "everywhere", "every", "ere", "each", "et", "etc", "elsewhere", "else", "ex", "excepted", "excepts", "except", "excepting", "exes", "enough", "qué","porque","posible","primer","primera","primero","primeros","principalmente","pronto","propia","propias","propio","propios","proximo","próximo","próximos","pudo","pueda","puede","pueden","puedo","pues","q","qeu","que","quedó","queremos","quien","quienes","quiere","quiza","quizas","quizá","quizás","quién","quiénes","qué","r","raras","realizado","realizar","realizó","repente","respecto","s","sabe","sabeis","sabemos","saben","saber","sabes","sal","salvo","se","sea","seamos","sean","seas","segun","segunda","segundo","según","seis","ser","sera","seremos","será","serán","serás","seré","seréis","sería","seríais","seríamos","serían","serías","seáis","señaló","si","sido","siempre","siendo","siete","sigue","siguiente","sin","sino","sobre","sois","sola","solamente","solas","solo","solos","somos","son","soy","soyos","su","supuesto","sus","suya","suyas","suyo","suyos","sé","sí","sólo","t","tal","tambien","también","tampoco","tan","tanto","tarde","te","temprano","tendremos","tendrá","tendrán","tendrás","tendré","tendréis","tendría","tendríais","tendríamos","tendrían","tendrías","tened","teneis","tenemos","tener","tenga","tengamos","tengan","tengas","tengo","tengáis","tenida","tenidas","tenido","tenidos","teniendo","tenéis","tenía","teníais","teníamos","tenían","tenías","tercera","ti","tiempo","tiene","tienen","tienes","toda","todas","todavia","todavía","todo","todos","total","trabaja","trabajais","trabajamos","trabajan","trabajar","trabajas","trabajo","tras","trata","través","tres","tu","tus","tuve","tuviera","tuvierais","tuvieran","tuvieras","tuvieron","tuviese","tuvieseis","tuviesen","tuvieses","tuvimos","tuviste","tuvisteis","tuviéramos","tuviésemos","tuvo","tuya","tuyas","tuyo","tuyos","tú","u","ultimo","un","una","unas","uno","unos","usa","usais","usamos","usan","usar","usas","uso","usted","ustedes","v","va","vais","valor","vamos","van","varias","varios","vaya","veces","ver","verdad","verdadera","verdadero","vez","vosotras","vosotros","voy","vuestra","vuestras","vuestro","vuestros","w","x","y","ya","yo","z","él","éramos","ésa","ésas","ése","ésos","ésta","éstas","éste","éstos","última","últimas","último","últimos"])

        wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=1344, height=743).generate(text)
        t.append([palabra for palabra in text.split(' ') if palabra not in stopwords])
        df=pd.DataFrame(t)
        df=df.T
        df=df.rename(columns={0:'Palabra'})
        df =  df.groupby('Palabra').size().reset_index(name='Repeticiones')
        df = df.sort_values(by='Repeticiones', ascending=False) #ordena las repeticiones de mayor a menor

        plt.axis("off")
        plt.figure( figsize=(40,20))
        plt.tight_layout(pad=0)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(nombre_graf+".png", bbox_inches='tight',pad_inches = 0)

        return df
    
    def lineas(self, valores:list, leyenda:list, nombre_graf:str):
        df=pd.DataFrame(dict(leyenda=leyenda, valores=valores))
        fig = px.line(df, x=leyenda, y=valores, title=nombre_graf)
        fig.update_layout(showlegend=False)
        fig.write_image(nombre_graf+".jpg")
        fig.write_html(nombre_graf+".html")


    def pie(self, valores:list, leyenda:list, nombre_graf:str):
        # This dataframe has 244 lines, but 4 distinct values for `day`
        df=pd.DataFrame(dict(leyenda=leyenda, valores=valores))
        fig = px.pie(df, values=valores, names=leyenda)
        fig.write_image(nombre_graf+".jpg")
        fig.write_html(nombre_graf+".html")

    def mapa_paises(self, df:pd.DataFrame):
        fig = px.choropleth(df, locations="Codigo",
                            color="Cantidad_articulos", # lifeExp is a column of gapminder
                            hover_name="Nombre_pais", # column to add to hover information
                            color_continuous_scale=px.colors.sequential.Plasma)
        fig.write_image("mapa.jpg")
        fig.write_html("mapa.html")


class autores(): #Se realiza la consulta de los autores más citados y los autores con mayor cantidad de artículos escritos
    #df=pd.read_excel("autores.xlsx", index_col=0)
    nombre="nombre_autor"
    codConsulta= "SELECT "+ nombre + ", Citas_recibidas, Titulo FROM articulo, autor, autor_articulo where articulo.ID_art = autor_articulo.ID_art AND autor.ID_au = autor_articulo.ID_au"
    df=consulta.df_consulta(consulta, codConsulta)
    filtrado_df=consulta.df
    df_au_cit=pd.DataFrame()
    df_au_pro=pd.DataFrame()
    df_lotka = pd.DataFrame()
    df_au_elite = pd.DataFrame()

    def __init__(self):
        super().__init__() 
    
    def autores_mas_productivos(self): 
        autores.df_au_pro =  autores.df.groupby('Nombre_autor').size().reset_index(name='Cantidad_articulos')
        aux=autores.df_au_pro.nlargest(10,'Cantidad_articulos')
        graficos.treemap(graficos, list(aux['Cantidad_articulos']), list(aux['Nombre_autor']), "AutoresMasProductivos")
        autores.df_lotka=autores.df_au_pro.groupby('Cantidad_articulos').size().reset_index(name='Cantidad_autores')
        graficos.lotka(graficos, list(autores.df_lotka['Cantidad_articulos']), list(autores.df_lotka['Cantidad_autores']))


    def elite(self):
        t=list(autores.df_lotka['Cantidad_articulos'])
        a=list(autores.df_lotka['Cantidad_autores'])
        #Para hallar los autores élite  (donde dos lineas se intersectan) se busca el valor donde la resta sea la más cercana al 0
        resta=[]
        for i in range(len(t)):
            resta.append(a[i]-t[i])
        resta=np.array(resta)
        resta=abs(resta)
        resta=list(resta)
        print(t[resta.index(min(resta))])
        autores.df_au_elite=autores.df_au_pro
        autores.df_au_elite= autores.df_au_elite.where(autores.df_au_elite['Cantidad_articulos']>=t[resta.index(min(resta))])
        autores.df_au_elite=autores.df_au_elite.dropna()
        autores.df_au_elite=autores.df_au_elite.sort_values(by="Cantidad_articulos", ascending=True)
        autores.df_au_elite=autores.df_au_elite.reset_index(drop=True)
        print(autores.df_au_elite)

    def filtro(self, autor):
        nConsulta=autores.codConsulta+" AND "+autores.nombre+" = "+'"'+autor+'"'
        c=consulta
        c.df_consulta(c, nConsulta)
        autores.filtrado_df=c.df
    

class revistas(): #Se realiza la consulta de las revistas
    #df=pd.read_excel("revistas.xlsx", index_col=0)
    nombre="Nombre_fuente"
    codConsulta= "SELECT "+ nombre + ", ISSN, eISSN, ISBN, Titulo, Citas_recibidas FROM FUENTE, ARTICULO WHERE ARTICULO.ID_fuente=FUENTE.ID_fuente"
    
    df=consulta.df_consulta(consulta, codConsulta)
    filtrado_df=consulta.df
    df_rev_cit=pd.DataFrame()
    df_rev_pro=pd.DataFrame()
    df_bradford = pd.DataFrame()
    zonas_b=[]

    def __init__(self):
        super().__init__() 
    
    def revistas_mas_citados(self):
        revistas.df_rev_cit=pd.DataFrame(revistas.df, columns=['Nombre_fuente', 'Citas_recibidas'])
        revistas.df_rev_cit['Citas_recibidas']=revistas.df_rev_cit['Citas_recibidas'].astype(float)
        revistas.df_rev_cit = revistas.df_rev_cit.groupby('Nombre_fuente').sum() #funciona, pone como indice le nombre autor
        #no ordena bien y me pone otros valores x
        revistas.df_rev_cit = revistas.df_rev_cit.sort_values(by='Citas_recibidas', ascending=False) #ordena los articulos de mayor a menor
        revistas.df_rev_cit=revistas.df_rev_cit.reset_index()
        aux=revistas.df_rev_cit.head(15)
        graficos.treemap(graficos, list(aux['Citas_recibidas']), list(aux['Nombre_fuente']), "RevistasMasCitados")

    def revistas_mas_productivos(self): 
        revistas.df_rev_pro =  revistas.df.groupby('Nombre_fuente').size().reset_index(name='Cantidad_articulos')
        revistas.df_rev_pro = revistas.df_rev_pro.sort_values(by='Cantidad_articulos', ascending=False)
        aux=revistas.df_rev_pro.nlargest(10,'Cantidad_articulos')
        graficos.barchart(graficos, list(aux['Cantidad_articulos']), list(aux['Nombre_fuente']), "RevistasMasProductivos")
        self.bradford(revistas)
    
    def bradford(self):
        cant=list(revistas.df_rev_pro['Cantidad_articulos'])
        revistas.df_bradford=revistas.df_rev_pro

        ind=sum(cant)/3
        ind=int(ind)#aproxima a un valor exacto
        zonas=[]

        print(ind)
        
        cont=0
        z=1
        r=0
        for i in cant:
            if cont<ind:
                cont+=i #articulos
                zonas.append("Zona "+str(z))
            else:
                revistas.zonas_b.append([r, round((r/len(cant))*100, 2), cont, round((cont/sum(cant))*100, 2)])
                cont=0
                r=0
                z+=1
                cont+=i
                zonas.append("Zona "+str(z))
            r+=1
        revistas.zonas_b.append([r, round((r/len(cant))*100, 2), cont, round((cont/sum(cant))*100, 2)])
        
        print(len(zonas), len(cant))
        revistas.df_bradford["Zona"]=zonas
        print(revistas.df_bradford)
        print(revistas.zonas_b)
    
    def filtro_zona(self, zona):
        df = revistas.df_bradford.where(revistas.df_bradford["Zona"]==zona)
        df=df.dropna()
        return df


    def filtro(self, revista):
        nConsulta=revistas.codConsulta+" AND "+revistas.nombre+" = "+'"'+revista+'"'
        c=consulta
        c.df_consulta(c, nConsulta)
        revistas.filtrado_df=c.df

class instituciones(): #Se realiza la consulta de los instituciones más citados y los instituciones con mayor cantidad de artículos escritos
    #df=pd.read_excel("instituciones.xlsx", index_col=0)
    nombre="Nombre_institucion"
    codConsulta= "SELECT " +nombre+ ", Titulo  from INSTITUCION, INSTITUCION_ARTICULO, ARTICULO WHERE INSTITUCION.ID_institucion = INSTITUCION_ARTICULO.ID_institucion and ARTICULO.ID_art = INSTITUCION_ARTICULO.ID_art"
    
    df=consulta.df_consulta(consulta, codConsulta)
    filtrado_df=consulta.df
    df_ins_pro=pd.DataFrame()
    df_lotka = pd.DataFrame()
    df_au_elite = pd.DataFrame()

    def __init__(self):
        super().__init__() 
    

    def instituciones_mas_productivos(self): 
        instituciones.df_ins_pro =  instituciones.df.groupby('Nombre_institucion').size().reset_index(name='Cantidad_articulos')
        aux=instituciones.df_ins_pro.nlargest(10,'Cantidad_articulos')
        graficos.barchart(graficos, list(aux['Cantidad_articulos']), list(aux['Nombre_institucion']), "institucionesMasProductivas")

    def filtro(self, ins):
        nConsulta=instituciones.codConsulta+" AND "+instituciones.nombre+" = "+'"'+ins+'"'
        c=consulta
        c.df_consulta(c, nConsulta)
        instituciones.filtrado_df=c.df

class palabras():
    Autor_keyword=pd.DataFrame()
    BD_keyword=pd.DataFrame()
    filtrado_df=pd.DataFrame()

    def __init__(self):
        super().__init__()
    
    def graficos(self):
        palabras.BD_keyword=graficos.nubes_palabras(graficos, baseDatos.BDKEYWORD, 'BD_keyword', 'bd_keys')
        palabras.Autor_keyword=graficos.nubes_palabras(graficos, baseDatos.AU_KEYWORD, 'Autor_keyword', 'au_keys')
    
    def filtro(self, palabra:str, tabla:str):
        if tabla.find("bd")!=-1:
            nConsulta="SELECT ARTICULO.Titulo, BDKEYWORD.BD_keyword, ARTICULO.Resumen FROM BDKEYWORD INNER JOIN BDKEY_ARTICULO ON BDKEYWORD.ID_bdKey = BDKEY_ARTICULO.ID_bdkey INNER JOIN   ARTICULO ON ARTICULO.ID_art= BDKEY_ARTICULO.ID_art" + " WHERE BD_keyword like "+ "'"+ palabra+'%'+"'" +"OR BD_keyword like " + "'"+ '%'+palabra+'%' + "'"+ " OR BD_keyword like " + "'"+ '%'+palabra + "'"
        if tabla.find("au")!=-1:
            nConsulta="SELECT ARTICULO.Titulo, AU_KEYWORD.Autor_keyword, ARTICULO.Resumen FROM AU_KEYWORD INNER JOIN AUKEY_ARTICULO ON AU_KEYWORD.ID_auKey = AUKEY_ARTICULO.ID_aukey INNER JOIN   ARTICULO ON ARTICULO.ID_art= AUKEY_ARTICULO.ID_art" + " WHERE Autor_keyword like "+ "'"+ palabra+'%'+"'" +"OR Autor_keyword like " + "'"+ '%'+palabra+'%' + "'"+ " OR Autor_keyword like " + "'"+ '%'+palabra + "'"
        c=consulta
        c.df_consulta(c, nConsulta)
        palabras.filtrado_df=c.df

class pais():
    df_pais =pd.DataFrame()
    df_pais_articulo =pd.DataFrame()
    df_colaboracion =pd.DataFrame()
    df_filtrado=pd.DataFrame()
    df_filtrado_colaboracion=pd.DataFrame()


    def llenar_paises(self):
        self.cons = "SELECT DISTINCT PAIS.Codigo, PAIS.Nombre_pais, ARTICULO.Titulo FROM PAIS, Institucion, ARTICULO, INSTITUCION_ARTICULO WHERE Institucion.ID_pais = PAIS.ID_pais AND INSTITUCION_ARTICULO.ID_art = ARTICULO.ID_art AND INSTITUCION_ARTICULO.ID_institucion = Institucion.ID_institucion AND PAIS.Codigo != '[No disponible]'"
        consulta.df_consulta(consulta, self.cons)
        pais.df_pais_articulo = consulta.df
        pais.df_pais = pais.df_pais_articulo.groupby(['Codigo', 'Nombre_pais']).size().reset_index(name='Cantidad_articulos')
        graficos.mapa_paises(graficos, pais.df_pais)

    def colaboración(self):
        pais.df_colaboracion = pais.df_pais_articulo.groupby('Titulo').size().reset_index(name='Cantidad_Paises')
        pais.df_colaboracion['Colaboracion']= np.where(pais.df_colaboracion['Cantidad_Paises']>1, 'Internacional', 'Nacional')
        print(pais.df_colaboracion)
        df1=consulta.df_consulta(consulta, "SELECT Titulo, COUNT(*) AS Cantidad_autores FROM ARTICULO, AUTOR, AUTOR_ARTICULO WHERE AUTOR_ARTICULO.ID_au = AUTOR.ID_au AND ARTICULO.ID_art = AUTOR_ARTICULO.ID_art GROUP by Titulo having count(*) == 1")
        print(df1)
        titulos=list(df1['Titulo'])
        for fila in titulos:
            pais.df_colaboracion.iloc[pais.df_colaboracion.index[pais.df_colaboracion['Titulo'] == fila], 2]="Sin colaboración"

        df = pais.df_colaboracion.groupby('Colaboracion').size().reset_index(name='Cantidad_Paises')
        graficos.pie(graficos, list(df['Cantidad_Paises']), list(df['Colaboracion']), "ColaboracionPaises")

    
    def filtro_colaboracion(self, colab):
        pais.df_filtrado_colaboracion= pais.df_colaboracion[pais.df_colaboracion['Colaboracion'] == colab]

    def filtro(self, codigo:str) :
        ncons = self.cons + " AND PAIS.Codigo = " + "'" + codigo + "'"
        consulta.df_consulta(consulta, ncons)
        pais.df_filtrado=consulta.df

class general():
    df_anio_art=pd.DataFrame(baseDatos.ARTICULO, columns=['Anio', 'Titulo'])
    df_tipo_doc_art=pd.DataFrame(baseDatos.ARTICULO, columns=['Tipo_de_documento', 'Titulo'])
    df_idioma_art=pd.DataFrame(baseDatos.ARTICULO, columns=['Idioma', 'Titulo'])
    df_oa=pd.DataFrame()
    df_oa_art=pd.DataFrame()
    df_categoria=pd.DataFrame()
    df_financiamiento=pd.DataFrame()
    df_financiamiento_art=pd.DataFrame()

    df_anio=df_anio_art.groupby('Anio').size().reset_index(name='Cantidad_articulos')
    df_idioma=df_idioma_art.groupby('Idioma').size().reset_index(name='Cantidad_articulos')
    df_tipo_doc=df_tipo_doc_art.groupby('Tipo_de_documento').size().reset_index(name='Cantidad_articulos')

    def oa(self):
        cons="SELECT OPEN_ACCESS.Tipo_oa, ARTICULO.Titulo from OPEN_ACCESS, OA_ARTICULO, ARTICULO WHERE OA_ARTICULO.ID_oa = OPEN_ACCESS.ID_oa AND ARTICULO.ID_art = OA_ARTICULO.ID_art and OPEN_ACCESS.Tipo_oa!='[No disponible]'"
        consulta.df_consulta(consulta, cons)
        general.df_oa_art=consulta.df
        general.df_oa=general.df_oa_art.groupby('Tipo_oa').size().reset_index(name='Cantidad_articulos')
        graficos.pie(graficos, list(general.df_oa['Cantidad_articulos']), list(general.df_oa['Tipo_oa']), "Tipo_oa")

    def categoria(self):
        cons="SELECT CATEGORIA.Nombre_categoria, SUB_CATEGORIA.Nombre_subcategoria, ARTICULO.Titulo FROM CATEGORIA, CATEGORIA_ARTICULO, ARTICULO, SUB_CATEGORIA WHERE CATEGORIA_ARTICULO.ID_art = ARTICULO.ID_art AND CATEGORIA_ARTICULO.ID_cat = CATEGORIA.ID_cat AND CATEGORIA_ARTICULO.ID_subcat = SUB_CATEGORIA.ID_subcat"
        general.df_categoria=consulta.df_consulta(consulta, cons)
        general.df_categoria["Nombre_subcategoria"] = general.df_categoria["Nombre_subcategoria"].replace({"[No disponible]": "Sin subcategoría"})
        fig = px.treemap(general.df_categoria, path=[px.Constant("Categoria"), 'Nombre_categoria', 'Nombre_subcategoria'])
        fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        fig.write_image("Nombre_categoria.jpg")
        fig.write_html("Nombre_categoria.html")

    def financiamiento(self):
        cons = "SELECT FINANCIAMIENTO.institucion, ARTICULO.Titulo FROM FINANCIAMIENTO, ARTICULO, FINANCIAMIENTO_ARTICULO WHERE FINANCIAMIENTO.ID_fin = FINANCIAMIENTO_ARTICULO.ID_fin AND ARTICULO.ID_art = FINANCIAMIENTO_ARTICULO.ID_art AND FINANCIAMIENTO.institucion != '[No disponible]' AND FINANCIAMIENTO.institucion != ' '"
        general.df_financiamiento_art=consulta.df_consulta(consulta, cons)
        general.df_financiamiento = general.df_financiamiento_art.groupby('Institucion').size().reset_index(name='Cantidad_articulos')
        aux=general.df_financiamiento.nlargest(10,'Cantidad_articulos')
        graficos.treemap(graficos, list(aux['Cantidad_articulos']), list(aux['Institucion']), "InstitucionFinanciamiento")
        #El grafico se realiza con solo las primeras 10 instituciones dado que pueden ser demasiadas y generar ruido

    def graf_gen(self):
        graficos.lineas(graficos, list(general.df_anio['Cantidad_articulos']), list(general.df_anio['Anio']), "anios")
        graficos.barchart(graficos, list(general.df_idioma['Cantidad_articulos']), list(general.df_idioma['Idioma']), "Idioma")
        graficos.barchart(graficos, list(general.df_tipo_doc['Cantidad_articulos']), list(general.df_tipo_doc['Tipo_de_documento']), "Tipo_de_documento")
    
    def citas_articulo(self):
        cons="SELECT ARTICULO.Citas_recibidas, ARTICULO.Anio FROM ARTICULO WHERE ARTICULO.Citas_recibidas != 0.0"
        df=consulta.df_consulta(consulta, cons)
        df['Citas_recibidas'] = df['Citas_recibidas'].astype('float64')
        df['Articulos']=1
        df1=df.groupby(['Anio'])['Articulos', 'Citas_recibidas'].sum().reset_index()
        
        leyenda=list(df1['Anio'])
        valores=list(df1['Citas_recibidas'])
        valores2=list(df1['Articulos'])
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Add traces
        fig.add_trace(
            go.Scatter(x=leyenda, y=valores, name="Citas recibidas"),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(x=leyenda, y=valores2, name="Articulos"),
            secondary_y=True,
        )

        # Add figure title
        fig.update_layout(
            title_text="Citas recibidas por los documentos según año de publicación"
        )

        # Set x-axis title
        fig.update_xaxes(title_text="Anios")

        # Set y-axes titles
        fig.update_yaxes(title_text="Citas_recibidas", secondary_y=False)
        fig.update_yaxes(title_text="Articulos", secondary_y=True)

        fig.write_image("citasarticulos.jpg")
        fig.write_html("citasarticulos.html")

    def filtro_anio(self, anio):
        return general.df_anio_art[general.df_anio_art['Anio'] == int(float(anio))]
    
    def filtro_Tipo_Doc(self, tipo):
        return general.df_tipo_doc_art[general.df_tipo_doc_art['Tipo_de_documento'] == str(tipo)]
    
    def filtro_idioma(self, idioma):
        return general.df_idioma_art[general.df_idioma_art['Idioma'] == str(idioma)]
    
    def filtro_Tipo_OA(self, oa):
        return general.df_oa_art[general.df_oa_art['Tipo_oa'] == str(oa)]
    
    def filtro_categoria(self, cat):
        return general.df_categoria[general.df_categoria['Nombre_categoria'] == str(cat)]
    
    def filtro_financiamiento(self, fin_ins):
        return general.df_financiamiento_art[general.df_financiamiento_art['Institucion'] == str(fin_ins)]


def guardar_df(df:pd.DataFrame):
    archivo = filedialog.asksaveasfilename(title='Guardar tabla...', defaultextension='.xlsx', filetypes=[('XLSX', '*.xlsx')]) #va título, directorio de inicio (raíz) tipos que soporta //  initialdir='/', para inicializar el directorio en el puro inicio
    if not archivo.endswith('.xlsx'):
            archivo += '.xlsx'
    archivo=str(archivo)
    archivo=archivo.replace('/', '\\')
    df.to_excel(archivo)

def guardar_modelo_excel():
    import os
    baseDatos.ARTICULO.to_excel("ARTICULO.xlsx")
    baseDatos.BDKEY_ARTICULO.to_excel("BDKEY_ARTICULO.xlsx")
    baseDatos.BDKEYWORD.to_excel("BDKEYWORD.xlsx")
    baseDatos.CATEGORIA_ARTICULO.to_excel("CATEGORIA_ARTICULO.xlsx")
    baseDatos.CATEGORIA.to_excel("CATEGORIA.xlsx")
    baseDatos.SUB_CATEGORIA.to_excel("SUB_CATEGORIA.xlsx")
    baseDatos.AUTOR.to_excel("AUTOR.xlsx")
    baseDatos.AUTOR_ARTICULO.to_excel("AUTOR_ARTICULO.xlsx")
    baseDatos.AU_KEYWORD.to_excel("AU_KEYWORD.xlsx")
    baseDatos.AUKEY_ARTICULO.to_excel("AUKEY_ARTICULO.xlsx")
    baseDatos.FUENTE.to_excel("FUENTE.xlsx")
    baseDatos.OA_ARTICULO.to_excel("OA_ARTICULO.xlsx")
    baseDatos.OPEN_ACCESS.to_excel("OPEN_ACCESS.xlsx")
    baseDatos.INSTITUCION_ARTICULO.to_excel("INSTITUCION_ARTICULO.xlsx")
    baseDatos.INSTITUCION.to_excel("INSTITUCION.xlsx")
    baseDatos.PAIS.to_excel("PAIS.xlsx")
    baseDatos.FINANCIAMIENTO_ARTICULO.to_excel("FINANCIAMIENTO_ARTICULO.xlsx")
    baseDatos.FINANCIAMIENTO.to_excel("FINANCIAMIENTO.xlsx")
    return "Tus archivos se encuentran en: \n" + str(os.getcwd())

    
def main():
    autores.autores_mas_productivos(autores)   
    autores.elite(autores)
    instituciones.instituciones_mas_productivos(instituciones)
    revistas.revistas_mas_citados(revistas)
    revistas.revistas_mas_productivos(revistas)
    palabras.graficos(palabras)
    general.graf_gen(general)
    general.oa(general)
    general.categoria(general)
    general.financiamiento(general)
    general.citas_articulo(general)
    pais.llenar_paises(pais)
    pais.colaboración(pais)


if __name__ != "__main__":
    main()

        
    