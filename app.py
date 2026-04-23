import paho.mqtt.client as paho
import time
import streamlit as st
import json
import platform

# Configuración de la página
st.set_page_config(
    page_title="🌼 Motor Casa de Campo",
    page_icon="🌻",
    layout="centered"
)

# Estilos girly 🌼💛🌿
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff9db 0%, #e6ffe6 100%);
    }
    h1, h2, h3 {
        color: #6c9a2b;
        text-align: center;
    }
    .stButton>button {
        background-color: #ffd966;
        color: #5a5a00;
        border-radius: 12px;
        border: none;
        padding: 10px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #ffe680;
    }
    </style>
""", unsafe_allow_html=True)

# Info sistema
st.write("🌼 Versión de Python:", platform.python_version())

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("🌻 El motor recibió la orden correctamente\n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write("💌 Mensaje del sistema:", message_received)

broker = "157.230.214.127"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

# Título
st.title("🌻 Control del Motor - Casa de Campo")

st.markdown("### 🌿 Panel de control del sistema de Carla")

# Botones ON/OFF
col1, col2 = st.columns(2)

with col1:
    if st.button('🌼 Encender Luces'):
        act1 = "ON"
        client1 = paho.Client("Motor_Casa_Campo")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("carlaluces_s", message)
    else:
        st.write('')

with col2:
    if st.button('🌸 Apagar Luces'):
        act1 = "OFF"
        client1 = paho.Client("Motor_Casa_Campo")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("carlaluces_s", message)
    else:
        st.write('')

st.divider()

# Control analógico
st.markdown("### 🌷 Ajuste de potencia del motor")

values = st.slider('🌼 Nivel de funcionamiento', 0.0, 100.0)
st.write('🌿 Nivel seleccionado:', values)

if st.button('🌻 Enviar nivel al motor'):
    client1 = paho.Client("Motor_Casa_Campo")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("carlamotor_a", message)
else:
    st.write('')

st.divider()

st.markdown("💛 *El motor mantiene viva la casita de campo de Carla, cuidando cada rincón con amor y energía 🌼🏡*")




