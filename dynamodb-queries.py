import boto3
import simplejson as json
from environs import Env
env = Env()
print(env.read_env())



def save_json_file(response,file_name):
    with open(file_name, 'w') as outfile:
        json.dump(response['Items'], outfile)

dynamodb = boto3.resource('dynamodb','eu-west-1',aws_access_key_id=env("aws_access_key_id"),
    aws_secret_access_key=env("aws_secret_access_key"))

table_mc_features = dynamodb.Table('mc_features_production')
table_feature_users = dynamodb.Table('feature_users_production')



save_json_file(table_feature_users.scan(),'features_users_production.json')
save_json_file(table_mc_features.scan(),'data.json')

# read_file('/Users/alisoliman/Development/Python/aiesecinternational-rnd/features_users_production.json')
