## Mission 11

![22](images/22.png)
- `cat end | grep -i "0JuAZ$"`
	- `grep` is used to find strings in a text file
	- `-i` is used to match strings irrespective of the case(lower or upper)
	- `$` is used to denote the end of the string

![23](images/23.png)

***
## Mission 12

![24](images/24.png)
- `cat file.yo | grep "^fu.*ck$"`
	- `grep` is used to find strings in a text file
	- `$` is used to denote the end of the string
	- `^` used to denote the start of the string
	- `.*` denotes an arbitrary string of arbitrary length

![25](images/25.png)

***

## Mission 13

![26](images/26.png)
- `env`

![27](images/27.png)
***

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

## Mission 17

![36](images/36.png)

- `find / -type f -mtime +18980 2>/dev/null`
	- `-mtime` it is a file property confirming the last time the file was modified
	- `(2022-1970) * 365 = 18980`
	- the `+` indicates older than 1970
![37](images/37.png)

***

## Mission 18

![38](images/38.png)


- run this on you local machine ([about scp](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/))
	- `scp -P 5000 clara@venus.hackmyvm.eu:~/protected.zip ~/` 
	- this is used to securely copy files from the remote location to your local desktop
	- `-P` mentions the ssh port
	- SYNTAX : `scp [OPTION] [user@]SRC_HOST:]file1 [user@]DEST_HOST:]file2`

![39](images/39.png)
. . . .

![40](images/40.png)
- `zip2john protected.zip > pass`
- we are getting the hashed form of the password
![41](images/41.png)
- `john pass --wordlist=/usr/share/wordlists/rockyou.txt`
- after executing this command we get the password for the protected zip file

- now we have to get the password for frida
![42](images/42.png)
***

## Mission 19
![43](images/43.png)
- we can use the commadn `uniq`
	- `uniq -d repeated.txt`
	- uniq is used to filter adjacent matching lines
	- `-d` is used to print only repeated lines

![44](images/44.png)

***

## Mission 20
![45](images/45.png)
![46](images/46.png)
- I'm not sure why the first one did not work
- `ssh -i .iris_key iris@localhost`
	- here localhost denotes computers IP and the port it is using, since we are already logged into venus.hackmyvm.eu I  think it works

![47](images/47.png)
- we get the password for `iris`

***