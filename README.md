# Helmet_Detection_Using_YOLOv10

## 1. Installation
`conda` virtual environment is recommended
```cmd
conda create -n yolov10_env
conda activate yolov10_env

pip install -r requirements.txt
pip install git+https://github.com/THU-MIG/yolov10.git
pip install ultralytics
pip install streamlit

pip install -e .
```

## 2. Usage
### 1. Using JupyterNotebook
1. Open `train.ipynb`
2. Chose the `yolov10_env` kernel
3. Run 1, 2 and the 6 for a prediction. Remember to change the `src_img`, `save_path`. Change `model_path` if you want to use another model.
### 2. Using streamlit app
```cmd
%cd Helmet_Detection_Using_YOLOv10/YOLOv10
conda activate yolov10_env
streamlit run app.py
```