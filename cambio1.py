import streamlit as st
import requests

def obtener_tasa_cambio():
    """Obtiene la tasa de cambio actual del dólar estadounidense frente al bolívar."""
    url = "https://v6.exchangerate-api.com/v6/7f1b4e91f2e33fba0b3b1909/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['conversion_rates']['VES']
    except requests.exceptions.RequestException as e:
        st.error(f"Error al obtener la tasa de cambio: {e}")
        return None


def calcular_cambio(monto_bolivares, pago_dolares):
    """Calcula el cambio en dólares."""
    tasa_cambio = obtener_tasa_cambio()
    if tasa_cambio is None:
        return None
    
    monto_dolares = monto_bolivares / tasa_cambio
    cambio = pago_dolares - monto_dolares
    return cambio


# Título de la aplicación
st.title("Conversor de Divisas y Calculadora de Cambio")

# Obtener la tasa de cambio al inicio
tasa_cambio = obtener_tasa_cambio()

# Campo para ingresar el monto en bolívares
monto_bolivares = st.number_input("Ingrese el monto del consumo en bolívares:", min_value=0.0)

# Mostrar la tasa de cambio actual
if tasa_cambio:
    st.write(f"La tasa de cambio actual es: 1 USD = {tasa_cambio} VES")

# Campo para ingresar el pago en dólares
pago_dolares = st.number_input("Ingrese el monto pagado en dólares:", min_value=0.0, disabled=not monto_bolivares)

# Botón para calcular el cambio
if st.button("Calcular Cambio"):
    if monto_bolivares > 0 and pago_dolares > 0:
        cambio = calcular_cambio(monto_bolivares, pago_dolares)
        if cambio is not None:
            # Convertir el pago en dólares a bolívares
            pago_bolivares = pago_dolares * tasa_cambio

            if cambio > 0:
                # Convertir el cambio a bolívares
                cambio_bolivares = cambio * tasa_cambio
                st.success(f"Tu cambio es: {cambio:.2f} USD ({cambio_bolivares:.2f} VES)")
            elif cambio == 0:
                st.success("Pago exacto.")
            else:
                st.error("El pago es insuficiente.")
        else:
            st.warning("No se pudo calcular el cambio debido a un error en la tasa de cambio.")
    else:
        st.warning("Por favor, ingrese ambos montos.")
