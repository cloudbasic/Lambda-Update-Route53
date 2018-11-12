from __future__ import print_function

import boto3, json, re

HOSTED_ZONE_ID = 'YOUR_HOSTED_ZONE_ID'

def lambda_handler(event, context):
    route53 = boto3.client('route53')

    dns_changes = {
        'Changes': [
            {
                'Action': 'UPSERT',
                'ResourceRecordSet': {
                    'Name': event['name'],
                    'Type': 'CNAME',
                    'ResourceRecords': [
                        {
                            'Value': event['value']
                        }
                    ],
                    'TTL': 300
                }
            }
        ]
    }

    print("Updating Route53")

    response = route53.change_resource_record_sets(
        HostedZoneId=HOSTED_ZONE_ID,
        ChangeBatch=dns_changes
    )

    return {'status':response['ChangeInfo']['Status']}