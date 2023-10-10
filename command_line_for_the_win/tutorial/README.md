
<img src="https://aceworldpub.com.ng/wp-content/uploads/2022/03/unnamed.png" width="200" height="100"> <img src="https://upload.wikimedia.org/wikipedia/commons/4/4b/Bash_Logo_Colored.svg" width="200" height="90"> 


# Command line for the win


## # How to use SFTP Commands to Copy Files to/from a Server

1- In your local machine, where you uploaded your files, copy the path for the 3 screenshots, we'll need it to step further

2- Open your sandbox fia SFTP (secure file transfer protocol) 

3- Copy the SFTP provided by your intranet account, paste it in your terminal, do the same with password
		![Untitled.png](https://github.com/MASMIYEN/alx-system_engineering-devops/blob/master/command_line_for_the_win/tutorial/Untitled.png?raw=true)
NOTE: You ll be connected to your sandbox via SFTP, so we ll be able to transfer files to our server(sandbox)
		![Untitled1.png](https://github.com/MASMIYEN/alx-system_engineering-devops/blob/master/command_line_for_the_win/tutorial/Untitled1.png?raw=true)
 
 Now lets access to the directory where we're supposed to transfer our files using **cd** command for in this project it's :
   

     /root/alx-system_engineering-devops/command_line_for_the_win/

   
 ![pwd.png](https://github.com/MASMIYEN/alx-system_engineering-devops/blob/master/command_line_for_the_win/tutorial/pwd.png?raw=true)
 *Don't mind that I already uploaded my files, but I ll give an example with a test file* 

Now lets copy the path of our files from our localmachine, our test files is **test.txt**
Now as you see in file properties, Parent folder is the PATH for our file 
After copying make sure the line you re copying is like this for example

    /home/marouane/alx/commandline-challenge/test.txt


![path file.png](https://github.com/MASMIYEN/alx-system_engineering-devops/blob/master/command_line_for_the_win/tutorial/path%20file.png?raw=true) 

Now lets use a command called **put** which its used to upload a file, then you'll notice that the file is uploaded
You can use **ls** command to check if the file is uploaded 
![put.png](https://github.com/MASMIYEN/alx-system_engineering-devops/blob/master/command_line_for_the_win/tutorial/put.png?raw=true)

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/324/06AChAO.png)

## Background Context

[CMD CHALLENGE](https://intranet.alxswe.com/rltoken/a83_NOBEtXgFr1Yqej0HYA "CMD CHALLENGE")  is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

**References :**

-   [SFTP Guide](https://intranet.alxswe.com/rltoken/OwMT_ctWdMI7L6JFzLvVKQ "SFTP Guide")
-   [SFTP File Transfer Tutorial](https://intranet.alxswe.com/rltoken/aTKBzKWZ5EI-qZjJVblUzg "SFTP File Transfer Tutorial")

**Here are the steps to follow:**

-   Take the  `screenshots`  of the completed levels as mentioned in the  `general`  requirements.
-   Open a terminal or command prompt on your local machine.
-   Use the  `SFTP command-line tool`  to establish a connection to the sandbox environment. You will need the  `hostname`,  `username`, and  `password`  provided to you for the sandbox environment.
-   Once connected, navigate to the  `directory`  where you want to upload the  `screenshots`.
-   Use the SFTP  `put`  command to upload the  `screenshots`  from your local machine to the sandbox environment.
-   Confirm that the  `screenshots`  have been successfully transferred by checking the sandbox directory.
-   Once the  `screenshots`  are transferred, you can proceed to push the  `screenshots`  to  `GitHub`  as mentioned in the initial requirements.
-   Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.

#### NOTE :

-   The screenshoots of completed level should be inside the dir  `/root/alx-system_engineering-devops/command_line_for_the_win/`
