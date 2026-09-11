# MY GIT General Skills

## Challenge Description
The README.md file hinted to push the flag as `root:root@picoctf`.
Which is in the format username:email.

## Approach
Command used to add user: `git config user.name "root"`.
Command used to add email: `git config user.email "root@picoctf"`
Following commands are used to push empty `flag.txt` file.
`git add flag.txt`
`git commit -m "Flag please"`
`git push`
The flag was given at the output of the `git push` command.

## Flag
`flag = picoCTF{1mp3rs0n4t4_g17_345y_06835333}`