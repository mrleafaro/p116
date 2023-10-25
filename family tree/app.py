# importando os módulos da biblioteca flask
from flask import Flask, render_template

# criando a instância da classe Flask, fornecendo a palavra-chave __name__ como argumento
app = Flask(__name__)

# escreva as rotas usando funções de decorador
# rota padrão ou 'URL'
@app.route("/")
def home():
    nome = "Asa Noturna"  # escreva seu nome
    idade = "15"  # escreva sua idade
    return render_template('index.html', nome=nome, idade=idade)

# defina a rota para a página do pai
@app.route("/pai")
def pai():
    nome_pai = "Batman"  # Substitua pelo nome do seu pai
    idade_pai = "35"  # Substitua pela idade do seu pai
    return render_template('pai.html', nome_pai=nome_pai, idade_pai=idade_pai)

# defina a rota para a página da mãe
@app.route("/mae")
def mae():
    nome_mae = "Batgirl"  # Substitua pelo nome da sua mãe
    idade_mae = "35"  # Substitua pela idade da sua mãe
    return render_template('mae.html', nome_mae=nome_mae, idade_mae=idade_mae)

# defina a rota para a página do amigo
@app.route("/amigo")
def amigo():
    nome_amigo = "Robin"  # Substitua pelo nome do seu amigo
    idade_amigo = "15"  # Substitua pela idade do seu amigo
    return render_template('amigo.html', nome_amigo=nome_amigo, idade_amigo=idade_amigo)

# Exemplo de outra rota
@app.route("/outra-rota")
def outra_rota():
    # Implemente o que você desejar nesta rota
    return "Esta é outra rota de exemplo."

# execute o arquivo
if __name__ == '__main__':
    app.run(debug=True)
