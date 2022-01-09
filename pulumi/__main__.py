import pulumi
import pulumi_eks as eks

# Create an EKS cluster with the default configuration.
cluster = eks.Cluster('my-cluster')

# Export the cluster's kubeconfig.
pulumi.export('kubeconfig', cluster.kubeconfig)

# CREATE BUCKET

# """An AWS Python Pulumi program"""

# import pulumi
# from pulumi_aws import s3
# # Create an AWS resource (S3 Bucket)
# bucket = s3.Bucket('my-bucket')

# # Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)

# ADD BUCKET WITHOUT LOOPS

# """An AWS Python Pulumi program"""

# import pulumi
# from pulumi_aws import s3
# # Create an AWS resource (S3 Bucket)
# bucket = s3.Bucket('my-bucket')
# bucket2 = s3.Bucket('my-bucket_2')
# # Export the name of the bucket
# pulumi.export('bucket_name', bucket.id)
# pulumi.export('bucket_name', bucket2.id)


# ADD BUCKET WITH LOOP

# """An AWS Python Pulumi program"""

# import pulumi
# from pulumi_aws import s3
# # Create an AWS resource (S3 Bucket)
# for i in range (1, 5):
#     bucket = s3.Bucket('my-bucket-' + str(i))
#     pulumi.export('bucket_name', bucket.id)

# DIRTY HARD CODED STATIC WEBSITE

# import pulumi
# import pulumi_aws as aws

# size = 't2.micro'

# ami = aws.ec2.get_ami(most_recent=True,
#                   owners=["137112412989"],
#                   filters=[aws.GetAmiFilterArgs(name="name", values=["amzn-ami-hvm-*"])])

# group = aws.ec2.SecurityGroup('web-secgrp',
#     description='Enable HTTP access',
#     ingress=[aws.ec2.SecurityGroupIngressArgs(
#         protocol='tcp',
#         from_port=80,
#         to_port=80,
#         cidr_blocks=['0.0.0.0/0'],
#     )])

# user_data = """
# #!/bin/bash
# echo "Hello, World!" > index.html
# nohup python -m SimpleHTTPServer 80 &
# """

# server = aws.ec2.Instance('web-server-www',
#     instance_type=size,
#     vpc_security_group_ids=[group.id],
#     user_data=user_data,
#     ami=ami.id)

# pulumi.export('public_ip', server.public_ip)
# pulumi.export('public_dns', server.public_dns)