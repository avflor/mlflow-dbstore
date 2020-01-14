from setuptools import setup

setup(
  name='dbstoreplugin',
  version='1.0.0',
  description='Plugin that provides DB Artifact Store functionality for MLflow',
  author='Avrilia Floratou',
  author_email='avflor@microsoft.com',
  packages=['dbstoreplugin'],
  install_requires=[
      'mlflow',
  ],
  entry_points={
      "mlflow.artifact_repository": [
        "mssql=dbstoreplugin.store.artifact:DBArtifactRepository"
      ]
  },
)
