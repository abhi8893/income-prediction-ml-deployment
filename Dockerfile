FROM continuumio/anaconda3:latest
COPY . /usr/app
WORKDIR /usr/app
RUN pip install -r requirements.txt
RUN python setup.py install
CMD python flask_app.py