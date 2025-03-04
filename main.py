import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuracion de la pagina
st.set_page_config(
    page_title="Dashboard",
    page_icon="🧮",
    layout="wide"
)

# TItulo principal
st.title("📈 Testing Dashboard")
st.markdown("*Visualizalo todo*")


# Crea un objeto expandible
with st.expander("Introduccion", expanded=True):
    st.markdown("""
                 Demustra el uso de diferentes bibliotecas de visualizacion:
                * **Matplotlib**: Biblioteca base para visualizacion de datos
                * **Seaborn**: Visualizaciones estadisticas
                * **Plotly**: Graficos interactivos
                * **Streamlit**: Framework para aplicaciones de datos 
                """)
    
try: 
    # Carga de los datasets
    prog_df = pd.read_csv('data/prs.csv').query('year == 2022')
    iris_df = pd.read_csv('data/Iris.csv')
    st.success("✅Datos cargados exitosamente")
    
    # Visualizar datos
    st.header("🎨 Visualizaciones con Matplotlib")
    # Se crea un contenedor
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("Grafico de Dispersion")
            fig,ax = plt.subplots(figsize=(8,6)) # fig contiene la figura y ax los eje
            languges = prog_df['name'].head(5)
            users = prog_df['count'].head(5)
            ax.scatter(languges,users,color='blue', alpha=0.6)
            plt.xticks(rotation=45)
            plt.title('Cantitdad de PRs por Lenguaje de Programacion')
            plt.xlabel('Lenguaje')
            plt.ylabel('Cantidad de PRs')
            st.pyplot(fig)
            plt.close()
            
        with col2:
            st.subheader("Grafico de Barras")
            fig,ax = plt.subplots(figsize=(8,6)) # fig contiene la figura y ax los eje
            languges = prog_df['name'].head(5)
            users = prog_df['count'].head(5)
            ax.bar(languges,users,color='skyblue')
            plt.xticks(rotation=45)
            plt.title('Cantitdad de PRs por Lenguaje de Programacion')
            plt.xlabel('Lenguaje')
            plt.ylabel('Cantidad de PRs')
            st.pyplot(fig)
            plt.close()
    
    # Visualizar datos con Searborn
    st.header("🎨 Visualizaciones con Seaborn")
     # Se crea un contenedor
    with st.container():
        col1,col2 = st.columns(2)
        with col1:
            st.subheader("Grafico de Violin")
            fig,ax = plt.subplots(figsize=(8,6)) # fig contiene la figura y ax los eje
            sns.violinplot(data=iris_df, x='Species', y='SepalLengthCm')
            plt.xticks(rotation=45)
            plt.title('Distribuicion de longitud del Sepalo por Especie')
            st.pyplot(fig)
            plt.close()
        with col2:
            st.subheader("Grafico de Cajas")
            fig,ax = plt.subplots(figsize=(8,6)) # fig contiene la figura y ax los eje
            sns.boxplot(data=iris_df, x='Species', y='PetalLengthCm')
            plt.xticks(rotation=45)
            plt.title('Estadistica de longitud del Petalo por Especie')
            st.pyplot(fig)
            plt.close()
            
    
    # Visualizar datos de manera interactiva
    st.header("🎨 Visualizaciones Interactivas")
    # Grafico de lineas interactivo
      # Se crea un contenedor
    with st.container():
        fig = px.line(prog_df,
                      x='name',
                      y='count',
                      title='Tendencia de uso',
                      markers=True)
        st.plotly_chart(fig,use_container_width=True)
        
        
        fig = px.pie(prog_df,
                      names='name',
                      values='count',
                      title='Tendencia de uso')
        st.plotly_chart(fig,use_container_width=True)
        
        
    
    # Seccion interactiva
    st.header("🔄️ Visualizaciones Interactivas ")
    # Dataset
    dataset_choice = st.radio(
        "Selecciona el conjunto de datos",
        ["Lenguaje de programacion", "Iris Datase"]
    )
    
    # Validacion de dataset
    if dataset_choice == 'Lenguaje de programacion' :
        df = prog_df
    else :
        df = iris_df
    
    # Tipo de grafico
    chart_type = st.selectbox(
        "Selecciona el tipo de grafico",
        ["Barras", "Dispersion", "Linea"]
    )
    
    # Selector de datos
    x_axis = st.selectbox("Selecciona el eje x", df.columns)
    y_axis = st.selectbox("Selecciona el eje y", df.columns)
    
    if chart_type == "Barras":
        fig = px.bar(df,x=x_axis, y=y_axis)
    elif chart_type == "Dispersion":
        fig = px.scatter(df,x=x_axis, y=y_axis)
    else:
        fig = px.line(df,x=x_axis, y=y_axis)
        
    st.plotly_chart(fig,use_container_width=True)
    
except Exception as e:
    st.error(f"Error al cargar los datos: {str(e)}")
    st.error(f"Por favor verifique que los datos existen en el directorio data")