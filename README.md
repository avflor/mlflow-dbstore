# SQL Server plugin for MLflow

This repository provides a MLflow plugin that allows users to use SQL Server as the artifact store for MLflow.


## Implementation overview
This repository contains one Python package:

`dbstoreplugin`: This package includes the `DBArtifactRepository` class that is used to read and write artifacts from SQL databases. This class sets the attribute `is_plugin = True` in order to indicate that the class is an MLflow artifact repository plugin. This package also includes the SQLAlchemy database models referenced by `DBArtifactRepository`. The package's `setup.py` file defines entrypoints that tell MLflow to automatically associate the `mssql` URIs with the `DBArtifactRepository` implementation when the `dbstoreplugin` library is installed. The entrypoints are configured as follows:

```
entry_points={
    "mlflow.artifact_repository": [
      "mssql=sqlplugin.store:DBArtifactRepository"
    ]
},
```

## User experience

The proposed plugin structure and development workflow provide the following experience to the end user:

Users can simply install MLflow with the SQL Server plugin via `pip install mlflow[sqlserver]` and then use MLflow as normal. The SQL Server artifact support will be provided automatically using the previously-described setup entrypoints mechanism.
