FROM python:3.10.8
WORKDIR /app
COPY ./HealthyApp.py /app/
COPY req.txt /app/
EXPOSE 4000
ENV token=''
RUN pip3 install -r req.txt
ENTRYPOINT ["python3","HealthyApp.py"]