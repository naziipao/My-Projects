import streamlit as st
from PIL import Image
from engine import scan_image

def main():
    """
    The Main Function: Handles the visual layout configurations, page assets, 
    user upload behaviors, and application state.
    """
    st.set_page_config(page_title="Image Descriptor", layout="centered")
    st.title("Smart AI Image Descriptor")
    st.write("Using a premium single model configuration for maximum detailed accuracy.")

    chosen_model = 'qwen2.5vl:7b'
    st.write(f"Current Model: **{chosen_model}**")

    uploaded_file = st.file_uploader("Choose an image:", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        image.thumbnail((550,550))
        st.image(image, caption="Uploaded Image")
        
        if st.button("Generate Image Description"):
            with st.spinner(f"Running intensive analysis via '{chosen_model}'..."):
                try:
                    # Call the imported function
                    short_desc, long_desc = scan_image(image, chosen_model)
                    
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
