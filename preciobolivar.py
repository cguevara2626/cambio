import streamlit as st
import requests

def obtener_precio_dolar_bolivar():
    url = "https://v6.exchangerate-api.com/v6/7f1b4e91f2e33fba0b3b1909/latest/USD"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        precio_bolivar = datos['conversion_rates']['VES']
        return precio_bolivar
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener el precio del dólar: {e}")
        return None

# Título de la aplicación
st.title("Conversor de Divisas: Dólar a Bolívar")

# Botón para actualizar el precio
if st.button("Actualizar Precio"):
    precio = obtener_precio_dolar_bolivar()
    if precio:
        st.success(f"El precio actual del dólar en bolívares es: {precio} VES")
    else:
        st.warning("No se pudo obtener el precio del dólar en este momento.")