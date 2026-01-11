import streamlit as st
import qrcode
from PIL import Image
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Paul's QR Master", page_icon="📱")

# --- OWNER SECTION (Your Picture) ---
# This creates a sidebar or top section with your details
col1, col2 = st.columns([1, 3])

with col1:
    try:
        # Make sure 'owner.jpg' is in the folder!
        st.image("owner.jpg", width=100)
    except:
        st.write("📷")  # Emoji fallback if photo missing

with col2:
    st.title("QR Master")
    st.markdown("**Created by: Kamtchoum Paul Kevyn**")
    st.caption("Generate professional QR Codes instantly.")

st.divider()

# --- INPUTS ---
website_link = st.text_input("1. Paste your Link or Text here:")
file_name = st.text_input("2. Name your file (e.g., my_code):")
qr_color = st.color_picker("3. Pick a Color", "#000000")

# --- GENERATE BUTTON ---
if st.button("Generate QR Code 🚀", type="primary"):
    if website_link and file_name:

        # Create QR
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(website_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=qr_color, back_color="white")

        # --- SHOW RESULT ---
        st.success("QR Code Generated!")
        st.image(img.get_image(), caption=f"QR Code for: {file_name}")

        # --- DOWNLOAD BUTTON ---
        # We need to turn the image into a downloadable file in memory
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")

        st.download_button(
            label="Download Image 📥",
            data=img_buffer,
            file_name=f"{file_name}.png",
            mime="image/png"
        )
    else:
        st.warning("Please fill in both the Link and the Filename!")
