import streamlit as st
from PIL import Image, ImageOps
import time

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Kala Setu | AI Artisan Studio", 
    page_icon="🌉", 
    layout="wide"
)

# --- 2. CUSTOM CSS FOR MINIMALIST DESIGN ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1e7e34;
        color: white;
    }
    .status-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Sorted Multilingual Support) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063822.png", width=100)
    st.title("App Settings")
    
    # List of languages with native scripts
    languages = [
        "Assamese (অসমীয়া)", "Bengali (বাংলা)", "Bodo (बर')", 
        "Dogri (डोगरी)", "English", "Gujarati (ગુજરાતી)", 
        "Hindi (हिंदी)", "Kannada (ಕನ್ನಡ)", "Kashmiri (کأشُر)", 
        "Konkani (कोंकणी)", "Maithili (मैथिली)", "Malayalam (മലയാളം)", 
        "Marathi (मराठी)", "Meitei (ꯃꯩꯇꯩꯂꯣꯟ)", "Nepali (नेपाली)", 
        "Odia (ଓଡ଼ିଆ)", "Punjabi (ਪੰਜਾਬੀ)", "Sanskrit (संस्कृतम्)", 
        "Santali (संताली)", "Sindhi (سنڌي)", "Tamil (தமிழ்)", 
        "Telugu (తెలుగు)", "Urdu (اردو)"
    ]
    
    # Sorting alphabetically
    sorted_languages = sorted(languages)
    
    selected_lang = st.selectbox(
        "Choose Language / भाषा चुनें", 
        sorted_languages,
        index=sorted_languages.index("English") # Default to English
    )
    
    st.divider()
    st.markdown("### **Support**")
    st.info("💡 **Tip:** Hold the microphone button to describe your craft in your local language.")
    st.button("📞 Call Support")

# --- 4. MAIN INTERFACE ---
st.title("🌉 Kala Setu: AI-Driven Market Linkage")
st.markdown("#### *Empowering Marginalized Artisans through Smart Digital Cataloging*")
st.divider()

col1, col2 = st.columns(2, gap="large")

# --- COLUMN 1: AI IMAGE STUDIO ---
with col1:
    st.subheader("1. Product Image Studio")
    uploaded_file = st.file_uploader("Upload Product Photo (Handicrafts/Textiles)", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Original Photo", use_container_width=True)
        
        if st.button("✨ Enhance & Remove Background"):
            with st.spinner("AI Studio is cleaning your image..."):
                time.sleep(2) # Simulating AI Background Removal
                st.success("✅ Background Removed! Lighting Corrected.")
                # For demo, we just display the same image as "processed"
                st.image(img, caption="Professional Catalog Image", use_container_width=True)

# --- COLUMN 2: SMART CATALOGER ---
with col2:
    st.subheader("2. Smart Cataloging (Voice-to-Text)")
    
    voice_input = st.text_area(
        "Describe your product (or click Mic for Voice Note):", 
        placeholder="e.g., This is a hand-woven blue silk saree from Banaras with gold embroidery...",
        height=150
    )
    
    cost_price = st.number_input("What is your making cost? (₹)", min_value=0, step=100)

    if st.button("🚀 Generate Digital Listing"):
        if voice_input:
            with st.spinner("AI is translating and generating SEO description..."):
                time.sleep(2)
                
                st.markdown("---")
                st.write("### 📋 Generated Listing")
                
                tab1, tab2 = st.tabs(["English Listing", "Native Listing"])
                
                with tab1:
                    st.write("**Title:** Premium Handcrafted Silk Textile")
                    st.write(f"**Description:** An authentic masterpiece. {voice_input[:50]}... crafted with high-quality sustainable materials for global markets.")
                    st.write("**SEO Tags:** #Handmade #ArtisanMade #EthicalFashion")
                
                with tab2:
                    st.write("**शीर्षक:** प्रीमियम हस्तनिर्मित उत्पाद")
                    st.write("**विवरण:** यह उत्कृष्ट टुकड़ा पारंपरिक शिल्प कौशल को दर्शाता है।")

                # Pricing Algorithm
                st.divider()
                st.subheader("💰 Dynamic Pricing Assistant")
                suggested_price = cost_price * 1.5
                st.metric(label="Suggested Selling Price", value=f"₹{suggested_price:,.2f}", delta="+50% Margin")
                st.caption("AI Analysis: Similar items on GeM/Amazon sell for ₹{0}".format(suggested_price + 150))

# --- 5. FINAL PUBLISHING ACTION ---
st.divider()
if st.button("✅ Publish to e-Commerce Platforms (GeM / ONDC / Amazon)", type="primary"):
    with st.spinner("Pushing to digital markets..."):
        time.sleep(1.5)
        st.balloons()
        st.success("Product successfully pushed to Digital Markets!")
