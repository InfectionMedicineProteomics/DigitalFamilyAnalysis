# Digital Family Analysis

These are the analysis notebooks for the digital family manuscript

# Installation
Installation will only take a few minutes on a normal desktop computer.

1. Create a python virtual environment
2. Install all dependenceis in the pyproject.toml file to the created virtual environment

# Usage

Run each jupyter notebook in the order that it is numbered starting with 2_cluster_analysis. If the notebooks are run as-is, it may take a few hours to complete all analysis due to the comprehensive bootstrapping strategy that is used.

Please run all notebooks as-is to recreate the analysis included in the manuscript.

1. 2_cluster_analysis
* 0_cluster_determination.ipynb
* 1_cluster_analysis.ipynb

2. 3_clinical_digital_family
* 0_model_selection_analysis.ipynb
* 1_digital_family_network.ipynb
* 2_clinical_data_df_predictions.ipynb
* 3_clinical_data_df_metrics.ipynb

3. 4_high_risk_sepsis
* 0_sepsis_risk.ipynb
* 1_sepsis_risk_digital_family_trajectroy_finder.ipynb
* 2_sepsis_risk_df_metrics.ipynb
* 3_high_risk_sepsis_v_not_high.ipynb
* 4_importantance_figure.ipynb
* 5_sepsis_risk_method_comp.ipynb

4. 5_model_adaptability
* 0_external_validation_hero.ipynb
* 1_adaptive_database.ipynb
* 2_adaptive_df_metrics.ipynb

5. 6_infection_df
* 0_neighborhood_component_analysis_transform.ipynb
* 1_infection_df_metrics.ipynb

6. 7_vasopressors
* 0_vasopressors.ipynb
* 1_organ_dys_df_metrics.ipynb
* 2_organ_dys_weights.ipynb

Run all of these notebooks consecutively and you will reproduce the analysis and the figures for the manuscript