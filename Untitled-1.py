
import boto3

# # Let's use Amazon S3
# s3 = boto3.client('s3')

# theobjects = s3.list_objects_v2(Bucket='thegratefulbrauer', StartAfter='recipe_description_images/'+'bbearce'+'/recipes/')
# for object in theobjects['Contents']:
#     print(object['Key'])


recipe_root = 'recipe_description_images/'+'asdf'+'/recipes/'

s3 = boto3.client('s3')
objects = s3.list_objects_v2(Bucket='thegratefulbrauer', StartAfter=recipe_root)    

summaries = []
for s in objects['Contents']:
    if s['Key'].find('.jpg') != -1 and s['Key'].find(recipe_root) != 1:
        print(s['Key'], s['LastModified'])




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