# 📄 GUIA DE IMPLEMENTAÇÃO: Criação do Agente "AZ-900 StudyBuddy" no Azure AI Foundry

Este guia detalha o processo "clique a clique" para a criação do recurso **Azure AI Foundry** (Hub) e o projeto inicial (`StudyBuddy`), que é a base para o Agente AZ-900 Study Buddy.


# Passo 1: Criação do Azure AI Foundry resource

## Etapa 1: Básico ([Basics](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/1-Create%20an%20Azure%20AI%20Foundry%20resource%20-%20Microsoft%20Azure_1_Basics.pdf))

Esta etapa define a localização e a nomenclatura dos recursos.


| Campo | Seleção | Detalhe | Fonte/Print |
| :--- | :--- | :--- | :--- |
| **Subscription** (Assinatura) | **Azure for Students** | Utiliza a assinatura de estudante. | [1](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/8-Create%20an%20Azure%20AI%20Foundry%20resource8%20-%20Microsoft%20Azure_6_Review%2Bsubmit_Created.pdf) |
| **Resource group** (Grupo de Recursos) | **RG-AZFG-Challenge** | O grupo de recursos existente | [1](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/8-Create%20an%20Azure%20AI%20Foundry%20resource8%20-%20Microsoft%20Azure_6_Review%2Bsubmit_Created.pdf) |
| **Name** (Nome do AI Hub) | **Pamela-Huth-Azure-Frontier-Girls-hub** | Nome do recurso principal | [1](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/8-Create%20an%20Azure%20AI%20Foundry%20resource8%20-%20Microsoft%20Azure_6_Review%2Bsubmit_Created.pdf) |
| **Region** (Região) | **Sweden Central** | Região selecionada após falha na implantação em West Europe e East US |  [1](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/1-Create%20an%20Azure%20AI%20Foundry%20resource%20-%20Microsoft%20Azure_1_Basics.pdf), [2](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/6-Create%20an%20Azure%20AI%20Foundry%20resource6%20-%20Microsoft%20Azure_6_Review%2BSubmit_Validation_failed.pdf), [3](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/7-Create%20an%20Azure%20AI%20Foundry%20resource7%20-%20Microsoft%20Azure_1_Basics_Changed%20region%20SwedenCentral.pdf)  |
| **Default project name** (Nome do Projeto Padrão) | **StudyBuddy** | Nome do projeto padrão que o Agente utilizará | [1](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/8-Create%20an%20Azure%20AI%20Foundry%20resource8%20-%20Microsoft%20Azure_6_Review%2Bsubmit_Created.pdf) |

## Etapa 2: Rede ([Network](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/2-Create%20an%20Azure%20AI%20Foundry%20resource2%20-%20Microsoft%20Azure_2_Network.pdf))

Esta etapa define as regras de acesso de entrada (Inbound Access).

* **Inbound Access** (Acesso de Entrada): Foi selecionada a opção mais permissiva: **"All networks, including the internet, can access this resource"** (Todas as redes, incluindo a internet, podem acessar este recurso).
* **Observação:** Esta configuração foi mantida, pois as APIs de Agentes só suportam injeção de rede para *Standard Agent set-up*, o que não é o foco do desafio.

## Etapa 3: Identidade ([Identity](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/3-Create%20an%20Azure%20AI%20Foundry%20resource3%20-%20Microsoft%20Azure_3_Identity.pdf))

Esta etapa define como o recurso se autentica em outros serviços do Azure (Managed Identity).

*  **Identity type** (Tipo de Identidade): Foi selecionada a opção **"System assigned"** (Atribuída ao sistema).
*  **Justificativa:** Esta é a opção mais simples, onde o ciclo de vida da identidade é gerenciado pelo próprio Azure e está vinculado ao recurso AI Foundry.

## Etapa 4: Criptografia ([Encryption](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/4-Create%20an%20Azure%20AI%20Foundry%20resource4%20-%20Microsoft%20Azure_4_Encryption.pdf))

Esta etapa define como os dados são criptografados no recurso.

* **Data Encryption** (Criptografia de Dados): A opção padrão **"Microsoft-managed keys"** foi mantida.
* **Alternativa Descartada:** Foi descartada a opção **"Encrypt data using a customer-managed key"** (CMK) para evitar a complexidade desnecessária de configurar um Azure Key Vault.

## Etapa 5: [Tags](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/5-Create%20an%20Azure%20AI%20Foundry%20resource5%20-%20Microsoft%20Azure_5_Tags.pdf)

* **Tags:** Não foram adicionadas Tags, pois não era um requisito obrigatório do desafio.

## Etapa 6: Revisar + Enviar ([Review + Submit](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/8-Create%20an%20Azure%20AI%20Foundry%20resource8%20-%20Microsoft%20Azure_6_Review%2Bsubmit_Created.pdf))

* **Revisão:** Foi realizada uma verificação final dos detalhes da implantação.
* **Implantação:** O botão **"Create"** (Criar) foi acionado.

---

## [Resultado](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/9-Index_Deployment%20details%20after%20resource%20creation.pdf) da Implantação

* **Status:** A implantação foi concluída com sucesso.
* **Nome da Implantação:** `AlFoundryCreate-20251117221706`.
* **Recursos Criados:** `Pamela-Huth-Azure-Frontier-Girls-hub` (Hub) e `Pamela-Huth-Azure-Frontier-Girls-hub/StudyBuddy` (Projeto/Agente).
* **Localização Final:** A localização final do recurso é **swedencentral**.
* **Próximo Passo:** O Agente `StudyBuddy` foi acessado para a configuração do *System Prompt* e das *Actions* (Tools).

---

# Passo 2: [Criação](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/10-Pamela-Huth-Azure-Frontier-Girls-hub%20-%20Microsoft%20Azure.pdf) do Agente

## Etapa 7: Configuração do Agente AZ-900 Study Buddy

O Agente foi criado e configurado para ter uma personalidade específica e um foco estrito no AZ-900.

A. Acesso e Status Inicial

* Após a conclusão da implantação, o Agente AZ-900 Study Buddy aparece na [lista de agentes](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/12-success%20agent%20created.png).


B. Definição da Personalidade e Escopo

* O Agente foi editado (tela "Setup") para definir seu propósito e regras: [1](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/13-Create%20and%20debug%20your%20agents_Setup.png), [2](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/14-Create%20and%20debug%20your%20agents_Setup2.png)

    
Descrição: Assistente de quiz e treinamento para a certificação AZ-900.

* [Instruções](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/13-Create%20and%20debug%20your%20agents_Setup.png) (System Prompt): Definindo que sua regra principal é usar a Tool quiz_generator e manter o foco estrito no AZ-900.

---

## Etapa 8: Implementação da Ação Funcional (Tool)

O Agente requer uma Tool para cumprir sua função. Foi escolhido o tipo OpenAPI 3.0 specified tool para integrar o código Python real (rodando no Codespace).


A. Seleção do Tipo de Ação

* Na tela de configuração do Agente (Setup), foi clicado em "[+ Add](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/14-Create%20and%20debug%20your%20agents_Setup2.png)" ao lado de "Actions".

* Foi selecionado "[OpenAPI 3.0 specified tool](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/15-add%20action.png)".

B. Criação da Custom Tool

* Detalhes da Tool: Foi inserido o nome [AZ900QuizService](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/16-create%20a%20custom%20tool.png) e uma descrição.

* Define [Schema](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/17-create%20a%20custom%20tool_Jason%20with%20Python%20URL.png): Nesta etapa, o contrato da API (quiz_api.json) foi carregado (por copy-paste devido à interface) para definir os endpoints.

Configuração da Conexão:

* Authentication method: Foi selecionado [Anonymous](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/17-create%20a%20custom%20tool_Jason%20with%20Python%20URL.png) (Anônimo).

* Schema (JSON): O conteúdo do [quiz_api.json](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/quiz_api.json) foi colado, incluindo a URL real do Codespace na seção servers (Ex: https://musical-trout-g4ppp9r99vx5cvr55-5000.app.github.dev/).

C. Finalização da Criação da Tool

* A Tool foi criada com sucesso, e a ação [AZ900QuizService](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/18-action%20created.png) aparece na seção "Actions" do Agente.

## Etapa 9: Testes Finais e Validação da Compatibilidade

* (Correção Crítica): Devido à incompatibilidade inicial do modelo [study-llm (GPT-5 Mini)](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/20-Erro%20400%20gpt-5-mini%20cannot%20be%20used.png) com ferramentas OpenAPI, foi necessário criar um [novo](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/21-Create%20new%20deployment.png) [Deployment](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/22-selecting%20gpt-4o.png) e trocar o modelo do Agente para o [GPT-4o](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/23-deploy%20gpt-4o.png).

(Teste Funcional): Após a troca para o GPT-4o, o Agente foi testado com [sucesso](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/24-test%202_WORKING.png), comprovando a chamada da Ação para o servidor Codespace e o retorno da [pergunta](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/24-test%202_WORKING2.png) de [quiz](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/25-test%203_second%20function.png), finalizando a Entrega [Técnica](https://github.com/Huth-P/AzureFrontierGirls-StudyBuddy-Python/blob/main/Guia_Implementacao/25-test%204_limitation%20function.png).
