import streamlit as st
from PIL import Image
import time

# --- PAGE CONFIG ---
st.set_page_config(page_title="Shilp-Setu AI Studio", page_icon="🎨", layout="wide")

# --- CUSTOM CSS FOR MINIMALIST UI ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #2E7D32; color: white; }
    .product-card { padding: 20px; border-radius: 15px; background: white; border: 1px solid #ddd; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🎨 Shilp-Setu: AI Virtual Business Manager")
st.markdown("### Empowering Marginalized Artisans through AI-Driven Digital Cataloging")
st.divider()

# --- SIDEBAR (Settings & Digital Literacy Support) ---
with st.sidebar:
    st.header("App Settings")
    language = st.selectbox("Choose Language / भाषा चुनें", ["English", "Hindi (हिंदी)", "Marathi (मराठी)", "Tamil (தமிழ்)"])
    st.info("This app is designed for low-literacy users. Use the Voice or Camera buttons to start.")

# --- MAIN INTERFACE ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Product Image Studio")
    uploaded_file = st.file_uploader("Upload Product Photo (Handicrafts/Textiles)", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Original Photo (Cluttered Background)", use_container_width=True)
        
        if st.button("✨ Auto-Enhance & Remove Background"):
            with st.spinner("AI is cleaning the background..."):
                time.sleep(2) # Simulating AI processing
                # In a real app, you'd use the 'rembg' library here
                st.success("Background Removed! Lighting Corrected.")
                st.image(img, caption="AI Enhanced (Professional Studio Look)", use_container_width=True)

with col2:
    st.subheader("2. Smart Cataloging (Voice-to-Text)")
    voice_input = st.text_area("Describe your product (or click Mic for Voice Note):", 
                              placeholder="e.g., This is a hand-woven blue silk saree from Banaras...")
    
    cost_price = st.number_input("What is your making cost? (₹)", min_value=0)

    if st.button("🚀 Generate Digital Listing"):
        if voice_input:
            with st.spinner("AI is translating and generating description..."):
                time.sleep(2)
                
                # --- SIMULATED AI OUTPUT ---
                st.markdown("---")
                st.markdown("### 📋 Final Marketplace Listing")
                
                tab1, tab2 = st.tabs(["English (Global)", "Hindi (Local)"])
                
                with tab1:
                    st.write("**Product Name:** Premium Authentic Hand-Woven Silk Saree")
                    st.write("**Description:** This exquisite piece features traditional craftsmanship with intricate patterns. Sourced from local artisans, perfect for formal occasions.")
                    st.write("**SEO Tags:** #Handmade #ArtisanSaree #EthicalFashion #VocalForLocal")
                
                with tab2:
                    st.write("**उत्पाद का नाम:** प्रीमियम प्रामाणिक हाथ से बुनी रेशम की साड़ी")
                    st.write("**विवरण:** यह उत्कृष्ट टुकड़ा जटिल पैटर्न के साथ पारंपरिक शिल्प कौशल को दर्शाता है।")

                # --- PRICING ALGORITHM ---
                st.subheader("3. Dynamic Pricing Suggestion")
                suggested_price = cost_price * 1.4  # Simple logic: Cost + 40% margin
                st.metric(label="Recommended Selling Price", value=f"₹{suggested_price:,.2f}", delta="Competitive Market Rate")
                st.write("💡 *AI Analysis: Similar items are selling for ₹{0} on Government e-Marketplace (GeM).*".format(suggested_price+200))

# --- FOOTER ---
st.divider()
if st.button("✅ Publish to e-Commerce Platforms (GeM / ONDC / Amazon)"):
    st.balloons()
    st.success("Product successfully pushed to Digital Markets!")
