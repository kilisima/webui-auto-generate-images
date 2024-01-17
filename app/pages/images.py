import streamlit as st
import os
import glob
from PIL import Image
import dotenv
dotenv.load_dotenv(".env", override=True)

def isImageExt(filepath:str) -> bool:
    root, extension = os.path.splitext(filepath)
    print(f"root:{root} ext:{extension}")
    if extension.lower() == ".jpg":
        return True
    elif extension.lower() == ".jpeg":
        return True
    elif extension.lower() == ".png":
        return True
    else:
        return False

def search_files(dir_path:str) -> [str]:
    types = ('jpg', 'png', 'jpeg')
    files = []
    for t in types:
        files += glob.glob(os.path.join(dir_path, '*.' + t ))
    return files

def main():
    st.title("Images")
    dir_path = os.getenv("STORAGE_PATH")
    st.write(dir_path)
    files = search_files(dir_path)
    files.sort(reverse=True)
    with st.expander("filename list"):
        st.write("files:", files)

    with st.container(border=True):
        cols = st.columns(4)
        for i in range(len(files)):
            col = i % 4
            filepath = files[i]
            print(f"i:{i} col:{col} filepath:{filepath}")
            if isImageExt(filepath):
                # stream = BytesIO(st.session_state['results'][i])
                img = Image.open(filepath)
                with cols[col]:
                    st.image(img)
                    filename_with_extension = os.path.basename(filepath)
                    with open(filepath, "rb") as fb:
                        st.download_button("download", fb, filename_with_extension)


    pass

if __name__ == "__main__":
    main()
    pass