FROM python:3.7.6

# Create app directory
WORKDIR /usr/src/app
ADD . /usr/src/app

# Install app dependencies
RUN pip install -r requirements.txt


EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
