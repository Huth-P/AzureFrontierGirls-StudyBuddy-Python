# app.py: Servidor Flask para a API do AZ-900 Study Buddy

from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Base de Dados de Perguntas AZ-900 (Entrega Técnica)
AZ900_QUESTIONS = {
    "custos": [
        {
            "id": 1,
            "question": "Qual é o termo para o modelo de despesa na nuvem onde os custos variam conforme o uso?",
            "options": "A. CapEx, B. OpEx, C. TCO, D. Fixed Costs",
            "correct_answer": "B",
            "explanation": "OpEx (Operational Expenditure) é o modelo pay-as-you-go, onde se paga pelo consumo. CapEx é a compra de infraestrutura física.",
        }
    ],
    "segurança": [
        {
            "id": 2,
            "question": "O Azure Active Directory (Azure AD) é o principal serviço do Azure para qual dos seguintes?",
            "options": "A. Armazenamento de Blobs, B. Identidade e Acesso, C. Máquinas Virtuais, D. Redes Virtuais",
            "correct_answer": "B",
            "explanation": "O Azure AD é a solução de Gerenciamento de Identidade e Acesso (IAM) da Microsoft.",
        }
    ],
    "serviços": [
        {
            "id": 3,
            "question": "Qual serviço do Azure é usado para hospedar um site web de forma simples (PaaS)?",
            "options": "A. Azure Virtual Machines, B. Azure App Service, C. Azure Container Instances, D. Azure Kubernetes Service",
            "correct_answer": "B",
            "explanation": "O Azure App Service é a solução PaaS (Platform as a Service) para hospedagem web.",
        }
    ]
}

# app.py: Adicione esta nova base de dados de definições
# (Cole logo após a base AZ900_QUESTIONS)

AZ900_DEFINITIONS = {
    "rbac": "Role-Based Access Control (RBAC) é um sistema que permite gerenciar quem tem acesso aos recursos do Azure e o que eles podem fazer com eles.",
    "region": "Uma Região do Azure é um conjunto de data centers implantados dentro de um perímetro definido por latência e conectados por uma rede regional dedicada.",
    "availability set": "Um Availability Set é um agrupamento lógico de VMs que garante que elas rodem em hardware tolerante a falhas e isolado em diferentes racks dentro de um datacenter."
}

def get_definition(term: str):
    """Retorna a definição de um termo do AZ-900."""
    term = term.lower().strip()
    return AZ900_DEFINITIONS.get(term, "Desculpe, não encontrei a definição exata para este termo AZ-900.")


# CÓDIGO para o NOVO ENDPOINT (Cole logo após o endpoint @app.route('/quiz',...))

@app.route('/define', methods=['GET'])
def define_endpoint():
    # Pega o parâmetro 'term' da URL que o Agente envia
    term = request.args.get('term', '')
    
    # Chama a função que retorna a definição
    definition = get_definition(term)
    
    # Retorna o JSON com a definição
    return jsonify({"definition": definition})

def get_quiz_question(topic: str):
    """Retorna uma pergunta do quiz com base no tópico."""
    topic = topic.lower().strip()
    
    if topic in AZ900_QUESTIONS:
        # Retorna uma pergunta aleatória sobre o tópico
        return random.choice(AZ900_QUESTIONS[topic])
    else:
        # Retorna uma pergunta geral ou mensagem de erro
        default_question = {
            "id": 99,
            "question": "Desculpe, esse tópico não está na base. Por favor, tente 'custos', 'segurança' ou 'serviços'.",
            "options": "A. Cosmos DB, B. Azure SQL Database, C. MySQL, D. PostgreSQL",
            "correct_answer": "N/A",
            "explanation": "O Agente foi programado para focar em tópicos específicos do AZ-900."
        }
        return default_question


# Definição do Endpoint da API (corresponde ao quiz_api.json)
@app.route('/quiz', methods=['GET'])
def quiz_endpoint():
    # Pega o parâmetro 'topic' enviado pelo Azure AI Agent na URL
    topic = request.args.get('topic', 'geral')
    
    # Chama a função que gera o quiz
    question_data = get_quiz_question(topic)
    
    # Retorna o resultado como um JSON que o Agente vai interpretar
    return jsonify(question_data)

if __name__ == '__main__':
    # Roda o servidor na porta 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
