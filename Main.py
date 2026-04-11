import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Passion", page_icon="👑", layout="wide")

# --- DARK THEME & LARGE TITLE CSS ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    
    /* THE HUGE CENTERED TITLE */
    .mega-title {
        font-size: 80px !important;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 5px;
        margin-top: -50px;
        margin-bottom: 10px;
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* CENTERED SUBHEADER */
    .mega-subtitle {
        text-align: center;
        font-size: 20px;
        letter-spacing: 2px;
        opacity: 0.7;
        margin-bottom: 50px;
    }

    /* Style the cards/slots */
    div[data-testid="column"] {
        background-color: #111111;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #222222;
        transition: transform 0.3s;
    }
    
    div[data-testid="column"]:hover {
        transform: translateY(-5px);
        border: 1px solid #D4AF37;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        background-color: #FFFFFF;
        color: #000000;
        font-weight: bold;
        border: none;
        height: 45px;
    }
    
    .stButton>button:hover {
        background-color: #D4AF37;
        color: #000000;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CENTERED MEGA TITLE ---
st.markdown('<h1 class="mega-title">PASSION</h1>', unsafe_allow_html=True)
st.markdown('<p class="mega-subtitle">Empire</p>', unsafe_allow_html=True)

st.divider()

# --- CONTENT SLOTS ---
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.image("https://via.placeholder.com/400x300/222222/FFFFFF?text=Empire+Visuals", use_container_width=True)
    st.markdown("### DESIGN")
    st.write("Visualizing the empire through high-end design and dark mode elegance.")
    st.button("Enter Vault", key="btn1")

with col2:
    st.image("https://via.placeholder.com/400x300/222222/FFFFFF?text=Core+Systems", use_container_width=True)
    st.markdown("### CODE")
    st.write("The technical backbone and code driving the passion forward.")
    st.button("View Source", key="btn2")

with col3:
    st.image("https://via.placeholder.com/400x300/222222/FFFFFF?text=Global+Reach", use_container_width=True)
    st.markdown("### STRATEGY")
    st.write("Strategy for scaling the empire and reaching new territories.")
    st.button("Launch Plan", key="btn3")

# --- FOOTER ---
st.divider()
st.markdown("<div style='text-align: center; opacity: 0.5;'>EST. 2026 | BUILT ON PRIDE</div>", unsafe_allow_html=True)
