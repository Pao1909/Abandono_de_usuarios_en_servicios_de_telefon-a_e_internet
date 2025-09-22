import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Datos de desempeño de modelos
# -------------------------------
data = {
    "Modelo": [
        "Regresión Logística",
        "Árbol de Decisión",
        "Bosque Aleatorio",
        "Clasificador XGBoost",
        "Clasificador LightGBM",
        "Modelo CatBoost"
    ],
    "AUC-ROC Train": [0.855636, 0.898190, 0.999981, 1.000000, 1.000000, 1.000000],
    "AUC-ROC Test": [0.839871, 0.793259, 0.879189, 0.919240, 0.917880, 0.925614],
    "Accuracy Train": [0.818844, 0.835022, 0.996089, 1.000000, 1.000000, 1.000000],
    "Accuracy Test": [0.793177, 0.778252, 0.841507, 0.875622, 0.878465, 0.889126]
}

df = pd.DataFrame(data)

# -------------------------------
# Dashboard en Streamlit
# -------------------------------
st.title("📊 Evaluación de Modelos de Clasificación")
st.markdown("""
Este dashboard muestra el desempeño de varios modelos de machine learning 
entrenados para predecir la deserción de clientes en la empresa **Interconnect**.
""")

# Mostrar tabla completa
st.subheader("Resultados de todos los modelos")
st.dataframe(df)

# -------------------------------
# Gráficos comparativos
# -------------------------------
st.subheader("Comparación de AUC-ROC en Test")
fig, ax = plt.subplots()
df.plot(x="Modelo", y="AUC-ROC Test", kind="bar",
        ax=ax, legend=False, color="skyblue")
plt.xticks(rotation=45, ha="right")
plt.ylabel("AUC-ROC (Test)")
plt.title("Comparación de AUC-ROC en el conjunto de prueba")
st.pyplot(fig)

st.subheader("Comparación de Accuracy en Test")
fig, ax = plt.subplots()
df.plot(x="Modelo", y="Accuracy Test", kind="bar",
        ax=ax, legend=False, color="orange")
plt.xticks(rotation=45, ha="right")
plt.ylabel("Accuracy (Test)")
plt.title("Comparación de Accuracy en el conjunto de prueba")
st.pyplot(fig)

# -------------------------------
# Destacar mejor modelo
# -------------------------------
mejor_modelo = df.loc[df["Accuracy Test"].idxmax()]
st.success(
    f"✅ El mejor modelo fue **{mejor_modelo['Modelo']}**, con un Accuracy Test de **{mejor_modelo['Accuracy Test']:.3f}** y un AUC-ROC Test de **{mejor_modelo['AUC-ROC Test']:.3f}**.")

# -------------------------------
# Sección interactiva por modelo
# -------------------------------
st.subheader("🔍 Ver métricas de modelos específicos")

# Permitir seleccionar uno o varios modelos
modelos_seleccionados = st.multiselect(
    "Selecciona los modelos", df["Modelo"], default=df["Modelo"][0])

if modelos_seleccionados:
    df_seleccionados = df[df["Modelo"].isin(modelos_seleccionados)]
    st.dataframe(df_seleccionados)

    # Gráfico comparativo de los modelos seleccionados
    fig, ax = plt.subplots()
    df_seleccionados.plot(
        x="Modelo",
        y=["AUC-ROC Test", "Accuracy Test"],
        kind="bar",
        ax=ax,
        color=["skyblue", "orange"]
    )
    plt.ylim(0, 1)
    plt.ylabel("Valor")
    plt.title("Métricas de los modelos seleccionados")
    plt.xticks(rotation=45, ha="right")
    st.pyplot(fig)
