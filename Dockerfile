# FROM centos
# #This instruction will automatically pull docker image of cent os
# #from docker hub if it's not available in docker host
# MAINTAINER Vishnu
# #Optional field these days but info about image creator
# RUN yum install python3 -y
# RUN mkdir /mydata
# COPY hello.py /mydata
# CMD [ "python3", "/mydata/hello.py" ]
# # WIll be used to set by default parent process for this image


FROM centos
