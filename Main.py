import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Passion Empire", page_icon="👑", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .mega-title {
        font-size: 80px !important; font-weight: 800; text-align: center;
        text-transform: uppercase; letter-spacing: 5px; margin-top: -50px;
        background: -webkit-linear-gradient(#eee, #333);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .mega-subtitle { text-align: center; font-size: 20px; opacity: 0.7; margin-bottom: 50px; }
    div[data-testid="column"] {
        background-color: #111111; padding: 25px; border-radius: 15px;
        border: 1px solid #222222; transition: transform 0.3s;
    }
    div[data-testid="column"]:hover { transform: translateY(-5px); border: 1px solid #D4AF37; }
    .stLinkButton>a {
        width: 100% !important; border-radius: 8px !important;
        background-color: #FFFFFF !important; color: #000000 !important;
        font-weight: bold !important; height: 50px !important;
        display: flex !important; align-items: center !important;
        justify-content: center !important; text-decoration: none !important;
    }
    .stLinkButton>a:hover { background-color: #D4AF37 !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="mega-title">PASSION</h1>', unsafe_allow_html=True)
st.markdown('<p class="mega-subtitle">Empire</p>', unsafe_allow_html=True)
st.divider()

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.image("https://images.unsplash.com/photo-1585110396054-c8112ca9625f?w=400&h=300&fit=crop", use_container_width=True)
    st.markdown("### MrBunny AI")
    st.write("Transforming how we interact with technology through AI.")
    st.link_button("Enter Vault", "https://mrbunnyai-v2.streamlit.app/")

with col2:
    st.image("https://images.unsplash.com/photo-1493863641943-9b68992a8d07?w=400&h=300&fit=crop", use_container_width=True)
    st.markdown("### PASSION X")
    st.write("The Beautiful Photography And Editing Studio Of The Passion Empire.")
    st.link_button("View Source", "https://sites.google.com/d/1iay-5VKvQotpczcXwQ8so0hCiiGg4zNt/p/1W3OFBAgfBlDdTiM5Du9z0RO8-6FHAkE3/edit")

with col3:
    st.image("https://images.unsplash.com/photo-1558769132-cb1aea458c5e?w=400&h=300&fit=crop", use_container_width=True)
    st.markdown("### SIEGE EMPIRE CLOTHING")
    st.write("Global reach into the clothing business. [Co-founded by Ethan Morris]")
    st.link_button("Launch Plan", "https://siegetheclothingempire.streamlit.app/")

st.divider()
st.markdown("<div style='text-align: center; opacity: 0.5;'>EST. 2026 | BUILT FOR PASSION</div>", unsafe_allow_html=True)