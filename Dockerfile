FROM python:3.10 as tests

# Install Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get update && apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN apt-get install python3-dev -y


# Inslate Allure CLI
# See https://github.com/allure-framework/allure-debian/issues/9
RUN apt-get update && apt-get install -y wget default-jdk && cd /opt && \
    (wget -c https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.16.0/allure-commandline-2.16.0.tgz -O - | tar -xz && chmod +x allure-2.16.0/bin/allure)
ENV PATH="${PATH}:/opt/allure-2.16.0/bin"

# Hack: link allure installation under a path Jenkins plugin expects it.
ENV __JENKINS_ALURE_PATH="/root/tools/ru.yandex.qatools.allure.jenkins.tools.AllureCommandlineInstallation"
RUN mkdir -p $__JENKINS_ALURE_PATH && ln -s /opt/allure-2.16.0 $__JENKINS_ALURE_PATH/._allure

RUN mkdir /Typhon
WORKDIR /Typhon

ADD . /Typhon

RUN pip install --upgrade pip && \
    pip install virtualenv && \
    virtualenv --python=/usr/bin/python3 /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install -r requirements.txt --quiet



CMD . /opt/venv/bin/activate && sh scripts/execute_docker_tests.sh