import streamlit as st
from ultralytics import YOLOv10
import numpy as np
from PIL import Image


def main():
    st.title('Safety Helmet Detection for Image')
    file = st.file_uploader('Upload image', type=['jpg', 'png', 'jpeg'])

    model = YOLOv10('helmet_detection_best_yolov10b.pt')

    if file is not None:
        b = file.getvalue()
        with open("test.png", "wb") as f:
            f.write(b)

        detection = model.predict(source='test.png', conf=0.4)

        detection[0].save('detected.png')
        col1, col2 = st.columns(2)
        with col1:
            st.image(file, caption='Uploaded Image')
        with col2:
            st.image('detected.png', caption='Detected Image')


if __name__ == "__main__":
    main()
# streamlit run app.py --server.enableXsrfProtection false
