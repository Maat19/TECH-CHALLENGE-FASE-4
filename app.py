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
# ==============================
# Título e descrição
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

mapa_binario = {"Sim": "yes", "Não": "no"}
mapa_caec_calc = {
    "Não": "no",
    "Às vezes": "Sometimes",
    "Frequentemente": "Frequently",
    "Sempre": "Always"
}
mapa_genero = {"Masculino": "Male", "Feminino": "Female"}
mapa_transporte = {
    "Carro": "Automobile",
    "Moto": "Motorbike",
    "Bicicleta": "Bike",
    "Transporte Público": "Public_Transportation",
    "A pé": "Walking"
}
mapa_resultado = {
    "Insufficient_Weight": "Abaixo do peso",
    "Normal_Weight": "Peso normal",
    "Overweight_Level_I": "Sobrepeso - Nível I",
    "Overweight_Level_II": "Sobrepeso - Nível II",
    "Obesity_Type_I": "Obesidade - Tipo I",
    "Obesity_Type_II": "Obesidade - Tipo II",
    "Obesity_Type_III": "Obesidade - Tipo III"
}
mapa_freq_vegetais = {
    "Raramente": 1,
    "Às vezes": 2,
    "Sempre": 3
}
mapa_refeicoes_dia = {
    "Uma refeição": 1,
    "Duas refeições": 2,
    "Três refeições": 3,
    "Quatro ou mais refeições": 4
}

mapa_litros_agua = {
    "<1L": 1,
    "1-2L": 2,
    ">2L": 3
}

mapa_atividade_fisica = {
    "Nenhuma": 0,
    "1-2 vezes por semana": 1,
    "3-4 vezes por semana": 2,
    "5 ou mais vezes por semana": 3
}

mapa_tempo_uso_eletronicos = {
    "0-2 horas por dia": 0,
    "3-5 horas por dia": 1,
    "Mais de 5 horas por dia": 2
}


with st.form("form_obesidade"):
    
    col1, col2 = st.columns(2)

    with col1:
        gender = mapa_genero[st.selectbox("Gênero", list(mapa_genero.keys()))]
        age = st.number_input("Idade", min_value=14, max_value=100, value=25)
        height = st.number_input("Altura (m)", min_value=1.40, max_value=2.20, value=1.70)
        weight = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
        family_history = mapa_binario[st.selectbox("Histórico familiar de sobrepeso?", list(mapa_binario.keys()))]
        favc = mapa_binario[st.selectbox("Consome alimentos altamente calóricos?", list(mapa_binario.keys()))]

    with col2:
        fcvc = mapa_freq_vegetais[st.selectbox("Consumo de vegetais", list(mapa_freq_vegetais.keys()))]
        ncp = mapa_refeicoes_dia[st.selectbox("Número de refeições principais por dia", list(mapa_refeicoes_dia.keys()))]
        caec = mapa_caec_calc[st.selectbox("Come entre as refeições?", list(mapa_caec_calc.keys()))]
        smoke = mapa_binario[st.selectbox("Fuma?", list(mapa_binario.keys()))]
        ch2o = mapa_litros_agua[st.selectbox("Consumo diário de água", list(mapa_litros_agua.keys()))]
        scc = mapa_binario[st.selectbox("Monitora calorias ingeridas?", list(mapa_binario.keys()))]
        faf = mapa_atividade_fisica[st.selectbox("Frequência de atividade física", list(mapa_atividade_fisica.keys()))]
        tue = mapa_tempo_uso_eletronicos[st.selectbox("Tempo usando dispositivos eletrônicos", list(mapa_tempo_uso_eletronicos.keys()))]
        calc = mapa_caec_calc[st.selectbox("Consumo de álcool", list(mapa_caec_calc.keys()))]
        mtrans = mapa_transporte[st.selectbox("Meio de transporte", list(mapa_transporte.keys()))]

    submit = st.form_submit_button("🔍 Realizar Predição")

# ==============================
# Predição
# ==============================
if submit:
    if height <= 0:
        st.error("Altura inválida.")
        st.stop()

    imc = weight / (height ** 2)

    if imc < 18.5:
        faixa = "Abaixo do peso"
    elif imc < 25:
        faixa = "Peso normal"
    elif imc < 30:
        faixa = "Sobrepeso"
    else:
        faixa = "Obesidade"

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
    predicao_pt = mapa_resultado.get(predicao, predicao)

    st.success(f"🩺**Nível de obesidade previsto:** {predicao_pt}")
    st.info(f"📊 IMC calculado: {round(imc, 2)} — Classificação clínica: {faixa}")