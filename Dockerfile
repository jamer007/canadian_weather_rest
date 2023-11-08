FROM python:3.11-bookworm
# create the app user
RUN addgroup --system jamer007 && adduser --system --group jamer007
# create the appropriate directories
ENV HOME=/home/jamer007
ENV APP_HOME=/home/jamer007/app
RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME/src
# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt
# copy project
ADD src/ $APP_HOME/src/
# chown all the files to the app user
RUN chown -R jamer007:jamer007 $APP_HOME
# change to the app user
USER jamer007
# run entrypoint
ENTRYPOINT ["python3", "main.py"]
