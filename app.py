from flask import flask, jsonify, request

app = flask (__name__)

livros = [
    { 
        'id': 1,
        'titulo': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien',
     },
     {
        'id': 2,
        'titulo': 'O Senhor dos Anéis - As Duas Torres',
        'autor': 'J.R.R. Tolkien',
     },
     {
        'id': 3,
        'titulo': 'O Senhor dos Anéis - O Retorno do Rei',
        'autor': 'J.R.R. Tolkien',
     },
     {
        'id': 4,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling',
     },
     {
        'id': 5,
        'titulo': 'Harry Potter e a Câmara Secreta',
        'autor': 'J.K. Rowling',
     },
    {
            'id': 6,
            'titulo': 'Harry Potter e o Prisioneiro de Azkaban',
            'autor': 'J.K. Rowling',
    },
    {
            'id': 7,
            'titulo': 'Harry Potter e o Cálice de Fogo',
            'autor': 'J.K. Rowling',
    },
    {
            'id': 8,
            'titulo': 'Harry Potter e a Ordem da Fênix',
            'autor': 'J.K. Rowling',
    },
    {
            'id': 9,
            'titulo': 'Harry Potter e o Enigma do Príncipe',
            'autor': 'J.K. Rowling',
    },
    {
            'id': 10,
            'titulo': 'Harry Potter e as Relíquias da Morte',
            'autor': 'J.K. Rowling',
    },
    {
            'id': 11,
            'titulo': 'O Hobbit',
            'autor': 'J.R.R. Tolkien',
    },
    {
            'id': 12,
            'titulo': 'O Silmarillion',
            'autor': 'J.R.R. Tolkien',
    },
    {
            'id': 13,
            'titulo': 'O Mundo de Sofia',
            'autor': 'Jostein Gaarder',
    },
    {
            'id': 14,
            'titulo': 'A Menina que Roubava Livros',
            'autor': 'Markus Zusak',
    },
    {
            'id': 15,
            'titulo': 'O Caçador de Pipas',
            'autor': 'Khaled Hosseini',
    },
    {
            'id': 16,
            'titulo': 'A Culpa é das Estrelas',
            'autor': 'John Green',
    },
    {
            'id': 17,
            'titulo': 'O Alquimista',
            'autor': 'Paulo Coelho',
    },
    {
            'id': 18,
            'titulo': 'O Pequeno Príncipe',
            'autor': 'Antoine de Saint-Exupéry',
    },
    {
            'id': 19,
            'titulo': 'Dom Casmurro',
            'autor': 'Machado de Assis',
    },
    {
            'id': 20,
            'titulo': 'Memórias Póstumas de Brás Cubas',
            'autor': 'Machado de Assis',
    },
    {
            'id': 21,
            'titulo': 'O Guarani',
            'autor': 'José de Alencar',
    },
    {
            'id': 22,
            'titulo': 'Iracema',
            'autor': 'José de Alencar',
    },
    {
            'id': 23,
            'titulo': 'Senhora',
            'autor': 'José de Alencar',
    },
    {
            'id': 24,
            'titulo': 'A Moreninha',
            'autor': 'Joaquim Manuel de Macedo',
    },
    {
            'id': 25,
            'titulo': 'O Primo Basílio',
            'autor': 'José Maria de Eça de Queirós',
    },
    {
            'id': 26,
            'titulo': 'Os Maias',
            'autor': 'José Maria de Eça de Queirós',
    },
        {
            'id': 27,
            'titulo': 'A Ilustre Casa de Ramires',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 28,
            'titulo': 'O Guarani',
            'autor': 'José de Alencar',
        },
        {
            'id': 29,
            'titulo': 'Iracema',
            'autor': 'José de Alencar',
        },
        {
            'id': 30,
            'titulo': 'Senhora',
            'autor': 'José de Alencar',
        },
        {
            'id': 31,
            'titulo': 'A Moreninha',
            'autor': 'Joaquim Manuel de Macedo',
        },
        {
            'id': 32,
            'titulo': 'O Primo Basílio',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 33,
            'titulo': 'Os Maias',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 34,
            'titulo': 'A Ilustre Casa de Ramires',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 35,
            'titulo': 'O Guarani',
            'autor': 'José de Alencar',
        },
        {
            'id': 36,
            'titulo': 'Iracema',
            'autor': 'José de Alencar',
        },
        {
            'id': 37,
            'titulo': 'Senhora',
            'autor': 'José de Alencar',
        },
        {
            'id': 38,
            'titulo': 'A Moreninha',
            'autor': 'Joaquim Manuel de Macedo',
        },
        {
            'id': 39,
            'titulo': 'O Primo Basílio',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 40,
            'titulo': 'Os Maias',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 41,
            'titulo': 'A Ilustre Casa de Ramires',
            'autor': 'José Maria de Eça de Queirós',
        },
        {
            'id': 42,
            'titulo': 'O Guarani',
            'autor': 'José de Alencar',
        },
        {
            'id': 43,
            'titulo': 'Iracema',
            'autor': 'José de Alencar',
        },
        {
            'id': 44,
            'titulo': 'Senhora',
            'autor': 'José de Alencar',
        },
        {
            'id': 45,
            'titulo': 'O Poder da Esperança',
            'autor': 'Julian Melgosa & Michelson Borges',
        },
        {
            'id': 46,
            'titulo': 'Uma Vida com Propósitos',
            'autor': 'Rick Warren',
        },
        {
            'id': 47,
            'titulo': 'O Deus Pródigo',
            'autor': 'Timothy Keller',
        },
        {
            'id': 48,
            'titulo': 'Em Seus Passos o Que Faria Jesus?',
            'autor': 'Charles M. Sheldon',
        },
        {
            'id': 49,
            'titulo': 'A Cabana',
            'autor': 'William P. Young',
        },
        {
            'id': 50,
            'titulo': 'Mulheres da Bíblia',
            'autor': 'Ann Spangler & Jean E. Syswerda',
        },
        {
            'id': 51,
            'titulo': 'O Livro dos Salmos',
            'autor': 'Diversos Autores',
        },
        {
            'id': 52,
            'titulo': 'O Livro de Provérbios',
            'autor': 'Diversos Autores',
        },
        {
            'id': 53,
            'titulo': 'O Livro de Eclesiastes',
            'autor': 'Diversos Autores',
        },
        {
            'id': 54,
            'titulo': 'O Livro de Cantares de Salomão',
            'autor': 'Diversos Autores',
        },
        {
            'id': 55,
            'titulo': 'O Livro de Gênesis',
            'autor': 'Diversos Autores',
        },
        {
            'id': 56,
            'titulo': 'O Livro de Êxodo',
            'autor': 'Diversos Autores',
        },
        {
            'id': 57,
            'titulo': 'O Livro de Levítico',
            'autor': 'Diversos Autores',
        },
        {
            'id': 58,
            'titulo': 'O Livro de Números',
            'autor': 'Diversos Autores',
        },
        {
            'id': 59,
            'titulo': 'O Livro de Deuteronômio',
            'autor': 'Diversos Autores',
        },
        {
            'id': 60,
            'titulo': 'O Livro de Josué',
            'autor': 'Diversos Autores',
        },
        {
            'id': 61,
            'titulo': 'O Livro de Juízes',
            'autor': 'Diversos Autores',
        },
        {
            'id': 62,
            'titulo': 'O Livro de Rute',
            'autor': 'Diversos Autores',
        },
        {
            'id': 63,
            'titulo': 'O Livro de I Samuel',
            'autor': 'Diversos Autores',
        },
        {
            'id': 64,
            'titulo': 'O Livro de II Samuel',
            'autor': 'Diversos Autores',
        },
        {
            'id': 65,
            'titulo': 'O Livro de I Reis',
            'autor': 'Diversos Autores',
        },
        {
            'id': 66,
            'titulo': 'O Livro de II Reis',
            'autor': 'Diversos Autores',
        },
        {
            'id': 67,
            'titulo': 'O Livro de I Crônicas',
            'autor': 'Diversos Autores',
        },
        {
            'id': 68,
            'titulo': 'O Livro de II Crônicas',
            'autor': 'Diversos Autores',
        },
        {
            'id': 69,
            'titulo': 'O Livro de Esdras',
            'autor': 'Diversos Autores',
        },
        {
            'id': 70,
            'titulo': 'O Livro de Neemias',
            'autor': 'Diversos Autores',
        },
        {
            'id': 71,
            'titulo': 'O Livro de Ester',
            'autor': 'Diversos Autores',
        },
        {
            'id': 72,
            'titulo': 'O Iluminado',
            'autor': 'Stephen King',
        },
        {
            'id': 73,
            'titulo': 'Drácula',
            'autor': 'Bram Stoker',
        },
        {
            'id': 74,
            'titulo': 'Frankenstein',
            'autor': 'Mary Shelley',
        },
        {
            'id': 75,
            'titulo': 'It: A Coisa',
            'autor': 'Stephen King',
        },
        {
            'id': 76,
            'titulo': 'O Exorcista',
            'autor': 'William Peter Blatty',
        },
        {
            'id': 77,
            'titulo': 'Coraline',
            'autor': 'Neil Gaiman',
        },
        {
            'id': 78,
            'titulo': 'A Assombração da Casa da Colina',
            'autor': 'Shirley Jackson',
        },
        {
            'id': 79,
            'titulo': 'O Chamado de Cthulhu',
            'autor': 'H.P. Lovecraft',
        },
        {
            'id': 80,
            'titulo': 'Os Outros',
            'autor': 'Sarah Waters',
        },
        {
            'id': 81,
            'titulo': 'O Médico e o Monstro',
            'autor': 'Robert Louis Stevenson',
        },
        {
            'id': 82,
            'titulo': 'A Casa dos Espíritos',
            'autor': 'Isabel Allende',
        },
        {
            'id': 83,
            'titulo': 'Cem Anos de Solidão',
            'autor': 'Gabriel García Márquez',
        },
        {
            'id': 84,
            'titulo': 'O Amor nos Tempos do Cólera',
            'autor': 'Gabriel García Márquez',
        },
        {
            'id': 85,
            'titulo': 'A Casa dos Espíritos',
            'autor': 'Isabel Allende',
        },
        {
            'id': 86,
            'titulo': 'A Cidade do Sol',
            'autor': 'Khaled Hosseini',

        },
        {
            'id': 87,
            'titulo': 'O Caçador de Pipas',
            'autor': 'Khaled Hosseini',
        },
        {
            'id': 88,
            'titulo': 'A Menina que Roubava Livros',
            'autor': 'Markus Zusak',
        },
        {
            'id': 89,
            'titulo': 'O Livro das Sombras',
            'autor': 'Phyllis Curott',
        },
        {
            'id': 90,
            'titulo': 'A Bruxa de Portobello',
            'autor': 'Paulo Coelho',
        },
        {
            'id': 91,
            'titulo': 'O Alquimista',
            'autor': 'Paulo Coelho',
        },
        {
            'id': 92,
            'titulo': 'Veronika Decide Morrer',
            'autor': 'Paulo Coelho',
        },
        {
            'id': 93,
            'titulo': 'O Diário de Anne Frank',
            'autor': 'Anne Frank',
        },
        {
            'id': 94,
            'titulo': 'A Revolução dos Bichos',
            'autor': 'George Orwell',
        },
        {
            'id': 95,
            'titulo': '1984',
            'autor': 'George Orwell',
        },
        {
            'id': 96,
            'titulo': 'Admirável Mundo Novo',
            'autor': 'Aldous Huxley',
        },
        {
            'id': 97,
            'titulo': 'Fahrenheit 451',
            'autor': 'Ray Bradbury',
        },
        {
            'id': 98,
            'titulo': 'O Conto da Aia',
            'autor': 'Margaret Atwood',
        },
        {
            'id': 99,
            'titulo': 'A Estrada',
            'autor': 'Cormac McCarthy',
        },
        {
            'id': 100,
            'titulo': 'O Estrangeiro',
            'autor': 'Albert Camus',
        },
        {
            'id': 101,
            'titulo': 'A Metamorfose',
            'autor': 'Franz Kafka',
        },
        {
            'id': 102,
            'titulo': 'O Processo',
            'autor': 'Franz Kafka',
        },
        {
            'id': 103,
            'titulo': 'O Castelo',
            'autor': 'Franz Kafka',
        },
        {
            'id': 104,
            'titulo': 'A Peste',
            'autor': 'Albert Camus',
        },
        {
            'id': 105,
            'titulo': 'O Mito de Sísifo',
            'autor': 'Albert Camus',
        },
        {
            'id': 106,
            'titulo': 'A Queda',
            'autor': 'Albert Camus',
        },
        {
            'id': 107,
            'titulo': 'O Estrangeiro',
            'autor': 'Albert Camus',
        },
        {
            'id': 108,
            'titulo': 'A Metamorfose',
            'autor': 'Franz Kafka',
        },
        {
            'id': 109,
            'titulo': 'O Processo',
            'autor': 'Franz Kafka',
        },
        {
            'id': 110,
            'titulo': 'O Castelo',
            'autor': 'Franz Kafka',
        },
        {
            'id': 111,
            'titulo': 'A Peste',
            'autor': 'Albert Camus',
        },
        {
            'id': 112,
            'titulo': 'O Mito de Sísifo',
            'autor': 'Albert Camus',
        },
        {
            'id': 113,
            'titulo': 'A Queda',
            'autor': 'Albert Camus',
        },
        {
            'id': 114,
            'titulo': 'O Estrangeiro',
            'autor': 'Albert Camus',
        },
        {
            'id': 115,
            'titulo': 'A Metamorfose',
            'autor': 'Franz Kafka',
        },
        {
            'id': 116,
            'titulo': 'O Processo',
            'autor': 'Franz Kafka',
        },
        {
            'id': 117,
            'titulo': 'O Castelo',
            'autor': 'Franz Kafka',
        },
        {
            'id': 118,
            'titulo': 'O Código Da Vinci',
            'autor': 'Dan Brown',
        },
        {
            'id': 119,
            'titulo': 'O Pequeno Príncipe',
            'autor': 'Antoine de Saint-Exupéry',
        },
        {
            'id': 120,
            'titulo': 'O Apanhador no Campo de Centeio',
            'autor': 'J.D. Salinger',
        },
        {
            'id': 121,
            'titulo': 'O Senhor dos Anéis',
            'autor': 'J.R.R. Tolkien',
        },
        {
            'id': 122,
            'titulo': 'O Alquimista',
            'autor': 'Paulo Coelho',
        },
        {
            'id': 123,
            'titulo': 'Harry Potter e a Pedra Filosofal',
            'autor': 'J.K. Rowling',
        },
        {
            'id': 124,
            'titulo': 'O Hobbit',
            'autor': 'J.R.R. Tolkien',
        },
        {
            'id': 125,
            'titulo': 'O Diário de Anne Frank',
            'autor': 'Anne Frank',
        },
        {
            'id': 126,
            'titulo': 'O Menino do Pijama Listrado',
            'autor': 'John Boyne',
        },
        {
            'id': 127,
            'titulo': 'A Menina que Roubava Livros',
            'autor': 'Markus Zusak',
        },
        {
            'id': 128,
            'titulo': 'O Caçador de Pipas',
            'autor': 'Khaled Hosseini',
        },
]
        # Consultar(todos)
@app.route('/livros',methods=['GET']) 
def obter_livros():
    return jsonify(livros)


       

        # Consultar (livro específico)
@app.route('/livros/<int:id>',methods=['GET'])        
def obter_livro_por_id(id):
     for livro in livro:
        if livro.get('id') == id:
            return jsonify(livro)
     
        # Editar
        # Deletar
        # Criar

app.run(port=5000,host='localhost',debug=True) 



        





