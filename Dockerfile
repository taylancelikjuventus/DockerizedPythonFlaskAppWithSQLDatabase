FROM python:3.8.3

WORKDIR /myapp2
COPY . /myapp2

RUN pip install flask==1.1.2
RUN pip install -r requirements.txt


ENTRYPOINT ["python"]
CMD ["app.py"]