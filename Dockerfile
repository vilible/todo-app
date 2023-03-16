FROM python:3.11.2-alpine

WORKDIR /todo-app

COPY requirements.txt ./
COPY src ./

RUN pip install -r requirements.txt

CMD [ "python", "main.py" ]
EXPOSE 5000