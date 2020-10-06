#/bin/env python
import argparse
import gitlab
import time
import os
import sys

users = []
parser = argparse.ArgumentParser(description = ''' Migration Scripts for Gitlab. ''')
parser.add_argument('--token',required=True, type=str, help='API token for access gitlab')
parser.add_argument('--url',required=True, type=str, help='Gitlab url address')
parser.add_argument('--ignore-ssl',required=False, type=bool, const=True, nargs='?', default=False, help='ignore ssl certifcate')
args = parser.parse_args()

print("====================================================")
print("Setup option to connect Gitlab...")
if args.ignore_ssl:
  gl = gitlab.Gitlab(args.url, private_token=args.token , ssl_verify=False)
  time.sleep(1)
else:
  gl = gitlab.Gitlab(args.url, private_token=args.token)
  time.sleep(1)

try:
  print("Try to authenticate with Gitlab...")
  gl.auth()
  time.sleep(1)
  print("Connect to Gitlab successfull")
except Exception as er:
  print(str(er))
  sys.exit(1)

password = 'password'

print("====================================================")

for i in range(len(users)):
  try:
    user = gl.users.create({'email': users[i] +'@example.com' , 'password': users[i] , 'username': users[i], 'name': users[i], 'skip_confirmation': True})
    user.save()
    print("Create user " + user.name + " successfull")
  except Exception as er:
    print(str(er))
    sys.exit(1)
