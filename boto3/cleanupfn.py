#Simple cleanup report generator for EC2 instances and S3 objects:


from datetime import datetime, timezone, timedelta
import boto3

clientec2 = boto3.client('ec2', region_name='eu-west-2')
clients3 = boto3.client('s3')
clientsns = boto3.client('sns', region_name='eu-west-2')

def lambda_handler(event, context):
    task = event.get('action')
    if task == 'cleanup':
        try:
          ec2_status = ec2_cleanup()
          status_s3 = s3_cleanup()
          message = f"The following EC2 instances are eligible for cleanup:\n"
          message += f"EC2 Cleanup Candidates: {ec2_status['candidates']}\n"
          message += f"S3 Deleted Objects: {status_s3['deleted_repo']}\n"
          message += f"S3 Latest Objects: {status_s3['latest_repo']}\n"

          send_mail = clientsns.publish(
              TopicArn='arn:aws:sns:eu-west-2:964936527908:cleanup',
              Subject='Cleanup Task Report',
              Message= message,)
        except Exception as e:
          print(f"Error during cleanup: {e}")
          return {
              'statusCode': 500,
              'body': f"Error during cleanup: {e}"
          } 
        
    

####################################################################### EC2

def ec2_cleanup():
    response = clientec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:cleanup',
                'Values': ['true']
            }
        ]
    )
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                "id": instance['InstanceId'],
                "state": instance['State']['Name'],
                "launch": instance['LaunchTime'],
                "tags": instance.get('Tags', [])
            })


    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=7)

    candidates = []

    for inst in instances:
        if inst["state"] != "stopped":
            continue
        # if inst["launch"] > cutoff:
        #     continue
        candidates.append(inst["id"])
    return {
        "candidates": candidates
    }
######################################################################### s3


def s3_cleanup():
    Bucket_to_check = "amzerleft"
    prefix = "repository/"   
    version_info = clients3.get_bucket_versioning(Bucket=Bucket_to_check)
    if version_info.get("Status") != "Enabled":
        print(f"{Bucket_to_check} is not versioned")
    else:
        print(f"{Bucket_to_check} is versioned")

        response = clients3.list_object_versions(
            Bucket=Bucket_to_check,
            Prefix=prefix
        )

        versions = response.get("Versions", [])
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=30)

        Latest_each_object = None
        delete_list = []
        latest_repo = []
        for each_obj in versions:
            if each_obj.get("IsLatest"):
                Latest_each_object = each_obj

            if (not each_obj.get("IsLatest")
                and each_obj['LastModified'] < cutoff):

                clients3.delete_object(
                    Bucket=Bucket_to_check,
                    Key=each_obj['Key'],
                    VersionId=each_obj['VersionId']
                )
                delete_list.append({
                    "Key": each_obj['Key'],
                    "VersionId": each_obj['VersionId']
                })
        if Latest_each_object:
            latest_repo.append({
                "Key": Latest_each_object['Key'],
                "VersionId": Latest_each_object['VersionId']
            })
    return {
        "deleted_repo": delete_list,
        "latest_repo": latest_repo
    }




