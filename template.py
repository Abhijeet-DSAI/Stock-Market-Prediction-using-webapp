import os

def create_directory_structure(base_path="e:\END TO END PROJECTS\Radhya Software Solutions\Stock Market Prediction"):
    # Create base directory
    if not os.path.exists(base_path):
        os.makedirs(base_path)

    # List of sub-directories and files to be created
    paths = [
        "data/raw/SENSEX",
        "data/raw/BSE100",
        "data/processed",
        "data/interim",
        "models/SENSEX",
        "models/BSE100",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "src/utils",
        "src/automation",
        "webapp/frontend",
        "webapp/backend",
        "tests"
    ]

    # Create directories
    for path in paths:
        full_path = os.path.join(base_path, path)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

    # List of empty Python files to be created
    files = [
        "src/data/__init__.py",
        "src/data/data_collection.py",
        "src/data/data_preprocessing.py",
        "src/features/__init__.py",
        "src/features/feature_engineering.py",
        "src/models/__init__.py",
        "src/models/train_model.py",
        "src/models/predict_model.py",
        "src/visualization/__init__.py",
        "src/visualization/visualize.py",
        "src/utils/__init__.py",
        "src/automation/__init__.py",
        "webapp/frontend/__init__.py",
        "webapp/backend/__init__.py",
        "config.py",
        "main.py",
        "experiment.py"
    ]

   # Create files
    for file in files:
        full_path = os.path.join(base_path, file)
        if not os.path.exists(full_path):
            open(full_path, 'a').close()

if __name__ == "__main__":
    create_directory_structure()
