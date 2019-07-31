#!/usr/bin/python

import boto3
import subprocess

ec2 = boto3.resource('ec2')

keyFile = open('key.pem', 'w') # prepare ssh key file

pair = ec2.create_key_pair(KeyName='keypair') # create keypair within aws and local machine

kout = str(pair.key_material) # capture key output
keyFile.write(kout) # store key in the file

subprocess.call([chmod 400 key.pem]) # make key file read only

instances = ec2.create_instances(
	ImageId='ami-0b898040803850657',
	MinCount=1,
	MaxCount=1,
	InstanceType='t2.micro',
	KeyName='keypair'
)