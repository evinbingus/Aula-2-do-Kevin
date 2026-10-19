materiais = {
 "mouse": 10,
 "teclado": 6,
 "cabo": 20
}
nome = input("Qual material deseja retirar? ").lower()
try:
 quantidade = int(input("Quantas unidades? "))
except ValueError:
 print("Digite uma quantidade numérica válida!")