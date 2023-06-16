import streamlit as st
import os

import pdf2image

st.set_page_config(
    # layout="wide",    
    page_title="Read the Economist",
    page_icon="📰",
    initial_sidebar_state="expanded",
)    

st.title('Read the Economist')


folders = [i for i in os.listdir() if '.' not in i and 'utils' not in i]
left, right,= st.columns([1,4])
with left:
    edition = st.selectbox(label = 'Choose Edition', options = sorted(folders, reverse=True) )
with right:
    file = st.selectbox(label="Select file", options = sorted(os.listdir(edition), reverse=True))

left_, right_,= st.columns(2)
with left_:
    method = st.selectbox(label="Read or Download", options = ['Read Online','Download'])
with right_:
    dpi = st.selectbox(label="DPI", options = [100,150,200,300])

submitted = st.button('Submit')

st.markdown('---')
if submitted:
    filepath = os.path.join(edition,file)
    if method == 'Download':
        with st.expander('Download pdf'):
            with open(os.path.join(edition,file),'rb') as f:
                bytes_ = f.read()
            st.download_button(f'Download {file}', data=bytes_, file_name=file)

    elif method == 'Read Online':
        def yield_images(filepath,dpi):
            with open(filepath,'rb') as f:
                images = pdf2image.convert_from_bytes(
                    f.read(),
                    dpi=dpi,
                    thread_count=-1
                )
            yield images
        with st.container():
            images = yield_images(filepath,dpi)
            st.image(images.__next__(), use_column_width=True)


