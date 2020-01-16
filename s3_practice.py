
import boto3

# # Let's use Amazon S3
# s3 = boto3.client('s3')

# theobjects = s3.list_objects_v2(Bucket='thegratefulbrauer', StartAfter='recipe_description_images/'+'bbearce'+'/recipes/')
# for object in theobjects['Contents']:
#     print(object['Key'])


recipe_root = 'recipe_description_images/'+'asdf'+'/recipes/'

# s3_client = boto3.client('s3')
# s3_resource = boto3.resource('s3')
# my_bucket = s3_resource.Bucket('thegratefulbrauer')
# my_bucket.put_object(Bucket='thegratefulbrauer', Body='', Key=recipe_root)




# Check if file exists
s3 = boto3.resource('s3')
bucket = s3.Bucket('thegratefulbrauer')
objs = list(bucket.objects.filter(Prefix=recipe_root))
if(len(objs)>0):
    print("key exists!!")
else:
    print("key doesn't exist!")






# objects = s3.list_objects_v2(Bucket='thegratefulbrauer', StartAfter=recipe_root)    

# summaries = []
# for s in objects['Contents']:
#     if s['Key'].find('.jpg') != -1 and s['Key'].find(recipe_root) != 1:
#         print(s['Key'], s['LastModified'])




# # summaries = []
# # for s in objects['Contents']:
# #     if s['Key'].find('.jpg') != -1:
# #         summaries.append(
# #             {'key':s['Key'].replace(recipe_root,''),
# #              'last_modified': s.last_modified,
# #             }
# #         )

        
# # Upload a new file
# # data = open('./static/favicon-32x32.png', 'rb')
# # s3.Bucket('thegratefulbrauer').put_object(Key='recipe_description_images/bbearce/recipes/favicon-32x32.png', Body=data)







# from boto3 import client, resource

# class S3Helper:

#   def __init__(self):
#       self.client = client("s3")
#       self.s3 = resource('s3')

#   def create_folder(self, path):
#       path_arr = path.rstrip("/").split("/")
#       if len(path_arr) == 1:
#           return self.client.create_bucket(Bucket=path_arr[0])
#       parent = path_arr[0]
#       bucket = self.s3.Bucket(parent)
#       status = bucket.put_object(Key="/".join(path_arr[1:]) + "/")
#       return status

# s3 = S3Helper()
# s3.create_folder("bucket_name/folder1/folder2)