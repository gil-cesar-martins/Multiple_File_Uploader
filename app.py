import streamlit as st
import os
from PIL import Image


@st.cache_resource
def load_image(image_file):
    img = Image.open(image_file)
    return img


# Salva o arquivo de upload
def save_uploaded_file(uploaded_file):
    with open(os.path.join("tempDir", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success("Salvo {} : em tempDir".format(uploaded_file.name))


def main():
    st.title("Upload de múltiplos arquivos")

    menu = ["Home", "Sobre"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Upload de muitos arquivos")
        uploadedfiles = st.file_uploader(
            "Upload de Múltiplas Imagens",
            type=["png", "jpeg", "jpg"],
            accept_multiple_files=True,
        )
        if uploadedfiles is not None:
            st.write(uploadedfiles)  # List
            for imagefile in uploadedfiles:
                st.write(imagefile.name)
                st.image(load_image(imagefile), width=250)
                # Save individual File
                save_uploaded_file(imagefile)
    else:
        st.subheader("Sobre o app")


if __name__ == "__main__":
    main()
