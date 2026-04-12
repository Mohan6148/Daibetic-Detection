# Diabetes Detection Django Project

A simple Django web app that predicts whether a person is diabetic from medical input values.

## Description

The project uses a saved scikit-learn model, a Django form, and a result page to show the prediction. It is designed for local development and easy GitHub upload.

## Features

- Home, contact, feedback, and detection pages
- Diabetes prediction from 8 medical inputs
- Saved ML model loaded from `savedModels/clf.joblib`
- Clean static HTML, CSS, and image assets

## Machine Learning Model

- Model type: `GradientBoostingClassifier`
- Saved with: `n_estimators=50`, `learning_rate=0.2`
- Notebook test accuracy: about `87.31%`

## How To Run

```powershell
cd "C:\Users\MOHAN\OneDrive\Desktop\Diabetic Detection\Django\DiabetesDetection"
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open:

http://127.0.0.1:8000/

## Notes

- `db.sqlite3` is generated locally and should stay ignored by Git.
- If you see a scikit-learn version warning, it is because the model was trained with 1.5.1 and the current environment uses 1.5.2.
