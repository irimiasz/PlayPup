FROM node:19.7.0

WORKDIR /code

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . .
