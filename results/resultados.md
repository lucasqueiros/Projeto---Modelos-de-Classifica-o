## Tabela que representa a acuracia de cada modelo e a configuração usada.


| Modelo | A. treino e teste | A. validação cruzada | Configuração |
|--------|-------------------|----------------------|--------------|
| Naive Bayes | 94.15% | 93.77% | previsores |
| SVM | 97.66% | 94.49% | previsores - SVC(kernel='linear', C=7, random_state=42) |
| Regressão logística | 96.49% | 94.54% | previsores - LogisticRegression(random_state=1, max_iter=500, penalty="l2", tol=0.0001, C=1,solver="lbfgs") |
| KNN | 94.15% | 93.77% | previsores |
| Árvore de decisão | 94.15% | 93.77% | previsores |
| Random Forest | 94.15% | 93.77% | previsores |
| XGBoost | 94.15% | 93.77% | previsores |
| LightGBM | 94.15% | 93.77% | previsores |
| CatBoost | 94.15% | 93.77% | previsores |

