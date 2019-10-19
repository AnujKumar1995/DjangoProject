# base image
FROM node:latest as build-deps


# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH app/node_modules/.bin:$PATH

COPY package.json .

# install and cache app dependencies
RUN npm install --silent
RUN npm audit fix
RUN npm install react-scripts@3.0.1 -g --silent
RUN npm install -g serve 
RUN npm i browserslist

COPY . .
# start app
CMD ["npm", "run","start","yarn","serve"]

RUN adduser --disabled-login user
USER user
