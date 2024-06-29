# Helmet_Detection_Using_YOLOv10

## 1. Installation
`conda` virtual environment is recommended
```cmd
conda create -n yolov10_env
conda activate yolov10_env

pip install -r requirements.txt
pip install git+https://github.com/THU-MIG/yolov10.git
pip install ultralytics

pip install -e .
```

## 2. Usage
1. Open `main.ipynb`
2. Run 1, 2 and the 6 for a prediction. Remember to change the `src_img`, `save_path`. Change `model_path` if you want to use another model. 