# AddressBook Application in Python (Amazon DynamoDB)

This is simple AddressBook Application implemented in Python. The application is in CLI Version. It uses [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) as NoSQL Database

## Dependecies
- [Boto3: AWS SDK for Python](https://github.com/boto/boto3)

## Getting Started
- Get AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY for your IAM User
- Replace above credentials in [app_config.py](https://github.com/atharvawagare/aws-addressbook-app/blob/main/app_config.py)
```python
aws_access_key_id="AWS_ACCESS_KEY_ID"
aws_secret_access_key="AWS_SECRET_ACCESS_KEY"
region_name="us-east-1"
```
- Run [main.py](https://github.com/atharvawagare/aws-addressbook-app/blob/main/main.py)
```console
python main.py
```
