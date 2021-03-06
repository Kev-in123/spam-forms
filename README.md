# **DISCLAIMER: THIS REPOSITORY IS FOR EDUCATIONAL PURPOSES ONLY AND IS NOT INTENDED TO PROMOTE ANY ILLEGAL ACTIVITIES. I WILL NOT BE HELD RESPONSIBLE FOR ANY MISUSE OF THE INFORMATION PROVIDED.**
-----------------------------------------
# User Guide

In `main.py` theres a part that says `form-id` below is an image that shows the id you need   
![image](https://user-images.githubusercontent.com/75402062/145698709-b009a865-2421-47d7-b786-7a6db154144c.png)

A few notes when using this:

1. There isn't a `limit to 1 response` on the form   
2. If all the questions are optional, you can leave the `data` dictionary blank    
3.
      a) (easier method) Fill in the form at least once and fetch the data from the request   
      <img src="https://user-images.githubusercontent.com/75402062/145698738-92ce1f0e-6097-40bd-90b1-25c17611239f.png" width="750"><br>
      b) (more time-consuming method)
     1. Open the inspector and navigate to the network tab  
     <img src="https://user-images.githubusercontent.com/75402062/165862373-782ba36c-fe13-4afe-8ad9-08a293d682b9.png" width="750"><br>
     2. Fill in the field to the question  
     <img src="https://user-images.githubusercontent.com/75402062/165862825-ccadbb3e-8e9b-48ad-96c5-6d3cf2c3bae6.png" width="750"><br>
     3. A few requests should pop up, look for one with `200` for it's status and a `POST` method  
     4. On the side, navigate to where it says request  
     5. Collect the corresponding id  
     <img src="https://user-images.githubusercontent.com/75402062/165862879-ae0d8d06-a4c2-4b70-b3da-239f87898c94.png" width="750"><br>
     6. Repeat for every field

for the `data` dictionary, you just paste in the values
 
 e.g.
 ```py
 
 data = {
  "entry.1234567890": "lol"
 }
 ```

Also, you can use the same method for any form/POST request :)


If you don't want to spam the form, you can remove threading and the while loop
