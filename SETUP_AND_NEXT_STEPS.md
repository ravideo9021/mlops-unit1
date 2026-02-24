# mlops-unit1: Step-by-Step Work Log and Next Steps

Date: 2026-02-24
Project path: `/Users/ravidev9021/Desktop/mlops-unit1`

## What was done (step by step)

1. Created project folder and MLOps-friendly structure:
   - `data/`
   - `src/`
   - `models/`
   - `requirements.txt`
   - `README.md`

2. Created Python ML pipeline script:
   - File: `src/train.py`
   - Script does:
     - Creates `data/iris.csv` from sklearn Iris dataset if not present
     - Loads dataset using `pandas`
     - Prints basic dataset statistics
     - Splits data into train/test sets
     - Trains `LogisticRegression`
     - Prints accuracy + classification report
     - Saves model to `models/logistic_regression_iris.joblib` using `joblib`

3. Added dependency file:
   - File: `requirements.txt`
   - Packages:
     - `pandas==2.2.3`
     - `scikit-learn==1.6.1`
     - `joblib==1.4.2`

4. Added documentation:
   - File: `README.md`
   - Includes:
     - Project objective
     - Dataset info
     - Run steps
     - Environment recreation steps
     - GitHub push commands

5. Added Git tracking helpers:
   - `.gitignore` created (`.venv`, `__pycache__`, etc.)
   - `data/.gitkeep` and `models/.gitkeep` added

6. Initialized Git and made first commit on `main`:
   - Commit: `4f9b7a9`
   - Message: `Initialize mlops-unit1 with training pipeline`

7. Created feature branch and made a small change:
   - Branch: `experiment-v1`
   - Change in `src/train.py`: prints train/test sample counts
   - Commit: `e009be7`
   - Message: `Add train/test split size logging`

8. Merged branch back to `main`:
   - `experiment-v1` merged into `main` (fast-forward)

9. Reproducibility clone check performed:
   - Cloned repo into `/Users/ravidev9021/Desktop/mlops-unit1-clone-check`
   - Attempted install and run
   - Blocker: this environment cannot access PyPI (network/DNS restricted), so dependencies could not be installed and script could not run fully

---

## Current Git state

- Active branch: `main`
- Branches:
  - `main`
  - `experiment-v1`
- Commits:
  - `e009be7` Add train/test split size logging
  - `4f9b7a9` Initialize mlops-unit1 with training pipeline

---

## What you need to do next

1. Configure Git identity (if not set already):
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

2. Create a GitHub repository named `mlops-unit1` on GitHub.

3. Connect local repo to GitHub and push:
```bash
cd /Users/ravidev9021/Desktop/mlops-unit1
git remote add origin <YOUR_GITHUB_REPO_URL>
git branch -M main
git push -u origin main
git push -u origin experiment-v1
```

4. Verify project runs on a machine with internet access:
```bash
cd /Users/ravidev9021/Desktop/mlops-unit1
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train.py
```

5. Reproducibility check (required exercise):
```bash
cd /Users/ravidev9021/Desktop
git clone <YOUR_GITHUB_REPO_URL> mlops-unit1-clone-verify
cd mlops-unit1-clone-verify
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/train.py
```

6. Confirm expected outputs:
   - Console shows dataset stats
   - Console shows model accuracy/report
   - File exists: `models/logistic_regression_iris.joblib`

---

## Optional cleanup on your machine

If you want to remove the temporary verification clone created earlier:
```bash
rm -rf /Users/ravidev9021/Desktop/mlops-unit1-clone-check
```
(Only run this if you no longer need that folder.)
