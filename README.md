# mlops-unit1

## Project Objective
This project demonstrates a simple end-to-end ML workflow with Git-based development practices:
- load a dataset with pandas
- print basic statistics
- split data into training/testing sets
- train a simple model
- evaluate model performance
- save the trained model

## Dataset Used
- **Iris dataset** from `sklearn.datasets`
- The script creates `data/iris.csv` locally (if missing) and then loads it using pandas.

## Project Structure
```text
mlops-unit1/
├── data/
├── src/
├── models/
├── requirements.txt
└── README.md
```

## Steps to Run the Project
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies.
4. Run the training script.

```bash
git clone <your-repo-url>
cd mlops-unit1
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train.py
```

## Recreate the Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Model Artifact
After running the script, the trained model is saved to:
- `models/logistic_regression_iris.joblib`

## Push to GitHub
```bash
git remote add origin <your-github-repo-url>
git branch -M main
git push -u origin main
```
