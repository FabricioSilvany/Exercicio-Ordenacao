"""
Dada uma lista de palavras, escreva um programa que receba uma lista de frutas e mostre:
- a lista original
- a lista ordenada
- a lista na ordem inversa

Caso o usuário digite sair, pare de solicitar dados

REFATORNADO CÓDIG:
Crie uma função para:
- Ordenação
- Ordenação na ordem inversa
"""

import os
os.system("cls || clear")

lista_frutas = []

def ordernar_lista(frutas):
    lista_ordenada = sorted(lista_frutas)
    return lista_ordenada, frutas

def ordem_inversa(frutas):
    lista_inversa = sorted(lista_frutas, reverse=True)
    return lista_inversa, frutas

print("===Solicitando dados===")
while True:
    frutas = input("Insira uma fruta: ")
    if frutas.lower() == "sair":
        break
    else:
        lista_frutas.append(frutas)

os.system("cls || clear")

print("===Exibindo dados===")
print("\nLista original:")
print(lista_frutas)

print("\nLista ordenada: ")
print(ordernar_lista(frutas))

print("\nLista Inversa: ")
print(ordem_inversa(frutas))