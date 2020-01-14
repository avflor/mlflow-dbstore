from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='mlflow-dbstore',
    version='1.0.0',
    description='Plugin that provides DB Artifact Store functionality for MLflow',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Avrilia Floratou',
    author_email='avflor@microsoft.com',
    url="https://github.com/avflor/mlflow-dbstore",
    packages=find_packages(),
    install_requires=[
        'mlflow',
    ],
    entry_points={
        "mlflow.artifact_repository": [
            "mssql=dbstoreplugin.store.artifact:DBArtifactRepository"
        ]
    },
)
