FROM python:3.6
RUN apt-get install bash
RUN pip install nbconvert==5.6.0 notebook==5.6.0 "pelican[markdown]" pelican-jupyter ghp-import
WORKDIR /caverna