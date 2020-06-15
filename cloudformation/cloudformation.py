import boto3
import json


class CloudFormationResource:
    def __init__(self, region_name, cft_file_name):
        self.region_name = region_name
        self.cft_file_name = cft_file_name
        self.cloud_formation_client = boto3.client('cloudformation', region_name=self.region_name)

    def create_cloud_formation_stack(self, stack_name=None, parameters_map=None):
        with open(self.cft_file_name) as cft_file:
            cft_json_data = json.load(cft_file)

        response = self.cloud_formation_client.create_stack(
            StackName=stack_name,
            TemplateBody=json.dumps(cft_json_data),
            Parameters=parameters_map,
            TimeoutInMinutes=3,
            OnFailure='ROLLBACK'
        )
        return response

    def update_cloud_formation_stack(self, stack_name=None, parameters_map=None):
        with open(self.cft_file_name) as cft_file:
            cft_json_data = json.load(cft_file)

        response = self.cloud_formation_client.update_stack(
            StackName=stack_name,
            TemplateBody=json.dumps(cft_json_data),
            Parameters=parameters_map
        )
        return response

    def destroy_cloud_formation_stack(self, stack_name=None):
        response = self.cloud_formation_client.delete_stack(
            StackName=stack_name
        )
        return response


if __name__ == '__main__':
    cloud_formation_object = CloudFormationResource("ap-south-1", "dynamodbtable_cft.json")
    parameters = [{
        'ParameterKey': 'TableName',
        'ParameterValue': 'USER_INFO'
    }]
    cloud_formation_object.create_cloud_formation_stack(stack_name="sample-dynamodb-table-stack",
                                                         parameters_map=parameters)
    # cloud_formation_object.update_cloud_formation_stack(stack_name="sample-dynamodb-table-stack",
    #                                                     parameters_map=parameters)
    # cloud_formation_object.destroy_cloud_formation_stack(stack_name="sample-dynamodb-table-stack")
