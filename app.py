import streamlit as st

st.set_page_config(page_title="Mensagem Especial", page_icon="💖")
st.title("💖 Se liguem nisso aqui...")

nome = st.text_input("Digite seu nome:")

if nome:
    nome_limpo = nome.lower()
    
    # Se for uma das meninas, solta os balões!
    if nome_limpo in ["ana carolina", "carol", "mari", "mariana"]:
        st.balloons() 

    # A frase agora é a mesma para TODO MUNDO (fora do if dos nomes)
    st.header(f"✨ Amandinha ama demais você, {nome.capitalize()}!!! <3 ✨")
    st.subheader("Obrigada existir na minha vida! 🌸") 
