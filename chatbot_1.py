from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Criando chatbot com mesmo banco de dados
bot = ChatBot(
    "JovemProgramador", 
    read_only=True, 
    logic_adapters=["chatterbot.logic.BestMatch"],
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri="sqlite:///database.sqlite3"  # Banco de dados compartilhado
)


trainer = ListTrainer(bot)

# Base de treinamento
conversas = [
    "oi", "Olá! Como posso te ajudar?",
    "olá", "Oi! Diga sua dúvida sobre o programa Jovem Programador.",
    "quem é você?", "Sou um chatbot feito para responder dúvidas sobre o programa Jovem Programador.",
    "o que é o jovem programador?", "É um programa de formação gratuito na área de tecnologia para jovens de Santa Catarina.",
    "o curso é online?", "Sim! As aulas são online e ao vivo.",
    "o curso é gratuito?", "Sim! O programa é 100% gratuito para os participantes.",
    "quais os requisitos?", "Ter entre 16 e 29 anos, ensino médio completo ou cursando, e morar em SC.",
    "qual a duração do curso?", "O curso tem duração de 9 meses.",
    "precisa ter experiência?", "Não precisa. Basta ter interesse na área de tecnologia.",
    "como faço para me inscrever?", "As inscrições são feitas pelo site jovemprogramador.com.br quando abertas.",
    "quem pode participar?", "Jovens entre 16 e 29 anos, moradores de SC, com ensino médio completo ou cursando.",
    "tem certificado?", "Sim, o curso oferece certificado ao final.",
]

# Treinando o bot
trainer.train(conversas)

print("Treinamento concluído! Execute app.py para testar.")
