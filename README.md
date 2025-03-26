# Automação de Notificação de Certificado SSL com AWS Lambda

Este projeto surgiu da necessidade de implementar um certificado SSL no meu site, [eduardolentz.com.br](http://www.eduardolentz.com.br), utilizando serviços da AWS como ACM (AWS Certificate Manager), Route53 e CloudFront.

No processo, precisei criar um certificado SSL no ACM, validá-lo com registros DNS no Route53 e posteriormente criar uma distribuição no CloudFront para utilizar o certificado validado.

## Mas... Por que a automação?

Como toda pessoa ansiosa, não queria ficar atualizando a página do ACM a cada 2 minutos para conferir se o certificado já estava validado. Então, decidi criar uma pequena automação usando **AWS Lambda** com **SNS (Simple Notification Service)**, para receber um e-mail automaticamente assim que o certificado estivesse disponível.

## Como a Automação Funciona?

A automação verifica o status do certificado ACM a cada 5 minutos (usando uma regra do EventBridge). Quando o certificado muda para o status `ISSUED`, recebo imediatamente uma notificação por e-mail, avisando que o certificado já está disponível para uso.

### Tecnologias Usadas
- **AWS ACM**: Gerenciamento e validação do certificado SSL/TLS
- **AWS Route53**: Gerenciamento dos registros DNS
- **AWS CloudFront**: Distribuição segura e rápida do conteúdo do site
- **AWS Lambda**: Execução da função para checar status do certificado
- **AWS SNS**: Envio automático da notificação por e-mail
- **AWS EventBridge**: Agendamento periódico para execução da Lambda

## Estrutura do Projeto

```
acm-automation/
├── lambda_function.py            # Código Lambda que verifica o status do certificado
├── acm_notification_policy.json  # Política IAM para execução da Lambda
└── README.md                     # Documentação geral (você está aqui!)
```

## Como utilizar

1. Solicite um certificado no ACM e crie registros no Route53.
2. Configure o tópico SNS e faça a assinatura para receber notificações.
3. Faça o deploy do código Lambda, configurando as variáveis:
   - `CERTIFICATE_ARN`: ARN do seu certificado no ACM
   - `SNS_TOPIC_ARN`: ARN do seu tópico SNS
4. Crie uma regra no EventBridge para executar a Lambda periodicamente.

### Agora, basta relaxar enquanto a automação cuida do resto! ✌🏽😎
---
### Saiba mais sobre a implementação

Quer entender os bastidores deste projeto e como integrei vários serviços da AWS para resolver um problema real?  
Confira o artigo completo no Medium, com os detalhes e aprendizados:

🔗 [Como automatizei a validação do meu certificado SSL usando AWS Lambda (e me livrei da ansiedade)](https://medium.com/@eduardolentz/como-automatizei-a-valida%C3%A7%C3%A3o-do-meu-certificado-ssl-usando-aws-lambda-e-me-livrei-da-ansiedade-5b82ae8abf86)


--- 

### Eduardo O. Lentz  
💻 [Portfolio](http://www.eduardolentz.com.br) | 🔗 [LinkedIn](https://www.linkedin.com/in/eduardolentz) | 📂 [GitHub](https://github.com/eduardolentz) | 📝 [Medium](https://medium.com/@eduardolentz) | 📸 [Instagram](https://www.instagram.com/eduardolntz/)

