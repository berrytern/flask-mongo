# Docker comands to run properly

## Mongodb container
sudo docker pull mongo:4.0.4<br/>
sudo docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4

## Flask container
###### go to into Dockerfile path

sudo docker build -t flask .<br/>
sudo docker run -it --name flask --link mongodb -dp 3000-3002:3000-3002 flask

##### Check if all is running
sudo docker ps<br/>
sudo docker ps -a