import streamlit as st

# Título de la aplicación
st.title("Conversor de Divisas y Calculadora de Cambio")

# Campo para ingresar la tasa de cambio manualmente
tasa_cambio = st.number_input("Ingrese la tasa de cambio actual (1 USD = ? VES):", min_value=0.0)

# Campo para ingresar el monto en bolívares
monto_bolivares = st.number_input("Ingrese el monto del consumo en bolívares:", min_value=0.0)

# Campo para ingresar el pago en dólares
pago_dolares = st.number_input("Ingrese el monto pagado en dólares:", min_value=0.0, disabled=not monto_bolivares)

# Función para calcular el cambio
def calcular_cambio(monto_bolivares, pago_dolares, tasa_cambio):
    """Calcula el cambio en dólares."""
    monto_dolares = monto_bolivares / tasa_cambio
    cambio = pago_dolares - monto_dolares
    return cambio

# Botón para calcular el cambio
if st.button("Calcular Cambio"):
    if monto_bolivares > 0 and pago_dolares > 0 and tasa_cambio > 0:
        cambio = calcular_cambio(monto_bolivares, pago_dolares, tasa_cambio)
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
        st.warning("Por favor, ingrese todos los valores.")
