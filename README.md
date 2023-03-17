> # 📝 TODO App
> 
> Simple TODO application writen in Flask (Python framework).  
> Functionalities:  
> - ➕ Adding
> - ✖️ Editing
> - ➖ Deleting

> ## 🐋 How to run it in Docker?
> First, you need to build a Docker image. To do so, go to project folder and run this command:
> ```
> $ docker build -t YOUR-IMAGE-NAME .
> ```
> Great! You've just build a Docker Image! Now you can run your container:
> ```
> $ docker run -p YOUR-FREE-PORT:5000 YOUR-IMAGE-NAME
> ```