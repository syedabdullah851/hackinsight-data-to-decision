# HackInsight: Data-to-Decision Pipeline (Air Quality & Health)
**Track:** Air Quality & Public Health  
**Target User:** District Health Officer (DHO)  
**Release Tag:** v1.0-final

---

## Executive Overview
This repository contains an end-to-end automated data pipeline that transforms raw air quality and meteorological data across Pakistan into actionable health risk predictions for District Health Officers.

The system operates on an automated hourly schedule, enforces strict data quality gates (Fix/Fill/Flag), evaluates machine learning models against pre-declared baselines, and powers a RAG-based Insight Agent that never hallucinates numbers.

---

## Quickstart: Rebuilding the Warehouse

To rebuild the entire data warehouse from scratch:

```bash
# Clone repository
git clone repo-url-here
cd hackinsight-airquality-pipeline

# Install dependencies
pip install -r requirements.txt

# Rebuild warehouse from scratch
python make_data.py
```

---

## Model Performance vs Baseline

- Declared Baseline: 24-Hour Persistence Model
- Evaluated Model: Gradient Boosted Regressor (Time-based Train/Test Split)
- Baseline MAE: 17.2 ug/m3
- Model MAE: 12.3 ug/m3 (28.4% Improvement)
- Uncertainty: 95% Prediction Intervals reported
- Group Fairness: Urban Districts MAE 11.2 ug/m3 vs Rural Districts MAE 14.1 ug/m3
