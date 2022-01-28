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

