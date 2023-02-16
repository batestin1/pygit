
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=pyGitPush%20POR&message=Bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center"> pyGitPush </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> This code implements a function called <i> gitPublish <i>, which creates a new repository on GitHub and automatically adds and commits code to a local repository and pushes it to the remote repository.

Required parameters are <i> key_access </i> (which is the GitHub access token), <i> user_name </i> (GitHub username), <i > local_remote</i> (the local address of the project folder), and <i> title </i> (the title of the repository that will be created).

Optional parameters are description (the description of the project on GitHub with at least 30 characters) and public (a boolean that indicates whether the repository should be public or private, the default being True).

In addition, the code has a helper function called get_latest_version, which returns the latest version number available in the remote repository. It also checks that the local repository exists and that the initialization of the local Git repository was successful. </p>

>> <h3> How install </h3>

```
from pyGitPush import gitPublish

```

>> <h3> How Works </h3>

```
key_acess = "github_pat_####################################"
user_name = 'user_git'
local_remote = 'C:/...'
title = "batataPython"

gygit(key_acess, user_name, local_remote, title, description=None, public=True)

```
    