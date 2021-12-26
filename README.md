# **DISCLAIMER: THIS REPOSITORY IS FOR EDUCATIONAL PURPOSES ONLY AND IS NOT INTENDED TO PROMOTE ANY ILLEGAL ACTIVITIES. I WILL NOT BE HELD RESPONSIBLE FOR ANY MISUSE OF THE INFORMATION PROVIDED.**
-----------------------------------------
# User Guide

In `main.py` theres a part that says `form-id` below is an image that shows you how to get it   
![image](https://user-images.githubusercontent.com/75402062/145698709-b009a865-2421-47d7-b786-7a6db154144c.png)

A few notes when using this:

1. There isn't a `limit to 1 response` on the form   
2. If all the questions are optional, you can leave the `data` dictionary blank
3. To fill the `data` dictionary, you need to fill in the form at least once and fetch the data from the request  
![image](https://user-images.githubusercontent.com/75402062/145698738-92ce1f0e-6097-40bd-90b1-25c17611239f.png)
in the above image, you see a field that says `entry.1079835443	"Option+1"`, all you need to do is to copy that field (if there are more questions, copy all the `entry` fields and the values) and add it to the dictonary while making them strings  
 
 
 e.g.
 ```py
 data = {
  "entry.1079835443": "Option+1"
 }
 ```
