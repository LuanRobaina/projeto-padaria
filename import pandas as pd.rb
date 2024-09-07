import pandas as pd

# Supondo que os dados estão armazenados em um arquivo CSV na nuvem
data = pd.read_csv('s3://bucket-name/estoque.csv')

# Análise básica
print(data.describe())

# Gerar relatório de desperdício
desperdicio = data[data['weight'] < threshold]  # Defina um valor de threshold apropriado
print(f"Desperdício detectado: {len(desperdicio)} ocorrências")
