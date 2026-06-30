FROM python
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
RUN mkdir /data
CMD [ "python", "flask4.py" ]
