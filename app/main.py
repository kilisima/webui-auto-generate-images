import streamlit as st
import dotenv
dotenv.load_dotenv(".env", override=True)
from library.ImageGenerate import ImageGenerate, GenerateConfig
import asyncio
from PIL import Image
from io import BytesIO
import glob
import os

async def main():
    st.set_page_config("Generate NovelAI", layout="wide")
    st.title("Generate Novel AI")
    with st.container(border=True):
        input_context = st.text_area("Input Context")
        negative_prompt = st.text_area("Negative Prompt")
        n_samples = st.number_input("n_samples", value=3)
        clicked = st.button("Submit", "submit")
    

    if 'files' not in st.session_state:
        st.session_state['files'] = []

    if clicked :
        gc = GenerateConfig(negative_prompt=negative_prompt, n_samples=n_samples)
        with st.spinner():
            ig = ImageGenerate(gc)
            _results = await ig.generate_files(input_context=input_context)
            st.session_state['files'].extend(_results)

    with st.container(border=True):
        cols = st.columns(4)
        for i in range(len(st.session_state['files'])):
            col = i % 4
            filepath = st.session_state['files'][i]
            print(f"i:{i} col:{col} filepath:{filepath}")
            img = Image.open(filepath)
            basename = os.path.basename(filepath)
            with cols[col]:
                st.image(img)
                with open(filepath, "rb") as f:
                    st.download_button("download", f, basename)

        pass


if __name__ == "__main__":
    asyncio.run(main())
    pass