#Parte 1 – Funções lambda (expressões matemáticas)
#1. Crie uma função lambda que calcule f(x) = x². Teste com x = 4.

potencia_quadrada = lambda x : x**2
potencia_quadrada(9)

#2. Crie uma função lambda que calcule f(x) = 5x - 3. Teste com x = 2.

formula = lambda x : 5*x - 3
formula(7)

#3. Crie uma função lambda que calcule f(x) = x² + 2x + 1. Teste com x = -1, 0, 1.

funcao = lambda x : x**2 + 2*x + 1
funcao(1)

#4. Crie uma função lambda que calcule f(x, y) = x^2 + 2xy + y^2. Teste com x = 2, y= 4.
#5. Crie uma função lambda que calcule f(x, y, z) = x^y+z. Teste com x = 3, y = 2, z=10.

#Parte 2 – Funções def
#6. Escreva uma função def lucro(receita, custo) que retorne o lucro da empresa: Lucro = Receita - Custo. Teste com receita = 10.000 e custo = 7.500.

def lucro(receita, custo):
    lucro = receita - custo
    return lucro

lucro(100, 50)
#7. Escreva uma função def margem_lucro(receita, custo) que calcule a margem de lucro percentual: Margem = (Lucro/Receita) * 100. Teste com receita = 20.000 e custo = 15.000.

def margem_lucro(receita, custo):
    lucro = receita - custo
    margem_lucro = lucro/receita
    return margem_lucro

margem_lucro(100, 25)

#8. Escreva uma função def ponto_equilibrio(custo_fixo, preco, custo_variavel) que calcule a quantidade mínima a ser vendida para não ter prejuízo: Qe = Custo Fixo / (Preço - Custo Variável). Teste com CF = 5.000, preço = 50, custo variável = 30.

def ponto_equilibrio(custo_fixo, preco, custo_variavel):
    quantidade = custo_fixo/(preco - custo_variavel)
    return quantidade

ponto_equilibrio(5000, 50, 30)

#9. Escreva uma função def folha(funcionarios) que receba uma lista de dicionários com nome e salário e retorne o total da folha salarial. Exemplo: [{'nome': 'Ana', 'salario': 3000}, {'nome': 'Carlos', 'salario': 4500}].
funcionarios = [{'nome': 'Ana', 'salario': 3000}, {'nome': 'Carlos', 'salario': 4500}]
def folha(funcionarios):
    soma_salario = 0
    for funcionario in funcionarios:
        soma_salario += funcionario['salario']
    return soma_salario
    
folha(funcionarios)

#10. Escreva uma função def juros_compostos(capital, taxa, tempo) que calcule o montante: M = C * (1+i)^t. Teste com C = 1.000, i = 0.02, t = 12.

def juros_compostos(capital, taxa, tempo):
    montante = capital*(1 + taxa)**tempo
    return montante

juros_compostos(1000, 0.02, 12)