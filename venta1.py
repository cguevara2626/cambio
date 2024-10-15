import streamlit as st
import pandas as pd
import datetime

def save_data(product_a, product_b, date):
    """Guarda los datos de venta en un archivo CSV.

    Args:
        product_a: Cantidad de Producto A vendida.
        product_b: Cantidad de Producto B vendida.
        date: Fecha de la venta.
    """

    try:
        df = pd.read_csv('ventas_diarias.csv')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Fecha', 'Producto A', 'Producto B'])

    new_data = {'Fecha': date, 'Producto A': product_a, 'Producto B': product_b}
    df = pd.concat([df, pd.DataFrame(new_data, index=[0])], ignore_index=True)
    df.to_csv('ventas_diarias.csv', index=False)

def query_data(start_date, end_date):
    try:
        df = pd.read_csv('ventas_diarias.csv', parse_dates=['Fecha'])
        # Convertimos las fechas de entrada a formato datetime
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        filtered_df = df[(df['Fecha'] >= start_date) & (df['Fecha'] <= end_date)]
        return filtered_df
    except FileNotFoundError:
        st.error("No se encontraron datos de ventas.")
        return None
        
# Título de la aplicación
st.title('Registro y Consulta de Ventas Diarias')

# Menú
page = st.sidebar.selectbox("Selecciona una opción", ["Agregar Venta", "Consultar Ventas"])

if page == "Agregar Venta":
    # Obtener los datos del usuario
    product_a = st.number_input('Cantidad de Producto A vendida hoy:', min_value=0)
    product_b = st.number_input('Cantidad de Producto B vendida hoy:', min_value=0)
    date = st.date_input('Fecha de la venta')

    # Botón para guardar los datos
    if st.button('Guardar'):
        save_data(product_a, product_b, date)
        st.success('Datos guardados correctamente')

elif page == "Consultar Ventas":
    start_date = st.date_input("Fecha de inicio")
    end_date = st.date_input("Fecha de fin")

    if st.button("Consultar"):
        results = query_data(start_date, end_date)
        if results is not None:
            st.dataframe(results)
        else:
            st.info("No se encontraron ventas en el rango de fechas seleccionado.")