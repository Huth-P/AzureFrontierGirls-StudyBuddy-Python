# quiz_generator.py

import json
import random

# Base de Dados de Perguntas AZ-900 
# (Expandir esta lista ajudará na criatividade e na demonstração técnica!)
AZ900_QUESTIONS = {
    "custos": [
        {
            "id": 1,
            "question": "Qual é o termo para o modelo de despesa na nuvem onde os custos variam conforme o uso?",
            "options": ["A. CapEx", "B. OpEx", "C. TCO", "D. Fixed Costs"],
            "correct_answer": "B",
            "explanation": "OpEx (Operational Expenditure) é o modelo pay-as-you-go, onde se paga pelo consumo. CapEx (Capital Expenditure) é a compra de infraestrutura física.",
        }
    ],
    "segurança": [
        {
            "id": 2,
            "question": "O Azure Active Directory (Azure AD) é o principal serviço do Azure para qual dos seguintes?",
            "options": ["A. Armazenamento de Blobs", "B. Identidade e Acesso", "C. Máquinas Virtuais", "D. Redes Virtuais"],
            "correct_answer": "B",
            "explanation": "O Azure AD é a solução de Gerenciamento de Identidade e Acesso (IAM) da Microsoft, crucial para autenticação e autorização.",
        }
    ]
}

def get_quiz_question(topic: str):
    """
    Simula a busca de uma pergunta AZ-900.
    Em um cenário real, este seria um endpoint de API (ex: Azure Function).
    """
    topic = topic.lower().strip()
    
    # Se o tópico estiver na base, seleciona uma pergunta aleatória
    if topic in AZ900_QUESTIONS:
        question_list = AZ900_QUESTIONS[topic]
        # Retorna o JSON serializado (simulando a resposta da API)
        return json.dumps(random.choice(question_list))
    else:
        # Se não encontrar o tópico, retorna uma pergunta geral
        default_question = {
            "id": 99,
            "question": "Tópico não encontrado. Qual é o serviço principal de banco de dados SQL do Azure?",
            "options": ["A. Cosmos DB", "B. Azure SQL Database", "C. MySQL Flexible Server", "D. PostgreSQL Single Server"],
            "correct_answer": "B",
            "explanation": "O Azure SQL Database é o serviço PaaS do SQL Server nativo da Microsoft."
        }
        return json.dumps(default_question)

# Este bloco apenas para teste local, não é chamado pelo agente
if __name__ == '__main__':
    print(get_quiz_question("segurança"))
