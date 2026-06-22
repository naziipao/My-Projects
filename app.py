import streamlit as st
from PIL import Image
from engine import scan_image

def main():
    """
    The Main Function: Handles the visual layout configurations, page assets, 
    user upload behaviors, and application state.
    """
    st.set_page_config(page_title="Image Descriptor", layout="centered")
    st.title("🥇 Local AI Image Scanner")
    st.write("Using a premium single model configuration for maximum detailed accuracy.")

    CHOSEN_MODEL = 'qwen2.5vl:7b'

    uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        
        if st.button("Generate Image Description"):
            with st.spinner(f"Running intensive analysis via '{CHOSEN_MODEL}'..."):
                try:
                    # Call the imported function
                    short_desc, long_desc = scan_image(image, CHOSEN_MODEL)
                    
                    st.success("Analysis Complete!")
                    
                    # Renders visual interface components
                    st.markdown("### **Quick Summary**")
                    st.info(short_desc)
                    
                    st.markdown("---") 
                    
                    st.markdown("### **Detailed Description**")
                    st.write(long_desc)
                    
                except Exception as e:
                    st.error(f"Execution Error: {e}")

if __name__ == "__main__":
    main()
