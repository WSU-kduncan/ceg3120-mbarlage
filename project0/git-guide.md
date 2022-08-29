**status**
* Shows status of the local repository. This status includes:
number of local commits that have not been synced with remote (GitHub)
list of files in local folder than are NOT being tracked by git
list of files in local folder that have changes that need to be committed
- git status

**clone**
- def
- git clone <repo_name>

**add**
- add file for tracking
- git add <filename>

**rm**
- REMOVE 
- rm filename = remove file 
- rmdir <directory_name> = remove an empty directory
- rm -r <directory_name> = remove a non-empty directory and all the files within them

**commit**
- saves changes to your local repository
- git commit -m "commit message"

**push**
- uploads local repository content to a remote repository (such as GitHub)
- git push <repo_name> <branch_name>

**fetch**
- downloads content from the remote repository... it does not force to merge the changes into 
the repository, it just shows the progression of the central history 
- git fetch <branch_name>

**merge**
- combines multiple sequences of commits into one unified history. In frequent cases, merge is used to 
combine two branches
- git merge <branch_name>

**pull** 
- combination of git fetch + git merge. fetch updates the remote tracking branches while merge will
update your current branch with any new commits on the remote tracking branch
- git pull <branch_name>

**branch**
- creates a new branch, a separate version of the main repository
- git branch <branch_name>

**checkout**
- switch branches 
- get checkout <branch_name>
