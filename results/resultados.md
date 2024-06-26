## Tabela que representa a acuracia de cada modelo e a configuração usada.


| Modelo | A. treino e teste | A. validação cruzada | Configuração |
|--------|-------------------|----------------------|--------------|
| Naive Bayes | 94.15% | 93.77% | previsores |
| SVM | 97.66% | 94.49% | previsores - SVC(kernel='linear', C=7, random_state=42) |
| Regressão logística | 96.49% | 94.54% | previsores - LogisticRegression(random_state=1, max_iter=500, penalty="l2", tol=0.0001, C=1,solver="lbfgs") |
| KNN | 97.08% | 92.00% | previsores KNeighborsClassifier(n_neighbors=7, metric='minkowski', p=1) |
| Árvore de decisão | 97.08% | 93.79% | previsores - DecisionTreeClassifier(criterion='entropy', random_state = 42, max_depth=3) |
| Random Forest | 97.08% | 94.00% | previsores - RandomForestClassifier(n_estimators=150, criterion='entropy', random_state=42, max_depth=4) |
| XGBoost | 97.08% | 97.23% | previsores - XGBClassifier(max_depth=2, learning_rate=0.05, n_estimators=250, objective='binary:logistic', random_state=3) |
| LightGBM | 96.49% | 95.99% | previsores - lgb.LGBMClassifier(num_leaves = 250, objective = 'binary', max_depth = 2, learning_rate = .05, max_bin =100) |
| CatBoost | 96.49% | 96.25% | previsores - CatBoostClassifier(task_type='CPU', iterations=100, learning_rate=0.1, depth = 8, random_state = 5,eval_metric="Accuracy") |

## Conclusão
Com base na tabela de acurácia dos modelos de classificação, podemos observar que o modelo que apresentou o melhor desempenho é o XGBoost. Ele obteve uma acurácia de 97.08% nos dados de treino e teste e uma acurácia de 97.23% na validação cruzada. Esse modelo superou todos os outros em termos de desempenho na validação cruzada, indicando sua maior capacidade de generalização e melhor desempenho global.

A configuração utilizada para o modelo XGBoost foi:

- max_depth=2
- learning_rate=0.05
- n_estimators=250
- objective='binary:logistic'
- random_state=3  
Essa combinação de hiperparâmetros permitiu ao XGBoost alcançar os melhores resultados entre os modelos avaliados.
