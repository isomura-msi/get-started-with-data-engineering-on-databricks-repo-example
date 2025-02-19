# Databricks notebook source
# MAGIC %run ../../Includes/_common
# MAGIC

# COMMAND ----------

# MAGIC %run ./Classroom-Setup-00-common

# COMMAND ----------

lesson_config = LessonConfig(name = None,
                             create_schema = True,
                             create_catalog = False,
                             requires_uc = False,
                             installing_datasets = True,
                             enable_streaming_support = False,
                             enable_ml_support = False)

DA = DBAcademyHelper(course_config=course_config, 
                     lesson_config=lesson_config)
DA.reset_lesson()
DA.init()

_setup_tables(create_raw=True)

DA.conclude_setup()
