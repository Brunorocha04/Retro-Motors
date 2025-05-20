import csv
from your_app.models import Veiculo

with open('veiculos.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Veiculo.objects.create(
            nome=row['nome'],
            marca=row['marca'],
            modelo=row['modelo'],
            ano=int(row['ano']),
            km=int(row['km']),
            combustivel=row['combustivel'],
            descricao=row['descricao']
        )
