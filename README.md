# 🤗 Testando HuggingFace
No ambiente virtual, instalei as bibliotecas **torch, transformers e flask.** 
<br> Essas bibliotecas são essenciais para o funcionamento do agente:
- Torch é a biblioteca necessária para rodar modelos de aprendizado de máquina.
- Transformers é da Hugging Face, onde obtive os modelos pré-treinados, como o distilbert-base-cased-distilled-squad, que é utilizado para responder perguntas com base em um contexto.
- Flask seria uma dependência opcional para transformar o agente em uma API, mas por enquanto não foi necessário.
<br>
Logo em seguida, criei um arquivo Python que define um pipeline de perguntas e respostas (question-answering) usando o modelo distilbert-base-cased-distilled-squad. 
<br> Esse pipeline foi configurado para:

- Processar uma pergunta (pergunta): "Quando começou a Revolução Francesa?"
- Usar um contexto relacionado (contexto) para gerar uma resposta. O modelo foi capaz de identificar corretamente que a Revolução Francesa começou em 1789.


Com o ambiente virtual ativado e o script pronto, rodei o código usando o comando *python script.py* no PowerShell. O script executou o agente e retornou a resposta correta: 1789. :relaxed:

```
(venv) PS C:\Users\..\agente-ia> python script.py
Device set to use cpu
Resposta: 1789 e teve um grande impacto na Europa
(venv) PS C:\Users\..\agente-ia> deactivate
```

Esse processo criou a base de um agente de IA que pode ser expandido para diversas outras funções, como tradução, geração de texto, ou até mesmo uma API para responder perguntas de usuários em tempo real.

