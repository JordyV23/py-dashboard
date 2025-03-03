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
    prog_df = pd.read_csv('data/prs.csv')
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
            
        with col2:
            st.subheader("Grafico de Barras")
            
    
except Exception as e:
    st.error(f"Error al cargar los datos: {str(e)}")
    st.error(f"Por favor verifique que los datos existen en el directorio data")