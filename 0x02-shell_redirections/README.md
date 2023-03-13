![alx-system_engineering-devops](https://ci4.googleusercontent.com/proxy/IaJ94G7zio4xT5vx5a07ewkwcXeyZy4R2_cy_CIyIYiUsMoMo3j_qXTqrV8UOPGMBt_h-tdAaNq9E8NKp0aCTE1TCcGnSLV2HjnJQG5BLr88F-tbHCZo2JxredfT4t8ldfkGsWMT=s0-d-e1-ft#https://avatars.slack-edge.com/2022-02-03/3043433154022_fdf1362d6bd15d243ef3_88.png)

# 0x02-shell_redirections

##   Shell, I/O Redirection

-   What do the commands  `head`,  `tail`,  `find`,  `wc`,  `sort`,  `uniq`,  `grep`,  `tr`  do
-   How to redirect standard output to a file
-   How to get standard input from a file instead of the keyboard
-   How to send the output from one program to the input of another program
-   How to combine commands and filters with redirections

# Used scripts 

###  0. Hello World
a script that prints “Hello, World”, followed by a new line to the standard output.

###   1. Confused smiley :raised_eyebrow:

a script that displays a confused smiley **`"(Ôo)'`.**

###  2. Let's display a file
Display the content of the **`/etc/passwd`** file.

###  3. What about 2?
Display the content of **`/etc/passwd`** and **`/etc/hosts`**

###  4. Last lines of a file
Display the last 10 lines of **`/etc/passwd`**

###  5. I'd prefer the first ones actually
Display the first 10 lines of **`/etc/passwd`**

###  6. Line #2
a script that displays the third line of the file  **`iacta`.**
The file  **`iacta`**  will be in the working directory


###  7. It is a good file that cuts iron without making a noise
a shell script that creates a file named exactly **`\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)`** containing the text **`Best School`** ending by a new line.

###  8. Save current state of directory
a script that writes into the file **`ls_cwd_content`** the result of the command **`ls -la`.** If the file **`ls_cwd_content`** already exists, it should be overwritten. If the file **`ls_cwd_content`** does not exist, create it.

###  9. Duplicate last line
a script that duplicates the last line of the file **`iacta`**

### 10. No more javascript
a script that deletes all the regular files (not the directories) with a **`.js`** extension that are present in the current directory and all its subfolders.

### 11. Don't just count your directories, make your directories count
a script that counts the number of directories and sub-directories in the current directory.

-   The current and parent directories should not be taken into account  
-  Hidden directories should be counted

### 12. What’s new
a script that displays the 10 newest files in the current directory.
*Requirements:*
-   One file per line
-   Sorted from the newest to the oldest

### 13. Being unique is better than being perfect
a script that takes a list of words as input and prints only words that appear exactly once.
-   Input format: One line, one word
-   Output format: One line, one word
-   Words should be sorted

### 14. It must be in that file

Display lines containing the pattern *“root”* from the file **`/etc/passwd`**

### 15. Count that word
Display the number of lines that contain the pattern *“bin”* in the file **`/etc/passwd`**

### 16. What's next?
Display lines containing the pattern *“root”* and 3 lines after them in the file **`/etc/passwd`.**

### 17. I hate bins
Display all the lines in the file **`/etc/passwd`** that do not contain the pattern *“bin”.*

### 18. Letters only please
Display all lines of the file  **`/etc/ssh/sshd_config`**  starting with a letter.
-   include capital letters as well

### 19. A to Z
Replace all characters **`A`** and **`c`** from input to **`Z`** and **`e`** respectively.

### 20. Without C, you would live in hiago
a script that removes all letters **`c`** and **`C`** from input.

### 21. esreveR
a script that reverse its input.

### 22. DJ Cut Killer
a script that displays all users and their home directories, sorted by users.
-   Based on the the  **`/etc/passwd`**  file


