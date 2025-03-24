# Databricks notebook source
# MAGIC %md
# MAGIC # Default notebook
# MAGIC
# MAGIC This default notebook is executed using Databricks Workflows as defined in resources/test_cicd_01.job.yml.

# COMMAND ----------

# MAGIC %load_ext autoreload
# MAGIC %autoreload 2

# COMMAND ----------

from test_cicd_01 import main

main.get_taxis(spark).show(10)