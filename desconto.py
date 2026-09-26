#-----------------------------------------------------------------------------
# ENTRADA DE DADOS
#-----------------------------------------------------------------------------
# O QUE FIZ: Criei uma variável "valor_compra"na qual posso atribuir qualquer valor, o termo float permite que esse valor seja decimal e o input determina o prompt de entrada
#-----------------------------------------------------------------------------

valor_compra = float(input("Digite o valor total da compra: R$ "))

#-----------------------------------------------------------------------------
# CONDICAO
#-----------------------------------------------------------------------------
# O QUE FIZ: Aqui foi criada a condicao do desconto através do valor inserido no programa
#-----------------------------------------------------------------------------

if valor_compra < 200:
    percentual_desconto = 0.05
elif valor_compra < 300:
    percentual_desconto = 0.10
else:
    percentual_desconto = 0.15

#-----------------------------------------------------------------------------
# OPERACOES DE DESCONTO
#-----------------------------------------------------------------------------
# O QUE FIZ: Essas sao as contas pra determinar o valor descontado e o valor final
#-----------------------------------------------------------------------------


valor_desconto = valor_compra * percentual_desconto
valor_final = valor_compra - valor_desconto


#-----------------------------------------------------------------------------
# EXIBICAO DE RESULTADOS
#-----------------------------------------------------------------------------
# O QUE FIZ:Com o print eu consigo mostrar na tela os resultados no final
#-----------------------------------------------------------------------------


print(f"\nValor da compra: R$ {valor_compra:.2f}")
print(f"Percentual de desconto aplicado: {percentual_desconto * 100:.0f}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor total a pagar: R$ {valor_final:.2f}")


#-----------------------------------------------------------------------------
