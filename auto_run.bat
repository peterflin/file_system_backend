docker stop file_system
docker rm file_system
docker rmi asbeas2323/file_system:1.0
docker build -t asbeas2323/file_system:1.0 .
docker run -dit -p 8010:8000 --name file_system asbeas2323/file_system:1.0
