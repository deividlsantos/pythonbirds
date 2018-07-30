class  Pessoa:
    olhos = 2

    def __init__(self,*filhos,  nome=None, idade=24):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    print(Pessoa.metodo_estatico(), tatiane.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classes(), tatiane.nome_e_atributo_de_classes())