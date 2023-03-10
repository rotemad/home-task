FROM python:3.10-slim
RUN pip3 install requests && mkdir /rickandmortyapi
ADD main.py /rickandmortyapi
WORKDIR /rickandmortyapi
RUN python main.py