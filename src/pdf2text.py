import boto3
import io
from PyPDF2 import PdfReader

def getPdfTextFromS3(event):
    s3Client = boto3.client('s3')
    data = ''

    for record in event['Records']:
        content = s3Client.get_object(
            Bucket = record['s3']['bucket']['name'],
            Key = record['s3']['object']['key']
        )
        pdfData = io.BytesIO(content['Body'].read())
        pdfReader = PdfReader(pdfData)
        for page in pdfReader.pages:
            data += page.extract_text()

    return data