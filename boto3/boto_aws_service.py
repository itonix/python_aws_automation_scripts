import boto3

client = boto3.client('s3')


def createbukt(bucket_name):
    try:
            created_bucket = client.create_bucket(
            ACL='private',
            Bucket= bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'eu-west-2',
                'Tags': [
                    {
                        'Key': 'mail',
                        'Value': 'welcome'
                    },
                ]
            },

            ObjectOwnership='BucketOwnerPreferred'
        )
            return ("Bucket created successfully: ", created_bucket['Location'])
    except Exception as e:
        return ("Error creating bucket: ", e)


def deletebukt(bucket_to_delete, bucket_names):
     if bucket_to_delete not in bucket_names:
        return ("ERROR: Bucket does not exist:", bucket_to_delete)
     else:
        try:
            client.delete_bucket(Bucket=bucket_to_delete)
            return ("Bucket deleted successfully:", bucket_to_delete)
        except Exception as e:
            return ("Error deleting bucket:", e)



############################################################################ Main Program to create or delete S3 bucket based on user input ##########


task = input("Create or Delete S3 Bucket based on user input'create'or'delete':").lower()

print("You selected {}".format(task))

if task == 'create':

    bucket_to_create = input ("Enter the unique bucket name to create: ")
    
    print(createbukt(bucket_to_create))
       
elif task == 'delete':

    # List existing buckets
    response = client.list_buckets()
    bucket_names = [b['Name'] for b in response['Buckets']]

    print("Existing buckets:")
    for name in bucket_names:
        print(" -", name)

    bucket_to_delete = input("Enter bucket name to delete: ")
    print(deletebukt(bucket_to_delete,bucket_names))
    
else:
    print("Invalid option. Choose 'create' or 'delete'.")




################ Check if bucket exists, if not create it #####################

#      if (bucket_to_create == bucket_name['Name']):
#         print("ERROR:The requested Bucket found: ", bucket_name['Name'])
#         break
# else:
   

################ List objects in a bucket #####################

# list_contents = client.list_objects(
#     Bucket='my-wemail-template1',
#     EncodingType='url',
   
# )


# for content in list_contents['Contents']:
#      print("File: ...... {}".format(content['Key']))
 
#  ################ Upload a file to a bucket #####################   
    
# client.upload_file('D:\python\plants.txt', 'my-wemail-template1', 'hello.txt')


# deletebucket = client.delete_bucket(
#     Bucket= bucket_to_create,
    
# )
# print("Bucket deleted successfully: ", deletebucket)


