FROM pchuang0219/accton_tms_frontend_service:base
LABEL MAINTAINER Anber Huang <anber_huang@accton.com>

ADD . /web
WORKDIR /web

RUN apt-get -y update
RUN apt-get -y upgrade
RUN usermod -aG www-data root
RUN ln -s environment/nginx-app.conf /etc/nginx/sites-enabled/

RUN pip3 install --upgrade pip
RUN pip3 install -r environment/requirements.txt

ENV LANG='en_US.utf8'
ENV LC_ALL='en_US.utf8'

COPY environment/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 8000
CMD ["/usr/bin/supervisord","-n"]