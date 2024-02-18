# FaceMash Nano

This repo is made just for fun to compare images to select the best picture from
local picture database.

## How to run locally
* Clone repo:
```
git clone
cd facemash_nano
```
* Put your images to ```static``` folder. Remove file ```PUT_YOUR_IMAGES_HERE```
* Create virtual env with ```python>=3.10```:
```bash
python3 -m venv venv
source venv/bin/activate # For Mac/Linux
venv\Scripts\activate # For Windows 
```
* Install all python dependencies:
```bash
pip install -r requirements.txt
```

* Run:
```bash
python app.py --data-format jpeg # For jpeg pictures 
```
