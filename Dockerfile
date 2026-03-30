FROM python
WORKDIR /dest
COPY . /dest
EXPOSE 5000
CMD [ "python" "sample.py" ]
