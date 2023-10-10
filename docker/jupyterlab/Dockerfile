FROM spark:3.4.2-hadoop-3

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install ffmpeg \
                       libsm6 \
                       libxext6 \
                       git \
                       make \
                       bash-completion \
                       sudo
RUN apt-get -y autoclean && \
    apt-get -y autoremove

RUN pip install --upgrade setuptools \
                          wheel

ENV PYSPARK_PYTHON=/usr/bin/python
                          
WORKDIR /opt/jupyterlab
RUN cd /opt/jupyterlab
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir 
RUN rm -rf /opt/jupyterlab/requirements.txt

# RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz && \
#     wget https://downloads.apache.org/hadoop/common/hadoop-3.3.4/hadoop-3.3.4.tar.gz.sha512 && \
#     shasum -a 512 hadoop-3.3.4.tar.gz && \
#     tar -xzvf hadoop-3.3.4.tar.gz && \
#     mv hadoop-3.3.4 /usr/local/hadoop && \
#     echo "export JAVA_HOME = $JAVA_HOME" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh



CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]