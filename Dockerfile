FROM python:3.8.3

COPY ./ /opt/osutext
WORKDIR /opt/osutext
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]
