import streamlit as st
import requests
import json
import uuid

# ---------------------------------------------------------
# 🔑 CONFIGURATION
# ---------------------------------------------------------
BASE_API_URL = "https://aws-us-east-2.langflow.datastax.com/lf/d9b5c7dd-2716-4be9-ba3e-a1bec0332180/api/v1/run/fb49c613-a8e7-4f04-9d6d-c94e9f676c74"
LANGFLOW_ID = "d9b5c7dd-2716-4be9-ba3e-a1bec0332180"
FLOW_ID = "fb49c613-a8e7-4f04-9d6d-c94e9f676c74"
APPLICATION_TOKEN = "AstraCS:ZDZdfZfQQExaOmwaUYElTShr:c7e7316b1a3632665f4e4345e943b34756421db6819486bfcf68dcd2a683982e" # <--- PASTE YOUR TOKEN HERE

# ---------------------------------------------------------
# 🎨 FORCE THEME & UI SETUP
# ---------------------------------------------------------
st.set_page_config(
    page_title="Kisan-Mitra v2.0", 
    page_icon="🚜", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Force Light Mode & Custom Gradient via HTML Injection
st.markdown("""
    <style>
        /* Force Text Color to Black for Light Mode compatibility */
        body, .stMarkdown, .stText, h1, h2, h3, p {
            color: #333333 !important;
        }
        
        /* Main Gradient Background */
        .stApp {
            background: linear-gradient(135deg, #e0f7fa 0%, #e8f5e9 100%) !important;
        }

        /* Header Styling */
        .header-container {
            background-color: #ffffff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            margin-bottom: 2rem;
            border-bottom: 5px solid #2e7d32;
        }
        
        /* Chat Message Styling */
        .user-message {
            background-color: #d1f2eb;
            color: #0b5345;
            padding: 15px;
            border-radius: 20px 20px 0 20px;
            margin: 10px 0;
            text-align: right;
            font-weight: 500;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }
        .bot-message {
            background-color: #ffffff;
            color: #2c3e50;
            padding: 15px;
            border-radius: 20px 20px 20px 0;
            margin: 10px 0;
            text-align: left;
            border-left: 5px solid #27ae60;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
        }
        
        /* Button Styling */
        .stButton>button {
            background-color: #ffffff;
            border: 2px solid #2e7d32;
            color: #2e7d32;
            border-radius: 10px;
            font-weight: bold;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #2e7d32;
            color: white;
            border-color: #2e7d32;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 🧠 BACKEND LOGIC
# ---------------------------------------------------------
def run_flow(message: str):
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}"
    payload = {
        "input_value": message,
        "output_type": "chat",
        "input_type": "chat",
        "session_id": str(uuid.uuid4())
    }
    headers = {"Authorization": "Bearer " + APPLICATION_TOKEN, "Content-Type": "application/json"}
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# ---------------------------------------------------------
# 📱 UI STRUCTURE
# ---------------------------------------------------------

# Header
st.markdown('<div class="header-container"><h1>🚜 Kisan-Mitra AI <span style="font-size:0.5em; vertical-align:top; color:#2e7d32">v2.0</span></h1><p style="font-size:1.1em; color:#555;">Intelligent Farm Advisory System powered by <b>IBM Watsonx</b></p></div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎛️ Control Panel")
    st.markdown("---")
    st.info("📊 **Live System Status**")
    st.progress(100)
    st.caption("All Systems Operational")
    
    st.markdown("### 🌍 Region Settings")
    st.selectbox("Select State", ["Punjab", "Maharashtra", "Gujarat", "Karnataka"])
    st.selectbox("Soil Type", ["Alluvial", "Black Soil", "Red Loam"])
    
    st.markdown("---")
    st.warning("⚠️ **Alert:** Heavy rains predicted in Nashik region for next 48h.")

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Quick Actions
st.markdown("### ⚡ Quick Assistant")
col1, col2, col3, col4 = st.columns(4)

def quick_ask(query):
    st.session_state.messages.append({"role": "user", "content": query})
    st.rerun()

if col1.button("🌾 Best Fertilizer?"): quick_ask("What is the best fertilizer for Wheat?")
if col2.button("🐛 Identify Pest"): quick_ask("How to treat whitefly on Cotton?")
if col3.button("💰 Market Price"): quick_ask("Current mandi price for Onion?")
if col4.button("📅 Sowing Date"): quick_ask("When should I sow Mustard?")

st.markdown("---")

# Display Messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-message">{message["content"]}</div>', unsafe_allow_html=True)

# Input Area
prompt = st.chat_input(" Ask your question here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.markdown(f'<div class="user-message">{prompt}</div>', unsafe_allow_html=True)

    with st.spinner("🤖 Analyzing Soil Reports & Market Data..."):
        response_data = run_flow(prompt)
        try:
            text = response_data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
            st.session_state.messages.append({"role": "assistant", "content": text})
            st.rerun()
        except:
            st.error("Connection Error. Please check API Token.")