import boto3

# Function to Add a Single Item in Address Book
def add_entry(table, mobile, name, city, email, joining_fees):
    table.put_item(
        Item={
            "mobile":mobile,
            "info":{"c_name":name, "city":city, "email":email, "joining_fees":joining_fees}
            }
        )

# Function to Open the Item form the Address Book
def open_entry(table, mobile):
    try:
        result=table.get_item(
            Key={"mobile":mobile}
            )["Item"]
        print(result)
    except:
        print("Error: Record Not Fetched")
    
# Function to Delete Whole Address Book (DynamoDB Table)
def delete_address_book(table):
    try:
        table.delete()
    except:
        print("Error: Table Not Deleted")
    
# Function to Update Single Item in Address Book
def update_entry(table, mobile, name, city, email, joining_fees):
    try:
        table.update_item(
            Key={"mobile":mobile},
            UpdateExpression="SET info.c_name=:new_name, info.city=:new_city, info.email=:new_email, info.joining_fees=:new_joining_fees",
            ExpressionAttributeValues={":new_name":name, ":new_city":city, ":new_email":email, ":new_joining_fees":joining_fees}
            )
    except:
        print("Error: Update Failed")
        
# Function to Delete Single Item from Address Book
def delete_entry(table, mobile):
    try:
        table.delete_item(
            Key={"mobile":mobile}
            )
    except:
        print("Deletion Failed")
        
# Function to Search Single Item in Address Book
def search_entry(table, field_name, field_value):
    try:
        result=table.scan(FilterExpression=boto3.dynamodb.conditions.Attr(field_name).eq(field_value))["Items"]
        print("Records Found Are\n")
        for i, res in enumerate(result):
            print(f"{i+1} = {res}\n")
    except:
        print("Error in Searching")