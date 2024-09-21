'''print("Qual a sua idade?")
idade = int(input())
 
if idade >= 18:
    print("Acesso Liberado! Boa Festa!")
else:
    print('Acesso negado! Você é menor de idade')'''


    #Código para liberar acesso somente para maiores de 18 anos

'''print('Qual a sua idade?')
idade = int(input())
if idade <18:
    print('Acesso Negado! Menor de idade')
elif idade ==18:
    print('Você está quase lá. Mais um ano e você terá acesso')
else:
    print('Acesso Liberado!')'''


'''print('Bimestre Escolar - Raquel Maciel') # título do código



print('Digite a nota do 1° bimestre')
B1 = float(input())  
print('Digite a nota do 2° bimestre')
B2 = float(input())  
print('Digite a nota do 3° bimestre')
B3 = float(input()) 
print('Digite a nota do 4° bimestre')
B4 = float(input())   
media = (B1 + B2 + B3 + B4) / 4
print('A média do aluno é ', media)

if media >=7:
    print('Parabéns. Aprovado!')

elif media >=5:
     print('Recuperação. Estude mais!!!')
    
else:
     print('Reprovado!!!')'''


'''#CÓDIGO PARA VERIFICAR SE PODE PARTICIPAR DO PROGRAMA MULHERES TECH

print('QUAL SEU GÊNERO ? (F OU M) ')
GENERO = input().upper()
print('Qual município você mora? ')
municipio = input().lower()

if GENERO == 'F' and municipio == 'rio de janeiro':
        print('Você pode participar do programa "Mulheres Tech".')
else:
        print('Você não está apta para participar do programa "Mulheres Tech"')'''


#CÓDIGO PARA PERMISSÃO DE ACESSO AO CINEMA. CRITÉRIO: +18 LIBERADO; -15 NEGADO; 16/17 APENAS COM RESPONSÁVEL
print("*"*30, 'Bem vindo ao cinema KINOPLEX' ,"*"*30 )
print(' ')

print('DIGITE SUA IDADE:')
idade = int(input())


if idade >=18:
    print('Acesso Liberado.\nBom filme!!!')

elif idade >15:
    print('Está acompanhado do respónsável?' )
    responsavel = input().upper()
    if responsavel == 'SIM':
        print('ACESSO LIBERADO)')
    else:
        print('ACESSO NEGADO)')
else:
    print('Acesso negado!')




