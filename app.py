from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
import spacy

# Carregar o modelo de linguagem PT-BR explicitamente
spacy.cli.download("pt_core_news_sm")  # Certifique-se de que o modelo esteja instalado
nlp = spacy.load("pt_core_news_sm")  # Carregar o modelo em português para o SpaCy

app = Flask(__name__)

# Configurando o chatbot com banco de dados compartilhado
bot = ChatBot(
    "JovemProgramador", 
    read_only=True, 
    logic_adapters=["chatterbot.logic.BestMatch"],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"  # Banco de dados compartilhado
)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/perguntar", methods=["POST"])
def perguntar():
    pergunta = request.json.get("mensagem")
    resposta = bot.get_response(pergunta)
    
    # Se a resposta for igual à pergunta, forneça uma mensagem alternativa
    if str(resposta).strip().lower() == pergunta.strip().lower():
        resposta = "Desculpe, não entendi sua pergunta. Poderia reformular?"

    return jsonify({"resposta": str(resposta)})


if __name__ == "__main__":
    app.run(debug=True)
