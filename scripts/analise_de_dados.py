import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leitura do dataset (substitua 'caminho_do_arquivo.csv' pelo caminho real do seu arquivo)
df = pd.read_csv('caminho_do_arquivo.csv')

# Inspeção inicial do dataset
print("Informações do DataFrame:")
print(df.info())

print("\nPrimeiras 5 linhas do DataFrame:")
print(df.head())

# Estatísticas descritivas
print("\nEstatísticas Descritivas:")
print(df.describe())

# Verificação de valores ausentes
print("\nValores Ausentes:")
print(df.isnull().sum())

# Visualização de valores ausentes
plt.figure(figsize=(12, 8))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Mapa de Valores Ausentes')
plt.show()

# Distribuição de variáveis numéricas
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numerical_cols].hist(figsize=(15, 10), bins=20)
plt.suptitle('Distribuição de Variáveis Numéricas')
plt.show()

# Boxplots para variáveis numéricas
plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(4, 8, i+1)
    sns.boxplot(y=df[col])
    plt.title(col)
plt.tight_layout()
plt.show()

# Gráficos de barras para variáveis categóricas
categorical_cols = df.select_dtypes(include=['object', 'category']).columns
plt.figure(figsize=(15, 10))
for i, col in enumerate(categorical_cols):
    plt.subplot(4, 8, i+1)
    df[col].value_counts().plot(kind='bar')
    plt.title(col)
plt.tight_layout()
plt.show()

# Matriz de correlação para variáveis numéricas
plt.figure(figsize=(12, 10))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Matriz de Correlação')
plt.show()

# Scatter plot matrix (pair plot) para as primeiras 5 variáveis numéricas
sns.pairplot(df[numerical_cols[:5]])
plt.suptitle('Pair Plot das Primeiras 5 Variáveis Numéricas')
plt.show()
