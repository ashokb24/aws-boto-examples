import boto3


class sqsUtils:

    def __init__(self, region_name):
        self.region_name = region_name
        self.sqs_client = boto3.client('sqs', region_name=self.region_name)

    def list_queues(self):
        # Create SQS client
        response = self.sqs_client.list_queues()
        print(response)

    def create_sqs_queue(self):
        # Create a SQS queue
        response = self.sqs_client.create_queue(
            QueueName='twitter_queue',
            Attributes={
                'DelaySeconds': '60',
                'MessageRetentionPeriod': '86400'
            }
        )


if __name__ == '__main__':
    sqsUtils = sqsUtils("ap-south-1")
    sqsUtils.list_queues()
    sqsUtils.create_sqs_queue()
