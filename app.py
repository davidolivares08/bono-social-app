import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calculadora Bono Social", layout="centered")

st.title("Calculadora de Bono Social Eléctrico")
st.write("Complete el formulario para determinar su categoría de descuento.")

with st.form("calculadora_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        renta = st.number_input("Renta anual de la unidad (€)", min_value=0.0, step=100.0)
        mayores = st.number_input("Nº de adultos", min_value=1, step=1)
        menores = st.number_input("Nº de menores", min_value=0, step=1)
    
    with col2:
        st.write("**Situaciones específicas:**")
        f_numerosa = st.checkbox("Familia Numerosa")
        p_minima = st.checkbox("Pensión Mínima")
        imv = st.checkbox("Ingreso Mínimo Vital (IMV)")
        especiales = st.checkbox("Discapacidad >=33% / Violencia / Terrorismo")

    enviar = st.form_submit_button("Realizar Cálculo")

if enviar:
    resultado = ""
    descuento = ""
    es_vulnerable = False

    if f_numerosa or imv:
        resultado = "Consumidor Vulnerable"
        descuento = "65%"
        es_vulnerable = True
    elif p_minima:
        resultado = "Consumidor Vulnerable"
        descuento = "65%"
        es_vulnerable = True
    else:
        # Lógica de umbral IPREM simplificada
        limite = 12600 # Base orientativa
        if especiales:
            limite += 4200
        
        if renta <= limite:
            resultado = "Consumidor Vulnerable"
            descuento = "65%"
            es_vulnerable = True
        else:
            resultado = "No cumple requisitos"
            descuento = "0%"

    if es_vulnerable:
        st.success(f"**Resultado:** {resultado}")
        st.info(f"**Descuento estimado:** {descuento}")
    else:
        st.error(f"**Resultado:** {resultado}")