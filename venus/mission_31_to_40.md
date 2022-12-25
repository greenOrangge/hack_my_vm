# Mission 31

![75](images/75.png)
- Let's get the data on `waiting.php`
![76](images/76.png)
- Ok, so we have to use the `user-agent` header for this mission.
- `curl  http://localhost/waiting.php -H "user-agent: PARADISE"`
    - `-H` is used to set header value
![77](images/77.png)

***

# Mission 32

![78](images/78.png)
- `aliases` are used to store a particular commmand.
- **creating an alias**
    - `alias alias_name="command_to_run"`
- to view the aliases, all we have to do is type `alias` in the cmd
![79](images/79.png)

***

# Mission 33

![80](images/80.png)
- Ok, so we have to extract the compressed file
![81](images/81.png)
- `1` : it is a tar archive
- `2` : since we don't have permission to create files in the home directory we create one in the `/tmp` dir
- `3` : extraction `tar -xf zip.gz --directory /tmp/mission_33`
  - `x` tell the tar to **extract**
  - `f` specifies the file
- now let's go to the dir in `/tmp` and we find the password 

***
# Mission 34

![82](images/82.png)
- If we cat the file we find all gibberish, nothing makes sense to us
- We can use `strings` to find the strings in the file
- `strings trash` we can find the pass for the next mission ( we have to remove the first 2 letters)

***

# Mission 35

![83](images/83.png)
- Ok so we have to find the last 2 letters of the password, by bruteforcing using hydra
- For coming up with a wordlist for bruteforcing ssh, we can write a python script
```python
import string
# storing the given password
known_pass = "v7xUVE2e5bjUc"

# stored all the lowercase letters
letters = string.ascii_lowercase

# used to generate the wordlist
for letter_1 in letters:
    for letter_2 in letters:
        new_pass = known_pass + letter_1 + letter_2
        print(new_pass)
```

- let's run the code and store the output in a wordlist
`python3 mission_35_wordlist.py > wordlist_35.txt`
    - we are storing the output to `wordlist_35.txt`
- now we can use hydra to bruteforce
- `hydra -l gloria -P wordlist_35.txt venus.hackmyvm.eu -s 5000 -t 4 ssh`
    - `l` takes a single user parameter
    - `P` takes the password wordlist
    - `s` takes the port number
    - `t` specifies the number of threads, 4 is recommended
- it might take a while

***

# Mission 36

![84](images/84.png)