import streamlit as st

# Configuração da página (deixa o título na aba do navegador bonitinho)
st.set_page_config(page_title="Mensagem Especial", page_icon="💖")

# Título do seu site secreto
st.title("💖 Se liguem nisso aqui...")

# Criando a caixa de texto
nome = st.text_input("Digite seu nome:")

# A lógica mágica que você criou
if nome:
    # Transformando em minúsculo para aceitar "Carol", "carol", "CAROL", etc.
    nome_limpo = nome.lower()

    if nome_limpo in ["ana carolina", "carol", "mari", "mariana"]:
        st.balloons() # Isso vai soltar balões na tela delas! 🎈
        st.header(f"✨ Amandinha ama demais vocês, {nome.capitalize()}!!! <3 ✨")
        st.subheader("Obrigada por serem as melhores! 🌸")
    else:
        st.write(f"Olá {nome}! Que bom te ver por aqui. 😊")
