FROM python:3.8

RUN pip install ipython 	\
&& 	pip install pandas		\
&& 	pip install wordninja

WORKDIR /