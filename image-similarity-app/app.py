import streamlit as st
import numpy as np
from PIL import Image
from db_utils import save_image, load_images
from model import extract_features
from similarity import cosine_similarity

st.set_page_config(page_title="AI Image Similarity", layout="centered")

st.title("🧠 AI Image Similarity Engine")

uploaded = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded:
    new_img = np.array(Image.open(uploaded).convert("RGB"))

    st.image(new_img, caption="Uploaded Image", width=300)

    new_features = extract_features(new_img)

    db_images = load_images()

    if len(db_images) == 0:
        st.warning("No images in DB. Saving first image...")
        save_image("first_image", new_img)
    else:
        results = []

        for name, db_img, db_features in db_images:
            sim = cosine_similarity(new_features, db_features)
            similarity_percent = sim * 100

            results.append((name, similarity_percent, db_img))

        # 🔥 FILTER (>80%)
        filtered = [r for r in results if r[1] > 80]

        st.subheader("🔥 Similar Images (>80%)")

        if len(filtered) == 0:
            st.warning("No similar images found")
        else:
            filtered = sorted(filtered, key=lambda x: x[1], reverse=True)

            for name, sim, img in filtered:
                st.write(f"{name} → {sim:.2f}%")
                st.image(img, width=200)

        # 🏆 Best Match
        best = max(results, key=lambda x: x[1])

        st.subheader("🏆 Best Match")
        st.write(f"{best[0]} → {best[1]:.2f}%")

        st.image([new_img, best[2]], width=250)

        # 💾 Save Button
        if st.button("💾 Save Image"):
            save_image("img_" + str(np.random.randint(10000)), new_img)
            st.success("Saved to DB 🚀")