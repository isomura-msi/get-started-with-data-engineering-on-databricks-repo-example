# Databricks notebook source
# MAGIC %run ../../Includes/_common
# MAGIC

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

print()
DA.clone_source_table("sales", f"{DA.paths.datasets}/ecommerce/delta", "sales_hist")
DA.clone_source_table("events", f"{DA.paths.datasets}/ecommerce/delta", "events_hist")
DA.clone_source_table("events_raw", f"{DA.paths.datasets}/ecommerce/delta")
DA.clone_source_table("item_lookup", f"{DA.paths.datasets}/ecommerce/delta")
  
DA.conclude_setup()
