# Mission 41

![89](images/89.png)
- If we curl that page we get:
![90](images/90.png)
- We have to set the `key` header to `true` to get the password for the next mission.
- `curl -H "key:true" http://localhost/key.php`

***

# Mission 42

![91](images/91.png)
- `ls -a` and we can get the password 
![92](images/92.png)

***

# Mission 43

![93](images/93.png)
- this  user is always wrong with paula's password...hmmm...so mercy knows paula's password, and she would have entered it previously
- To check the previous commands used by a user, we can view the `.bash_history` or type `history` in the cmd
- And we can get the password for paula

***

# Mission 44

![94](images/94.png)
- It gives us a hint about groups, we can create a group and provide specific permission to that particular group
- We can view the group by using `id` command
![95](images/95.png)
- Now let's find all the files under the group `hidden`
- `find / -type f -group hidden 2>/dev/null`
  - `find` used to find files 
  - `/` we tell the command to start searching from the root directory
  - `type` search for a files
  - `group` search for a particular group
  - `2>/dev/null` we redirect all the errors to the /dev/null **2** is stderr in linux
![96](images/96.png)

***

# Mission 45

![97](images/97.png)
- So this is some type of steganography, i.e hiding messages in images
- Let's first start reading the meta data of this image
- `exiftool yuju.jpg`
- If we see the output carefully, we get tha password for the next mission.

*** 

# Mission 46

![98](images/98.png)
- `doas` is used to execute commands as another user
- Let's try accessing zora using this
- `doas -u zora bash`

***

# Mission 47

![99](images/99.png)
- Ok, so let's find this file
- `find / -type f 2>/dev/null | grep "venus"`
- the password we get here is not the password
- We have to add a header to get the password
- `curl -H "HOST:venus.hmv" http://localhost/` 

***

# Mission 48

![100](images/100.png)
- This seems like a hash of a password from the `$1$`
- After a bit of googling, this seems to be a `MD5` hash
- `john