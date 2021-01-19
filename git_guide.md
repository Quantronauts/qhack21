# Git tuto

## Install & start working on our qhack21 repo
```
# install
apt-get install git-all
# get the repo
git clone https://github.com/mickahell/qhack21.git
# if you have an ssh key link with your github account
git@github.com:mickahell/qhack21.git
```

## Starting a feature
- To work on our project we will use the tab `issues` on Github to structure what we need to do
- Select an issue, attribute it to yourself then create a branch with the name of th issue (with no space) :
```
git checkout -b my_feature
# check you are on your branch
git status
```
- Here you are now on your branch, make the changes you need, test them... **Have fun !**
-  You did some changes and you want to push them on GitHub to save it :
```
# check the whole changes you did
git status

# select the changes you want to send
git add toto.txt myfiles game.py

# write your commit message, explain in a few words what you did
git commit -m "blabla blabla"

# send your the files you select with the message
git push origin my_feature
```
- Now if your feature is finish, you have to make sure the version of your repository is the lastest so :
```
# get any new changes
git pull
```
- Sometimes when 2 peoples are working on the same file, that can create conflits. In this case don't hesitate to ask help (sometimes, it can be tricky) and we'll find a solution ;)

- Your branch is now ready to be merge with the branch develop. Go to Github, tab `Pull requests` and clic `New Pull request`:
	- Select as base the branch `develop` and as compare yours (here `myfeature`)don't forget to add the number of the issue you took in the title as `#1`
	- When the PR is ready, attribute it to someone who can just make a quick review, validate and clic `Merge`
- Then came back to your repo, get back on the `develop` branch get the new changes and restart the whole process by selecting another feature :
```
# get back on the branch develop
git checkout develop

# update your repo
git pull
```

## Few commands
Here a few commands using very often :
```
# get the whole repo
git clone your_depo

# check the status of your repo
git status

# update your depot
git pull

# create a new_branch
git checkout -b new_branch

# change on a branch (alrealdy exist)
git checkout old_branch

# add file to send
git add myfiles

# write commit message with the files you had
git commit -m "blabla"

# push your files
git push origin your_branch
```

## Reference
[git - the simple guide](http://rogerdudler.github.io/git-guide/index.html)
