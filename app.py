import streamlit as st

# Simulação de banco de usuários com cargos
usuarios = {
    "admin": {"senha": "1234", "cargo": "admin"},
    "monitor": {"senha": "5678", "cargo": "monitor"}
}

# Controle de sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False

def login():
    st.title("Sistema Instituto Araras")
    st.subheader("🔐 Login")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            st.session_state["logado"] = True
            st.session_state["usuario"] = usuario
            st.session_state["cargo"] = usuarios[usuario]["cargo"]
            st.success(f"Bem-vindo(a), {usuario}!")
        else:
            st.error("Usuário ou senha incorretos.")

def sistema():
    st.sidebar.title(f"Usuário: {st.session_state['usuario']}")
    st.sidebar.write(f"Cargo: {st.session_state['cargo']}")

    menu = st.sidebar.radio("Menu", ["Matrículas", "Sair"])

    if menu == "Matrículas":
        st.header("Cadastro de Participantes")
        with st.form("form_matricula"):
            nome = st.text_input("Nome completo")
            idade = st.number_input("Idade", 1, 100)
            projeto = st.selectbox("Projeto", ["Araras em Movimento", "Alfabetização", "Pré-vestibular"])
            enviado = st.form_submit_button("Cadastrar")
        if enviado:
            st.success(f"Participante {nome} cadastrado!")
    elif menu == "Sair":
        st.session_state.clear()
        st.experimental_rerun()

if not st.session_state["logado"]:
    login()
else:
    sistema()


