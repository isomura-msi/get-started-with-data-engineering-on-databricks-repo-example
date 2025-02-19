# Databricks notebook source
# MAGIC %run ./Classroom-Setup-05.1-Common
# MAGIC

# COMMAND ----------

lesson_config = LessonConfig(name = lesson_name,
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

DA.paths.storage_location = f"{DA.paths.working_dir}/storage_location"
DA.dlt_data_factory = DataFactory()

DA.conclude_setup()
