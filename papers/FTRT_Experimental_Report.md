# FTRT-3.0 Experimental Report

Generado automáticamente.

Fecha: 2026-07-24 01:38:08.565919

---

## EXP001_geometry_vs_sunspots

# EXP001 — Geometry vs Sunspots

## Objetivo

Evaluar si las métricas geométricas del sistema FTRT presentan
asociación estadística con el número diario de manchas solares
(SILSO).

## Variables geométricas

- lambda_max
- lambda_min
- energia_resonancia
- coherencia_espectral
- entropia_espectral
- estados_fase
- entropia_fase
- concentracion_fase

## Variable observacional

- Sunspot Number (SILSO)

## Metodología

1. Generar dataset FTRT.
2. Importar SILSO.
3. Unir por fecha.
4. Calcular Pearson.
5. Calcular Spearman.
6. Calcular correlación con desfases.
7. Generar tablas y figuras.

## Estado

Pendiente de ejecución.



---

## EXP002_lag_analysis

# EXP002 — Lag Correlation Analysis

## Objetivo

Evaluar la correlación entre las variables geométricas del FTRT y el
Sunspot Number (SILSO) considerando desfases temporales.

## Rango de análisis

-90 ... +90 días

## Variables

- lambda_max
- lambda_min
- energia_resonancia
- coherencia_espectral
- entropia_espectral
- estados_fase
- entropia_fase
- concentracion_fase

## Salidas

- Tabla de correlaciones
- Mejor desfase
- Correlación máxima
- Figuras

Estado: Pendiente.


---

## EXP003_significance

*Sin documentación.*

---

## EXP003_temporal_validation

*Sin documentación.*

---

## EXP004_montecarlo

*Sin documentación.*

---

## EXP005_prediction_validation

# EXP005 — Prediction Validation

## Objetivo

Evaluar si las variables geométricas FTRT permiten predecir
el número de manchas solares utilizando validación temporal.

## Metodología

1. Entrenamiento 2020-2024
2. Predicción 2025-2026
3. Correlación observada
4. Error MAE
5. Error RMSE
6. Coeficiente R²

## Estado

Pendiente.


---

## EXP006_lag_prediction

*Sin documentación.*

---

## EXP007_multivariable_prediction

# EXP007 — Multivariable Prediction

## Objetivo

Evaluar si la combinación de variables geométricas FTRT mejora la
predicción del número diario de manchas solares respecto al modelo base.

## Variables

- lambda_max
- energia_resonancia
- coherencia_espectral
- entropia_espectral
- estados_fase
- entropia_fase
- concentracion_fase

## Métricas

- Pearson (r)
- MAE
- RMSE
- R²

## Estado

Pendiente.


---

## EXP008_index_robustness

# EXP008 — FTRT Index Robustness

## Objetivo

Evaluar la robustez del FTRT Index v2.

## Pruebas

1. División temporal:
   - 2020-2022 entrenamiento
   - 2023-2026 validación

2. Métricas:
   - Pearson
   - Spearman
   - MAE
   - RMSE

3. Control:
   - Shuffle temporal
   - Bootstrap

## Entrada

results/csv/ftrt_index_v2.csv

## Salida

results/

Estado:
Pendiente de ejecución.


---

## EXP009_walk_forward

*Sin documentación.*

---

## EXP010_regimes

*Sin documentación.*

---

## EXP011_classification

*Sin documentación.*

---

## EXP013_baselines

*Sin documentación.*

---

## EXP015_hybrid_model

*Sin documentación.*

---

## EXP016_ablation

*Sin documentación.*

---

## EXP017_multivariate_regression

*Sin documentación.*

---

## EXP018_feature_significance

*Sin documentación.*

---

## EXP019_temporal_cv

*Sin documentación.*

---

## EXP020_bootstrap_coefficient

*Sin documentación.*

---

## EXP021_autocorrelation_control

*Sin documentación.*

---

## EXP022_block_permutation

*Sin documentación.*

---

## EXP023_cycle_validation

*Sin documentación.*

---

## EXP051_goes_classification

*Sin documentación.*

---

## EXP052_cme_association

*Sin documentación.*

---

## EXP053_bootstrap

*Sin documentación.*

---

## EXP054_permutation

*Sin documentación.*

---

## EXP055_roc_pr

*Sin documentación.*

---

## EXP056_walk_forward

*Sin documentación.*

---

## EXP057_probabilistic

*Sin documentación.*

---

## EXP058_operational_prediction

*Sin documentación.*

---

## EXP059_report

*Sin documentación.*

---

## EXP060_pipeline

*Sin documentación.*

---

## EXP061_join_expansion

*Sin documentación.*

---

## EXP062_auto_download

*Sin documentación.*

---

## EXP063_auto_update

*Sin documentación.*

---

## EXP064_master_catalog

*Sin documentación.*

---

## EXP065_global_statistics

*Sin documentación.*

---

## EXP066_active_regions

*Sin documentación.*

---

## EXP067_prediction_history

*Sin documentación.*

---

## EXP068_global_metrics

*Sin documentación.*

---

## EXP069_final_report

*Sin documentación.*

---

## EXP070_autonomous_lab

*Sin documentación.*

---

## EXP070_full_pipeline

*Sin documentación.*

---

## EXP071_null_model_validation

*Sin documentación.*

---

## EXP072_monte_carlo_null

*Sin documentación.*

---

## EXP073_threshold_sweep

*Sin documentación.*

---

## EXP074_lag_analysis

*Sin documentación.*

---

## EXP075_region_persistence

*Sin documentación.*

---

## EXP076_leave_region_out

*Sin documentación.*

---

## EXP077_region_contribution

*Sin documentación.*

---

## EXP078_region_temporal_memory

*Sin documentación.*

---

## EXP079_region_activity_correlation

*Sin documentación.*

---

## EXP080_composite_risk_index

*Sin documentación.*

---

## EXP081_risk_validation

*Sin documentación.*

---

## EXP082_risk_memory_model

*Sin documentación.*

---

## EXP083_precursor_window

*Sin documentación.*

---

## EXP084_precursor_persistence

*Sin documentación.*

---

## EXP085_active_region_control

*Sin documentación.*

---

## EXP086_rotation_memory

*Sin documentación.*

---

## EXP087_carrington_memory

*Sin documentación.*

---

## EXP088_solar_long_memory

*Sin documentación.*

---

## EXP089_solar_autocorrelation

*Sin documentación.*

---

## EXP090_cross_lag

*Sin documentación.*

---

## EXP091_ftrt_goes_crosslag

*Sin documentación.*

---

## EXP092_goes_energy_crosslag

*Sin documentación.*

---

## EXP093_cycle_phase_crosslag

*Sin documentación.*

---

## EXP094_rolling_correlation

*Sin documentación.*

---

## EXP095_lag_distribution

*Sin documentación.*

---

## EXP096_extended_crosslag

*Sin documentación.*

---

## EXP097_crosslag_180

*Sin documentación.*

---

## EXP098_lag_timeline

*Sin documentación.*

---

## EXP099_lag_persistence

*Sin documentación.*

---

## EXP100_lag_clusters

*Sin documentación.*

---

## EXP101_grand_conjunction

# EXP101 - Grand Conjunction Analysis

Objetivo
--------
Analizar si las Grandes Conjunciones Júpiter-Saturno
(~19.86 años) presentan cambios estadísticamente
significativos en:

- Índice FTRT
- Sunspot Number (SSN)
- GOES
- Energía GOES
- CME (si está disponible)

Periodo inicial:
1770-Actualidad

Ventanas previstas:

±180 días
±365 días
±730 días
±1825 días

Productos:

- grand_conjunctions.csv
- event_windows.csv
- statistics.csv
- summary.txt

Estado:
Preparación del experimento.


---

## EXP_AUDIT

*Sin documentación.*

---
