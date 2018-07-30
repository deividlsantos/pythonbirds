class  Pessoa:
    def __init__(self,*filhos,  nome=None, idade=24):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    deivid = Pessoa(nome='Deivid')
    tatiane = Pessoa(deivid, nome='Tatiane')
    print(Pessoa.cumprimentar(tatiane))
    print(id(tatiane))
    print(tatiane.cumprimentar())
    print(tatiane.nome)
    print(tatiane.idade)
    for filho in tatiane.filhos:
        print(filho.nome)