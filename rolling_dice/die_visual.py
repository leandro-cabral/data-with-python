import plotly.express as px
from die import Die

# Cria um D6
die = Die()

# Realiza alguns testes e armazena os resultados em uma lista
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analisa os resultados 
frequencies = []
poss_results = range(1, die.num_sides + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualiza os resultados
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()