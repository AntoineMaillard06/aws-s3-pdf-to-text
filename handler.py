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
