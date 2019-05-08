
import simplejson as json
import csv
from execute_sql import execute_sql

## This script is to get the operational data from the A/B Tested users and match them together to understand how did they behave after the experiment have been conducted.


def read_file(path):
    
    
        with open(path) as f:
            data = json.load(f)
            for i in range(0,len(data)-1):
                result = execute_sql('queries/first_application.sql',int(data[i]['person_id']))
                print('We are at ' + str(round(i/len(data)*100,2)) + '%.')
                with open('people.csv', 'a') as csvFile:
                        writer = csv.writer(csvFile, delimiter=",", lineterminator="\r\n")
                        writer.writerow(result[0]) 
                        csvFile.close()


read_file('/Users/alisoliman/Development/Python/aiesecinternational-rnd/features_users_production.json')



