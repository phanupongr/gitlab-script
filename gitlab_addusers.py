#/bin/env python
import argparse
import gitlab
import time
import os
import sys
import random
import string

# Users setup
users = [
  {
    username = "example"
    fullname = "firstName lastName"
    email = "example@gmail.com"
  }
]

parser = argparse.ArgumentParser(description = ''' Migration Scripts for Gitlab. ''')
parser.add_argument('--token',required=True, type=str, help='API token for access gitlab')
parser.add_argument('--url',required=True, type=str, help='Gitlab url address')
parser.add_argument('--ignore-ssl',required=False, type=bool, const=True, nargs='?', default=False, help='ignore ssl certifcate')
args = parser.parse_args()

# Random password
def random_password(length):
  characters = string.ascii_letters + string.digits + string.punctuation
  password = ''.join(random.choice(characters) for i in range(length))
  return password

# Create user
def create_gitlab_user(fullname, email, username, password):
  user = gl.users.create({
    'name': users[i].fullname,
    'email': users[i].email,
    'username': users[i].username,
    'password': password
    })
  user.save()
  return user

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

# Password of each user that created with this script, Minimun characters is 8
print("====================================================")
print("Begin create GitLab's user(s)...")
for i in range(len(users)):
  try:
    user = create_gitlab_user(users[i].fullname, users[i].email, users[i].username, password)
    print("Create user " + user.name + " successfull")
  except Exception as er:
    print("Unable to create user", str(er))
    sys.exit(1)
print("Success !")