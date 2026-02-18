import streamlit as st
import time

# --- పేజీ కాన్ఫిగరేషన్ ---
st.set_page_config(page_title="Chai AI Studio | BioTwin x Learnomine", page_icon="☕", layout="centered")

# --- కస్టమ్ స్టైలింగ్ (CSS) ---
st.markdown("""
    <style>
    /* మెయిన్ బ్యాక్ గ్రౌండ్ - వార్మ్ చాయ్ థీమ్ */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1576092768241-dec231879fc3?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
    }
    
    /* లాగిన్ కార్డ్ స్టైలింగ్ */
    .login-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 40px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        text-align: center;
    }

    /* బటన్ స్టైలింగ్ */
    .stButton>button {
        background: linear-gradient(45deg, #D27D2D, #F5DEB3);
        color: #1a120b !important;
        border: none;
        padding: 10px 25px;
        border-radius: 50px;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px #D27D2D;
    }

    h1, h2, p {
        color: #F5DEB3 !important;
        font-family: 'Georgia', serif;
    }
    </style>
    """, unsafe_allow_html=True)

# --- సెషన్ స్టేట్ మెయింటెనెన్స్ ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- లాగిన్ పేజీ ---
if not st.session_state.logged_in:
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.container():
        st.markdown("""
            <div class="login-card">
                <h1>☕ The Chai AI Studio</h1>
                <p>Collaborating with <b>Learnomine</b></p>
                <p style="font-size: 0.9rem; opacity: 0.8;">Blending AI + Storytelling + 3D Design</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ఇన్పుట్ ఫీల్డ్స్
        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            username = st.text_input("Creator ID", placeholder="Enter your ID")
            access_key = st.text_input("Master Access Key", type="password", placeholder="••••••••")
            
            if st.button("Unlock Creative Node"):
                if access_key == "CHAI_AI_2026": # మీ పాస్‌వర్డ్
                    st.session_state.logged_in = True
                    st.success("Access Granted! Loading Characters...")
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.error("Invalid Key. Please try again.")

# --- మెయిన్ డ్యాష్‌బోర్డ్ (Login తర్వాత వచ్చేది) ---
else:
    st.sidebar.markdown("### 🛠️ Production Tools")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.update({"logged_in": False}))
    
    st.title("🎬 Creative Production Dashboard")
    st.info("Project Status: **Final Rendering & Storytelling Audit**")

    # క్యారెక్టర్స్ ప్రివ్యూ సెక్షన్
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎭 Character Selection")
        char = st.selectbox("Choose an Ingredient", ["Ginger (The Brave)", "Cardamom (The Sassy)", "Tea Leaves (The Wise)"])
        st.write(f"**Concept:** Making {char} come alive using AI Visuals.")
        if st.button("Show Storyboard"):
            st.toast("Fetching 3D Textures...")
            st.image("https://images.unsplash.com/photo-1599021456807-25db0f974333?q=80&w=1932&auto=format&fit=crop", caption="Character Reference")

    with col2:
        st.markdown("### ⚡ AI Reel Preview")
        st.write("Current Work-in-progress Reel")
        # ఇక్కడ మీ అసలు వీడియో ఫైల్ పాత్ ఇవ్వండి
        st.video("https://www.w3schools.com/html/mov_bbb.mp4") 

    st.divider()
    st.markdown("#### 💡 Thought of the Day")
    st.write("> *'Design thinking is not just about aesthetics; it's about solving the problem of engagement in a digital-first world.'*")
