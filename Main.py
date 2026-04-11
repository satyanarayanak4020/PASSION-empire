import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Passion Empire", page_icon="👑", layout="wide")

# --- CUSTOM CSS ---
# This makes the buttons and text look a bit more "Empire" chic
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #2E4053;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("👑 Passion Empire")
st.subheader("Building a legacy through creativity and drive.")
st.divider()

# --- CONTENT SLOTS ---
# We use columns to create the "picture slots" side-by-side
col1, col2, col3 = st.columns(3)

with col1:
    # Slot 1
    st.image("https://via.placeholder.com/400x300", caption="Creative Ventures")
    st.markdown("### Art & Design")
    st.write("Exploring the visual boundaries of the digital empire.")
    if st.button("Explore Gallery"):
        st.toast("Entering the Gallery...")

with col2:
    # Slot 2
    st.image("https://via.placeholder.com/400x300", caption="Technical Mastery")
    st.markdown("### Development")
    st.write("Building the infrastructure of the future, one line at a time.")
    if st.button("View Projects"):
        st.success("Loading GitHub Repository!")

with col3:
    # Slot 3
    st.image("https://via.placeholder.com/400x300", caption="Strategic Growth")
    st.markdown("### Strategy")
    st.write("Planning the next moves for global influence and reach.")
    if st.button("Read Manifesto"):
        st.info("Opening the Empire Strategy...")

# --- FOOTER ---
st.divider()
st.caption("© 2026 Passion Empire | Built with Streamlit & GitHub")
