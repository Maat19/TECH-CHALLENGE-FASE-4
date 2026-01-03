import streamlit as st
import pandas as pd
import joblib

# ==============================
# Configuração da página
# ==============================
st.set_page_config(
    page_title="Predição de Obesidade",
    layout="centered"
)

st.title("🏥 Sistema Preditivo de Obesidade")
st.write(
    "Este sistema utiliza Machine Learning para auxiliar profissionais da saúde "
    "na identificação do nível de obesidade de um paciente."
)

# ==============================
# Carregamento do pipeline
# ==============================
@st.cache_resource
def carregar_modelo():
    return joblib.load("pipeline_obesity.pkl")

pipeline = carregar_modelo()

# ==============================
# Formulário de entrada
# ==============================
st.subheader("📋 Informações do Paciente")

with st.form("form_obesidade"):
    
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gênero", ["Male", "Female"])
        age = st.number_input("Idade", min_value=14, max_value=100, value=25)
        height = st.number_input("Altura (m)", min_value=1.40, max_value=2.20, value=1.70)
        weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
        family_history = st.selectbox("Histórico familiar de sobrepeso?", ["yes", "no"])
        favc = st.selectbox("Consome alimentos altamente calóricos?", ["yes", "no"])

    with col2:
        fcvc = st.slider("Consumo de vegetais (1 = raramente, 3 = sempre)", 1, 3, 2)
        ncp = st.slider("Número de refeições principais por dia", 1, 4, 3)
        caec = st.selectbox("Come entre as refeições?", ["no", "Sometimes", "Frequently", "Always"])
        smoke = st.selectbox("Fuma?", ["yes", "no"])
        ch2o = st.slider("Consumo diário de água (1 = <1L, 3 = >2L)", 1, 3, 2)
        scc = st.selectbox("Monitora calorias ingeridas?", ["yes", "no"])
        faf = st.slider("Frequência de atividade física (0 a 3)", 0, 3, 1)
        tue = st.slider("Tempo usando dispositivos eletrônicos (0 a 2)", 0, 2, 1)
        calc = st.selectbox("Consumo de álcool", ["no", "Sometimes", "Frequently", "Always"])
        mtrans = st.selectbox(
            "Meio de transporte",
            ["Automobile", "Motorbike", "Bike", "Public_Transportation", "Walking"]
        )

    submit = st.form_submit_button("🔍 Realizar Predição")

# ==============================
# Predição
# ==============================
if submit:
    imc = weight / (height ** 2)

    dados_entrada = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "IMC": round(imc, 2),
        "family_history": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }])

    predicao = pipeline.predict(dados_entrada)[0]

    st.success(f"🧠 **Nível de obesidade previsto:** {predicao}")
    st.info(f"📊 IMC calculado: {round(imc, 2)}")