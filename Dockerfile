FROM python:latest


WORKDIR /flask_skeleton
COPY . /flask_skeleton
RUN cd /flask_skeleton

RUN pip install -r requirements.txt 
EXPOSE 8091

CMD [ "python","/flask_skeleton/run.py" ] 

