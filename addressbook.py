import app_config as c
import boto3
from botocore.exceptions import ClientError

class AddressBook:

    def __init__(self):
        print("Working on Creating the Address Book")
        self.table_name="AddressBook"
        
        # Get Session Object from AWS Server
        self.session=boto3.Session(
            aws_access_key_id=c.aws_access_key_id,
            aws_secret_access_key=c.aws_secret_access_key,
            region_name=c.region_name
            )

        self.dyn=self.session.resource("dynamodb")
        
        try:
            self.table=self.dyn.create_table(
                TableName=self.table_name,
                KeySchema=[{"AttributeName":"mobile", "KeyType":"HASH"}],
                AttributeDefinitions=[{"AttributeName":"mobile", "AttributeType":"S"}],
                ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 1}
                )
            self.table.wait_until_exists()
            
            print("Address Book is Ready for Your Use")
            
        except ClientError as e:
            print("Address Book is None")
            print(e)
            self.table=None
            
    def get_address_book(self):
        return self.table