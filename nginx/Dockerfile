FROM nginx:1.20.2-alpine

RUN rm /etc/nginx/nginx.conf /etc/nginx/conf.d/default.conf

COPY default.conf /etc/nginx/conf.d/

EXPOSE 443

CMD [ "NGINX", "-g", "demon off;" ]