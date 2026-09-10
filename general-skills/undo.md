# Undo - picoCTF General Skills

## Challenge Description
The challenge gives an encoded string and hints that it has been through multiple transformations that need to be reversed.

## Approach
The first hint given was it's encoded as base64. So, first command was `base64 -d`.
After first decoding, the hint suggested it to be in reversed order, so command used is `rev`.
The third step hint suggested to replace dashes with underscores.` [Command: tr '-' '_']`
The fourth step was similar, where parenthesis was replaced with curly braces.` [Command: tr '()' '{}']` tr uses char by char
The fifth and final hint was to use rot13, which was a cipher text, of key 13. The command was given at hint, which was: ` tr 'a-zA-Z' 'n-za-mN-ZA-M'`
Which replaces the a-z lowercase to n-z - a-m and same for uppercase.
This revealead the flag.


## Flag

`picoCTF{...redacted}`
