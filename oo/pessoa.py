class  Pessoa:
    olhos = 2

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
    tatiane.sobrenome = 'Santos'
    del tatiane.filhos
    tatiane.olhos = 1
    del tatiane.olhos
    print(tatiane.__dict__)
    print(deivid.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(tatiane.olhos)
    print(deivid.olhos)
    print(id(Pessoa.olhos), id(tatiane.olhos), id(deivid.olhos))