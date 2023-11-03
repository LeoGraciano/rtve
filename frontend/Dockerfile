# Build
FROM node:20-alpine as build

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY ./frontend/package*.json ./
RUN npm i --silent
COPY ./frontend ./
RUN npm run build

# Server
FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY ./frontend/docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000
COPY ./README.md /usr/share/nginx/html/

CMD ["nginx", "-g", "daemon off;"]