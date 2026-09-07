import streamlit as st

# Mipangilio ya Ukurasa
st.set_page_config(page_title="Subalo High School", page_icon="🎓", layout="centered")

# Mtindo wa Muonekano (CSS Styling)
st.markdown("""
    <style>
    .stApp {
        background-color: #2e7d32;
        color: white;
    }
    .stButton>button {
        width: 100%;
        background-color: #d32f2f;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #b71c1c;
        color: white;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Hali ya Uhifadhi wa Hatua (Session State)
if "step" not in st.session_state:
    st.session_state.step = 1

# KIOO CHA 1: LOGIN SCREEN
if st.session_state.step == 1:
    st.title("STUDENTS REGISTRATION SYSTEM")
    st.subheader("SUBALO HIGH SCHOOL")
    
    st.image("https://img.icons8.com/color/192/000000/graduation-cap.png", width=150)
    
    st.write("---")
    if st.button("LOGIN"):
        st.session_state.step = 2
        st.rerun()

# KIOO CHA 2: WELCOME SCREEN
elif st.session_state.step == 2:
    st.title("SUBALO HIGH SCHOOL")
    st.info("Karibu kwenye mfumo wa usajili wa wanafunzi.")
    
    st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=400", caption="Karibu Subalo High School", width=250)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("BACK"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button("OPEN"):
            st.session_state.step = 3
            st.rerun()

# KIOO CHA 3: CHOOSE COMBINATION
elif st.session_state.step == 3:
    st.title("WELCOME TO OUR SCHOOL")
    st.write("Please choose combination you want to read:")
    
    combination = st.radio("Chagua Mchepuo:", ["PCB", "PCM", "CBG", "EGM", "HGK", "HGL"], index=0)
    st.session_state.combination = combination

    col1, col2 = st.columns(2)
    with col1:
        if st.button("BACK"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        if st.button("NEXT"):
            st.session_state.step = 4
            st.rerun()

# KIOO CHA 4: SUBJECTS LIST
elif st.session_state.step == 4:
    st.title("SUBJECTS TO STUDY")
    st.write(f"Masomo ya mchepuo wa **{st.session_state.get('combination', 'PCB')}**:")
    
    masomo = [
        "1. PHYSICS",
        "2. CHEMISTRY",
        "3. BIOLOGY",
        "4. GEOGRAPHY",
        "5. ECONOMICS",
        "6. GENERAL STUDIES",
        "7. BASIC APPLIED MATHEMATICS"
    ]
    for somo in masomo:
        st.write(f"- {somo}")
        
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("BACK"):
            st.session_state.step = 3
            st.rerun()
    with col2:
        if st.button("REGISTER"):
            st.session_state.step = 5
            st.rerun()

# KIOO CHA 5: REGISTRATION STATUS / CONFIRM
elif st.session_state.step == 5:
    st.title("REGISTRATION STATUS")
    st.success("Congratulations! You are being registered at SUBALO HIGH SCHOOL - SHINYANGA.")
    
    st.write(f"**Mchepuo Ulizochagua:** {st.session_state.get('combination', 'PCB')}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("BACK"):
            st.session_state.step = 4
            st.rerun()
    with col2:
        if st.button("CONFIRM"):
            st.session_state.step = 6
            st.rerun()

# KIOO CHA 6: SUCCESS SCREEN
elif st.session_state.step == 6:
    st.title("REGISTERED SUCCESSFULLY")
    st.subheader("REGISTRATION COMPLETED!!!")
    
    st.image("https://img.icons8.com/color/144/000000/checked-checkbox.png", width=120)
    
    if st.button("HOME"):
        st.session_state.step = 1
        st.rerun()