import streamlit as st
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image, ImageDraw
# Set page configuration
st.set_page_config(page_title="Color Segmentation Tool", page_icon="🎨", layout="centered")

st.title("Color Segmentation Tool")
st.text("Extract the 3 most dominant colors from any uploaded image.")

st.text("")  # One line break
st.text("")  # Another line break

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

col1,col2 = st.columns(2)
# Display the uploaded image

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    with col1:
        st.image(image, caption="Uploaded Image", width=150)


    # Convert image data to a numpy array and reshape for KMeans
    image_np = np.array(image)
    X = image_np.reshape(-1, 3)

    # Perform KMeans clustering to find 3 dominant colors
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(X)
    dominant_colors = kmeans.cluster_centers_.astype(int)

    # Function to create a color palette
    def create_color_palette(dominant_colors, palette_size=(300, 50)):
        # Create an image to display the colors
        palette = Image.new("RGB", palette_size)
        draw = ImageDraw.Draw(palette)

        # Calculate the width of each color swatch
        swatch_width = palette_size[0] // len(dominant_colors)

        # Draw each color as a rectangle on the palette
        for i, color in enumerate(dominant_colors):
            draw.rectangle([i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]], fill=tuple(color))

        return palette

    # Generate and display the color palette
    palette_image = create_color_palette(dominant_colors)

    db = st.button("Show dominant colors")
    if db:
        with col2:
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.text("")
            st.image(palette_image, caption="Dominant Colors Palette", width=300)
else:
    st.info("Upload an image to get started!")




