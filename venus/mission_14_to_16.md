## Mission 14

![28](images/28.png)
- it is mostly the `/etc/passwd`
- `cat /etc/passwd | grep "alice"`

![29](images/29.png)

***

## Mission 15

![30](images/30.png)
- let's try `sudo -l`
	- it lists the allowed commands for that particular user

![31](images/31.png)
- using `sudo -u natalia /bin/bash`
	- this runs the command as the specified user
	- from the above we know that it has access to the `/bin/bash` file
![32](images/32.png)
- we get the password for natalia
![33](images/33.png)
***

## Mission 16

![34](images/34.png)
- `base64 -d base64.txt`
	- `base64`
	- `-d` to decode the text
	- followed by the file name

![35](images/35.png)
***

