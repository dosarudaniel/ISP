# Homework 7

`sudo docker run --rm -p 8080:8000 --name hw7 com402/hw7`   

To open a bash: (to check solution of part 2)   
`sudo docker exec -it hw7 sh`    


`python3 client.py` # HW7    


## Part 2   

`f(x) = w0 + w * x.T`   
     
send 11 queries:     
 for `w0`, x should be `[0, 0, 0,..0]` (len(x) == 10)   
 for `w1`, x should be `[1, 0, 0,..0]` (len(x) == 10)    
.   
.   
.   
 for `w10`, x should be `[0, 0, 0,..,0,1]` (len(x) == 10)   

See python code for Pailler crypto library usage. 
