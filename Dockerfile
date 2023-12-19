FROM python:3.10.8
WORKDIR /app
COPY ./RestyApp.py /app/
COPY req.txt /app/
EXPOSE 5000
RUN pip3 install -r req.txt
ENTRYPOINT ["python3","RestyApp.py"]