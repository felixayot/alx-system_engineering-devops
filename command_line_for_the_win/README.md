# Command line for the win
This is an awesome challenge provided by the ALX Holberton Software Engineering School to be completed as an optional project for the curriculum.

## Background Context
[CMD CHALLENGE](https://cmdchallenge.com) is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

I tested my Bash skills that I had already learnt earlier in the program on a series of random tests(about 30 and counting) and I got to learn even more skills that can be very handy in System DevOps projects.

## SFTP (Secure File Transfer Protocol) command-line tool
Secure File Transfer Protocol (SFTP) is a network protocol for securely accessing, transferring and managing large files and sensitive data.

In addition to completing the project tasks and submitting the required screenshots to GitHub, I was tasked to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move my local screenshots to the sandbox environment.

**Here are the steps I took to achieve just that:**
- I had my `.png` screenshot files in my local machine which I could easily access using my `Ubuntu 20.04 LTS` terminal. In my ALX hosted sandbox environment, I'm provided with a `hostname`, `username`, and `password` to initiate SFTP command-line tool in my local terminal. Once SFTP is launched, I now have a secure connection to the sandbox environment.
- I had to learn a few `sftp` commands on the `man page` using `?` command. I used the usual shell commands `mkdir`, `cd`, `ls` to navigate to `/root/alx-system_engineering-devops/command_line_for_the_win/` folder in the remote sandbox environment. This is where I transferred the screenshots from my local machine.
- In `sftp command-line tool`, I'm able to access my directories in the local machine as well using these commands: `lcd`, `lls` and so forth. I used these to get to the folder that had my screenshots. From here I used the `put` command to upload these screenshots(`0-first_9_tasks.png`, `1-next_9_tasks.png` and `2-next_9_tasks.png`) to my remote sandbox in the designated folder.
- I confirmed the transfer was successful using the `ls` command which lists the uploaded `.png` files.
- After that, I proceeded accordingly with the usual upload to the remote Github repository. I also learnt the `get` sftp command used to download remote files from the server host to my local terminal.

```
ayot@DESKTOP-f_ayot:~/ayot/temp_folder$ sudo sftp 34cf755b46be@34cf755b46be.73f706bd.alx-cod.online
[sudo] password for ayot:
34cf755b46be@34cf755b46be.73f706bd.alx-cod.online's password:
Connected to 34cf755b46be.73f706bd.alx-cod.online.
sftp> ls
0x03-git        alx-pre_course  alx-zero_day    bin             boot            dev             etc             home            lib             lib32
lib64           libx32          media           mnt             opt             proc            root            run             sbin            srv
sys             tmp             usr             var
sftp> cd root
sftp> ls
0x01_emacs                       0x02_vi                          alx-pre_course                   alx-system_engineering-devops    new_school
school                           school_is_amazing
sftp> cd alx-system_engineering-devops
sftp> ls
0x00-shell_basics                0x01-shell_permissions           0x02-shell_redirections          0x03-shell_variables_expansions  README.md
command_line_for_the_win
sftp> cd command_line_for_the_win
sftp> lls
0-first_9_tasks.png  1-next_9_tasks.png  2-next_9_tasks.png
sftp> put *.png
Uploading 0-first_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/0-first_9_tasks.png
0-first_9_tasks.png                                                                                                                   100%  159KB 125.1KB/s   00:01
Uploading 1-next_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/1-next_9_tasks.png
1-next_9_tasks.png                                                                                                                    100%  107KB 126.7KB/s   00:00
Uploading 2-next_9_tasks.png to /root/alx-system_engineering-devops/command_line_for_the_win/2-next_9_tasks.png
2-next_9_tasks.png                                                                                                                    100%  110KB 145.8KB/s   00:00
sftp> ls
0-first_9_tasks.png  1-next_9_tasks.png   2-next_9_tasks.png
sftp> lpwd
Local working directory: /home/ayot/temp_folder
sftp> pwd
Remote working directory: /root/alx-system_engineering-devops/command_line_for_the_win
sftp> exit
ayot@DESKTOP-f_ayot:~/ayot/temp_folder$
```

## Author
- ***Felix Ayot*** < @felixayot >

## Resources
- ALX SE program provided a brief guidance on navigation of `SFTP command-line tool`.
- I also got some very helpful insights from [TechTarget](https://www.techtarget.com/searchcontentmanagement/definition/Secure-File-Transfer-Protocol-SSH-File-Transfer-Protocol) and [YouTube](https://www.youtube.com/watch?v=22lBJIfO9qQ).
