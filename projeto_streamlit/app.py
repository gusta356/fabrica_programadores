import streamlit as st 

st.title("minha primeira pagina")
st.subheader("feito com streamlit")


valor1 = st.number_input("digite o primeiro numero",min_value=0.0)
valor2 = st.number_input("digite o segundo numero",min_value=0.0)

if st.button("calcular"):
    resultado = valor1 + valor2
    st.title(  resultado)