import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Passion Empire", page_icon="👑", layout="wide")

# --- DARK THEME CSS ---
st.markdown("""
    <style>
    /* Main background and text colors */
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    
    /* Style the cards/slots */
    div[data-testid="column"] {
        background-color: #111111;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333333;
    }

    /* Titles and Subheaders */
    h1, h2, h3, p {
        color: #FFFFFF !important;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #FFFFFF;
        color: #000000;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #D4AF37; /* Gold hover effect */
        color: #000000;
    }

    /* Divider color */
    hr {
        border-top: 1px solid #333333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("👑 PASSION EMPIRE")
st.markdown("<p style='font-size: 20px; opacity: 0.8;'>Command your destiny. Build your legacy.</p>", unsafe_allow_html=True)
st.divider()

# --- CONTENT SLOTS ---
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    # Slot 1
    st.image("https://via.placeholder.com/400x300/222222/FFFFFF?text=Empire+Visuals", use_container_width=True)
    st.markdown("### The Aesthetic")
    st.write("Visualizing the empire through high-end design and dark mode elegance.")
    if st.button("Enter Vault"):
        st.balloons()

with col2:
    # Slot 2
    st.image("https://via.placeholder.com/400x300/222222/FFFFFF?text=Core+Systems", use_container_width=True)
    st.markdown("### The Engine")
    st.write("The technical backbone and code driving the passion forward.")
    if st.button("View Source"):
        st.snow()

with col3:
    # Slot 3
    st.image("https://via.placeholder.com/400x300/222222/FFFFFF?text=Global+Reach", use_container_width=True)
    st.markdown("### The Expansion")
    st.write("Strategy for scaling the empire and reaching new territories.")
    if st.button("Launch Plan"):
        st.toast("Expansion initialized...")

# --- FOOTER ---
st.divider()
st.caption("EST. 2026 | POWERED BY PASSION")
