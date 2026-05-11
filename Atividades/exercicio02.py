nivel = float (input("Informe o nivel atual do reservatorio"))
if nivel >=90:
  status = "CRITICO: Risco de transbordamento"
elif nivel >=50:
  status = "ADEQUADO: Fluxo normal"
elif nivel >=20:
  status = "ATENÇÃO: Nivel baixo"
else:
  status = "PERIGO: Nivel minimo atingido!"

  print(f"Status do sistema: {status}")