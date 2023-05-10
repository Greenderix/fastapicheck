FROM python:3.9

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi/requirements.txt

RUN pip install fastapi uvicorn
#
COPY . /fastapi

#
#CMD ["uvicorn", "start:create_app", "--reload"]