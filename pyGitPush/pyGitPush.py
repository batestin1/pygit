
#############################################################################################################################
#   filename:pyGitPush.py                                                       
#   created: 2023-02-15                                                              
#   import your librarys below                                                    
#############################################################################################################################

import os
import requests
from datetime import datetime

def gitPublish(key_acess, user_name, local_remote, title, description=None, public=True):
    """
    Creates a repository on GitHub and automatically commits and pushes the code to the created repository.

    Mandatory parameters:
    key_access(str): Access token for GitHub
    user_name(str): GitHub username
    local_remote(str): local address of project folder
    title(str): title of the repository to be created

    Optional parameters:
    description (str): GitHub project description (at least 30 characters long)
    public (bool): whether the repository will be public or private (default: public)
    """

    if not key_acess or not user_name or not local_remote or not title:
        raise ValueError('GitHub token, username, repository name, and local path are required.')

    # Check if local_remote exists
    if not os.path.exists(local_remote):
        raise FileNotFoundError(f'{local_remote} does not exist. Please provide a valid path.')

    # Change to local_remote and initialize Git repo
    os.chdir(local_remote)
    os.system('git init')

    # Check if Git repo was initialized correctly
    if not os.path.exists(os.path.join(local_remote, '.git')):
        raise Exception(f'Error initializing Git repo at {local_remote}')

    # Create repository on GitHub
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization': f'token {key_acess}'}
    payload = {
        'name': title,
        'description': description,
        'private': not public
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 201:
        raise Exception(f'Error creating repository on GitHub: {response.content}')

    # Add and commit changes to Git repo
    os.system('git add .')
    version = get_latest_version()
    version += 1
    date_now = datetime.now().strftime("%Y%m%d")
    commit = f"Version {version} - {date_now}"
    os.system(f'git commit -m "{commit}"')

    # Push changes to GitHub
    os.system('git branch -M main')
    remote_url = f'https://github.com/{user_name}/{title}.git'
    os.system(f'git remote add origin {remote_url}')
    os.system('git push -u origin main')

    # Clean up local_remote
    os.chdir('..')
    os.system(f'rm -rf {local_remote}')


def get_latest_version():
    """
    Returns the number of the latest version available in the remote repository.

    Returns 0 if there are no versions yet.
    """

    os.system('git fetch --tags')

    tags = os.popen('git tag --sort=committerdate').readlines()
    tags.reverse()

    for tag in tags:
        if tag.startswith('Version'):
            version = tag.split('Version')[1].split()[0]
            return int(version)

    return 0
