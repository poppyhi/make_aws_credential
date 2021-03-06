import json
import subprocess
import os

token_code = input('Enter token code:')

# create session token(10hours)
command = 'aws sts get-session-token --serial-number arn:aws:iam::[hoge] --duration-seconds 36000 --token-code ' + str(token_code)
ret = subprocess.check_output(command, shell=True)

credentials = json.loads(ret)

AccessKeyId = credentials["Credentials"]["AccessKeyId"]
SecretAccessKey = credentials["Credentials"]["SecretAccessKey"]
SessionToken = credentials["Credentials"]["SessionToken"]

filename = "set_aws_credential.bat"
with open(filename, mode='w') as f:
    f.write("@echo off\n")
    f.write("set AWS_ACCESS_KEY_ID=" + AccessKeyId + "\n")
    f.write("set AWS_SECRET_ACCESS_KEY=" + SecretAccessKey + "\n")
    f.write("set AWS_SESSION_TOKEN=" + SessionToken + "\n")
