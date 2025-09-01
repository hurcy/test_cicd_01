import os
from pathlib import Path
from pyspark.dbutils import DBUtils
from pyspark.sql import SparkSession


class PathResolver:
    _instance = None
    _bundle_name = "test_cicd_01"  # change to bundle name

    def __new__(cls):
        """
        Singleton pattern implementation for PathResolver class
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._root = Path(__file__).parent.parent.parent
        return cls._instance

    def _get_system_root(self):
        """
        Method to get the system root directory from the notebook path
        """
        spark = SparkSession.builder.getOrCreate()
        dbutils = DBUtils(spark)
        notebook_path = (
            dbutils.notebook.entry_point.getDbutils()
            .notebook()
            .getContext()
            .notebookPath()
            .get()
        )
        system_root = "/Workspace" + os.path.dirname(notebook_path).replace(
            f"{self._bundle_name}/src", f"{self._bundle_name}/resources"
        )
        return system_root

    @property
    def resources(self):
        """
        Define properties to resolve paths for resources, config, and tests directories
        """

        return self._root / "resources"

    @property
    def config(self):
        """
        Property to resolve the path for the config directory
        """
        return self._root / self._get_system_root() / "config"

    @property
    def tests(self):
        """
        Property to resolve the path for the tests directory
        """
        return self._root / "tests"
