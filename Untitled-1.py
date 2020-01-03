
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

# Upload a new file
data = open('./static/favicon-32x32.png', 'rb')
s3.Bucket('thegratefulbrauer').put_object(Key='recipe_description_images/bbearce/recipes/favicon-32x32.png', Body=data)
