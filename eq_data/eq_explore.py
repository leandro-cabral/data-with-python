import json
from pathlib import Path 

# Lê os dados como uma string e os converte em um objeto Python
path = Path('eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Cria uma versão mais legível do arquivo de dados
path = Path('readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)