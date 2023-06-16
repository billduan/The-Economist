import streamlit as st
import os

import pdf2image
import base64

st.set_page_config(
    layout="wide",    
    page_title="Chat with GPT4",
    page_icon="🤖",
    initial_sidebar_state="expanded",
)    

st.title('Read the Economist')


folders = [i for i in os.listdir() if '.' not in i and 'utils' not in i]
left, mid, right, rightx2 = st.columns([1,4,1,1])
with left:
    edition = st.selectbox(label = 'Choose Edition', options = sorted(folders, reverse=True) )
with mid:
    file = st.selectbox(label="Select file", options = sorted(os.listdir(edition), reverse=True))
with right:
    method = st.selectbox(label="Options", options = ['Read Online','Download'])
with rightx2:
    dpi = st.selectbox(label="Options", options = [50,100,200,300])

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
            # for page in images:
            #     st.image(page, use_column_width=True)
    # else:
    #     with open(filepath,'rb') as f:
    #         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    #     pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf">' 
    #     st.markdown(pdf_display, unsafe_allow_html=True)



# for edition in folders:
#     with st.expander(edition):
#         st.write(
#             os.listdir(edition)
#         )


