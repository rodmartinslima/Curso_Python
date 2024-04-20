notas = [55, 63, 80, 33, 77]
status = []
status = ('Aprovado' if nota >= 60 else 'Reprovado' for nota in notas )

for stat in status:
  print(stat)

