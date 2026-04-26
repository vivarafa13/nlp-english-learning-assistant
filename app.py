import streamlit as st
import google.generativeai as genai
import os

# Configuración de la página
st.set_page_config(page_title="Método Bremerton - NLP Assistant", layout="centered")

# 1. Configuración de la API (Secreto en Streamlit Cloud o Input en Demo)
st.sidebar.title("Configuración")
api_key = st.sidebar.text_input("Ingresa tu Gemini API Key:", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-3-flash-preview')

    st.title("📚 Método Bremerton: Fase 1")
    st.markdown("---")

    # 2. Análisis Funcional - Input
    col1, col2 = st.columns(2)
    with col1:
        keyword = st.text_input("Palabra clave:", placeholder="Ej: Disconcerting")
    with col2:
        context = st.text_area("Contexto (<20 palabras):", placeholder="The news was disconcerting for the investors.")

    if st.button("Generar ADN Semántico"):
        if keyword and context:
            # 3. Proceso - Prompt Engineering
            prompt = f"""
            Actúa como un experto lingüista del Método Bremerton para IELTS.
            Analiza la palabra '{keyword}' dentro del contexto: '{context}'.
            
            Entrega el resultado en este formato:
            1. ADN de la Palabra: (Pronunciación IPA y significado pragmático).
            2. THE VIBE: (Una analogía visual poderosa para fijar el concepto).
            """
            
            with st.spinner("Procesando en servidores de Google..."):
                response = model.generate_content(prompt)
                
                # 4. Output - Visualización
                st.subheader("Resultado del Análisis")
                st.info(response.text)
                
                # Contador de Tokens (Simulado según el modelo Flash)
                st.caption(f"⚡ Procesamiento completado. Latencia: Baja. Costo: $0 (Capa gratuita).")
        else:
            st.warning("Por favor, completa ambos campos.")
else:
    st.info("Por favor, ingresa tu API Key de Google AI Studio en la barra lateral para comenzar.")
