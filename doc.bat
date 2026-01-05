docker stop flask-container
docker rm flask-container
docker build --no-cache -t ehtisham1337/flask-app .
docker run -d -p 5000:5000 --name flask-container ehtisham1337/flask-app
docker logs flask-container