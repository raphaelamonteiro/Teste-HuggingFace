from transformers import pipeline

# Criando um agente de IA simples para responder perguntas
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Pergunta de teste
contexto = "A Revolução Francesa começou em 1789 e teve um grande impacto na Europa."
pergunta = "Quando começou a Revolução Francesa?"

# Rodando o modelo
resposta = qa_pipeline(question=pergunta, context=contexto)

# Exibindo a resposta
print("Resposta:", resposta["answer"])
