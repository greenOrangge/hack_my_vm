> This can be found [here](https://hackmyvm.eu/venus/)
```
Host: venus.hackmyvm.eu

Port: 5000

User: hacker

Pass: havefun!
```

- let's login using `ssh hacker@venus.hackmyvm.eu -p 5000`
	- description `ssh user@host -p (port number)`


- after logging in:

## Mission 1
![1](images/1.png)
- we can use the `ls` command to list the contents of the directory
- `cat` is used the print the file contents as output
- so the password is saved in a hidden file
- let's try `ls -a` 
	- the `-a` is used to list hidden files (read more about it using `man ls`)
![2](images/2.png)
- We get the password for the next level!!
- Now we have to login as sophia using the obtained password
- we can use `su sophia`
	- `su` is used to switch user or run a command  with substitute user
	- so here we are switching the user to sophia
- when we try `ls` we get a permission denied message
- now let's go back a directory `cd ..` and ls
- we can find many users, let's go to sophia
![4](images/4.png)
- here we can find the flag and the next mission!

***

## Mission 2

- For this mission we have to find a file called `whereismypazz.txt` 
- we can use a command `find`
- `find / -name whereismypazz.txt -type f 2>/dev/null`
	- here `/` tells to find form the root directory
	- `-name` flag is used to specify name
	- `-type f` us used to specify the type of files here `-f` mentions files, `-d` is used for directories
	- `2>/dev/null` is a file descriptor used to dump all the errors and not diplay them in the output
![5](images/5.png)
- now we can log in as angela and proceed to the next mission

*** 

## Mission 3

- The password for emma is stored in line `4069` of the file `findme.txt`
- We can read through each line of the file, but there is a more efficient way to do it
- we can use `cat` and `grep`
- `cat -n findme.txt  | grep "4069"`
	- cat `-n` numbers all the output lines
	- once the lines are numbered, we can `grep` them (check `man grep`)
![6](images/6.png)

***

## Mission 4

![7](images/7.png)

- `cat ./-`

![8](images/8.png)

***

# Mission 5

![9](images/9.png)

- `find / -name hereiam -type d 2>/dev/null`
	
![10](images/10.png)

***
## Mission 6

![11](images/11.png) 
- `find . -type f`

![12](images/12.png)

***
## Mission 7

![13](images/13.png)
- `find / -type f -size 6969c 2>/dev/null`

![14](images/14.png)

***

## Mission 8

![15](images/15.png)
- `find / -type f -user violin 2>/dev/null`

![16](images/16.png)
***
## Mission 9 

![17](images/17.png)
![18](images/18.png)
- since we dont have permissions,  we should create a directory in the `/tmp` directory
- `unzip passw0rd.zip -d /tmp/hj`
	- `-d` is used to mention an optional directory to which to extract files

![19](images/19.png)

***

## Mission 10

![20](images/20.png)
- `cat passy | grep -i "^a9HFX"`
	- `grep` is used to find strings in a text file
	- `-i` is used to match strings irrespective of the case(lower or upper)
	- `^` used to denote the start of the string

![21](images/21.png)

***
