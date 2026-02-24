from pathlib import Path

import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def ensure_dataset(csv_path: Path) -> None:
    """Create a local CSV copy of Iris dataset if it does not exist."""
    if csv_path.exists():
        return

    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    df.rename(columns={"target": "species"}, inplace=True)
    csv_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(csv_path, index=False)


def print_basic_statistics(df: pd.DataFrame) -> None:
    print("Dataset shape:", df.shape)
    print("\nColumn names:")
    print(df.columns.tolist())
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("\nBasic statistics:")
    print(df.describe(include="all"))


def train_and_evaluate(df: pd.DataFrame, model_path: Path) -> None:
    X = df.drop(columns=["species"])
    y = df["species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )
    print(f"\nTrain size: {len(X_train)} | Test size: {len(X_test)}")

    model = LogisticRegression(max_iter=300)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("\nModel evaluation:")
    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved to: {model_path}")


def main() -> None:
    project_root = Path(__file__).resolve().parent.parent
    data_path = project_root / "data" / "iris.csv"
    model_path = project_root / "models" / "logistic_regression_iris.joblib"

    ensure_dataset(data_path)

    # Requirement asks to load dataset using pandas.
    df = pd.read_csv(data_path)
    print_basic_statistics(df)
    train_and_evaluate(df, model_path)


if __name__ == "__main__":
    main()
