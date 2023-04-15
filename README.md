# aws-s3-pdf-to-text
A simple AWS workflow to get text from S3 ingested PDF.

This workflow is using serverless Framework.

**Language used:** python3.9

**Package used:** PyPDF2


**Services used:**
 - S3
 - Cloudwatch
 - Lambda

### Deployment
```sh
npm install
serverless deploy --stage test --region us-east-1
```

### Modify depending on your needs
You can edit the `handler.py` file to insert your code.
```python3
# handler.py
from src.pdf2text import getPdfTextFromS3

def pdf2text(event, context):
    text: str = getPdfTextFromS3(event)

    #--------- Your code goes here :)

    print(text)

    #############################################

    return {
        "statusCode": 200,
        "body": text
    }
```

## How to use
Upload a PDF file to `${self:service}-${sls:stage}-pdf-inputs` S3 bucket.
You can rename AWS resources directly in the `serverless.yml` file.
