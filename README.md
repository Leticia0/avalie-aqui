# avalie-aqui
Avalie Aqui - Projeto TCC

Passos para executar:
1. Clonar o repositório
2. No diretório do repositório, criar um ambiente virtual
      --> python3 -m venv venv
3. Acessar o ambiente virtual
      --> source venv/bin/activate
4. Configurar variável de ambiente
      --> no Linux: 
               - export FLASK_APP='main.py'
               - export FLASK_DEBUG=1
      --> no Windows: 
               - set FLASK_APP='main.py'
               - set FLASK_DEBUG=1
5. Instalar as dependências
       --> pip install -r requirements.txt
5. Executar a app
    --> flask run
