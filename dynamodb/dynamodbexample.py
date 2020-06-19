
import boto3
import time
import json
import datetime

class DynamoDbResource:
    def __init__(self, region_name, table_name):
        self.region_name = region_name
        self.table_name = table_name
        self.dynamodb_client = boto3.client('dynamodb', region_name=self.region_name)

    def create_dynambo_table(self):
        response = self.dynamodb_client.create_table(
            AttributeDefinitions=[
                {
                    'AttributeName': 'CUSTOMER_ID',
                    'AttributeType': 'N'
                }
            ],
            TableName=self.table_name,
            KeySchema=[
                {
                    'AttributeName': 'CUSTOMER_ID',
                    'KeyType': 'HASH'
                }
            ],
            BillingMode='PAY_PER_REQUEST',
            Tags=[
                {
                    'Key': 'OrganicFoodsWebsite',
                    'Value': 'UserInfoDetails'
                }
            ]

        )
        response[""]

    def write_an_item(self, item=None):
        put_item_response = self.dynamodb_client.put_item(TableName=self.table_name, Item=item)
        print(put_item_response)

    def get_an_item(self, key=None):
        get_item_response = self.dynamodb_client.get_item(TableName=self.table_name, Key=key, ConsistentRead=True)
        return get_item_response

    def back_up_a_dynamodb_table(self, table_name=None, backup_name=None):
        back_up_name = backup_name + "_"+datetime.datetime.today().strftime("%Y_%m_%d_%H_%M_%S")
        back_up_response = self.dynamodb_client.create_backup(TableName=table_name, BackupName=back_up_name)
        return back_up_response


if __name__ == '__main__':
    dynamodb_object = DynamoDbResource("ap-south-1", "USER_INFO")
    # # dynamodb_object.create_dynambo_table()
    # user_info = {
    #     "user_name": "ashokb24",
    #     "first_name": "Ashok",
    #     "last_name": "Bhadrappa",
    #     "email_addr": "ashokb08@gmail.com",
    #     "phone_num": "9731808033",
    #     "alternate_phone_num": "NA",
    #     "usr_type": "enduser",
    #     "usr_crtd_ts": str(time.time()),
    #     "password": "Website1233"
    # }
    # item = {
    #     "CUSTOMER_ID": {
    #         "N": "123"
    #     },
    #     "user_info": {
    #         "S": json.dumps(user_info)
    #     }
    # }
    # dynamodb_object.write_an_item(item)
    # key = {
    #     "CUSTOMER_ID": {
    #         "N": "123"
    #     }
    # }
    # dynamodb_object.get_an_item(key)
    dynamodb_object.back_up_a_dynamodb_table(table_name="USER_INFO", backup_name="BKP_USER_INFO")
