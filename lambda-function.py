import boto3
import os

def lambda_handler(event, context):
    acm_client = boto3.client('acm', region_name='us-east-1')
    sns_client = boto3.client('sns')
    
    certificate_arn = os.environ.get("CERTIFICATE_ARN")
    sns_topic_arn = os.environ.get("SNS_TOPIC_ARN")
    
    try:
        # Consulta o status do certificado
        response = acm_client.describe_certificate(CertificateArn=certificate_arn)
        status = response.get('Certificate', {}).get('Status')
        print(f"Status do certificado {certificate_arn}: {status}")
    except Exception as e:
        print(f"Erro ao consultar o certificado: {e}")
        return {"status": "erro", "message": str(e)}
    
    # Se o certificado estiver validado, envia a notificação via SNS
    if status == 'ISSUED':
        message = f"O certificado {certificate_arn} foi validado com sucesso!"
        try:
            sns_client.publish(
                TopicArn=sns_topic_arn,
                Message=message,
                Subject="Certificado Emitido"
            )
            print("Notificação enviada via SNS.")
            return {"status": "notificado", "message": message}
        except Exception as e:
            print(f"Erro ao enviar notificação via SNS: {e}")
            return {"status": "erro", "message": str(e)}
    else:
        # Se o certificado não estiver validado, não envia notificação
        print("Certificado ainda não está validado. Nenhuma notificação enviada.")
        return {"status": "aguardando", "certificate_status": status}
