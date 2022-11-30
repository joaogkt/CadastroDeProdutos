#Funções

def CriarArquvivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do aquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!!')


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def escrever(arq, codigo=0, descricao='desconhecido', preco=0, categoria='Outros'):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{codigo};{descricao};{preco};{categoria}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print('Registro do produto adiconado')
        finally:
            a.close()
