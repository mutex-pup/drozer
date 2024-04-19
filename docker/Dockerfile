FROM alpine:3.19.1 as builder
ADD "https://api.github.com/repos/WithSecureLabs/drozer/commits?per_page=1" latest_commit
RUN apk add --no-cache \
		openjdk11-jdk \
		python3-dev \
		py3-pip \
		py3-openssl \
		py3-twisted \
		py3-yaml \
		py3-distro \
		py3-service_identity \
		protobuf-dev \
		bash \
		gcc \
		py3-wheel && \
	wget https://github.com/WithSecureLabs/drozer/archive/refs/heads/develop.zip -O drozer.zip && \
	unzip drozer.zip && \
	mv drozer*/ drozer/ && \
	cd drozer && \
	pip install --no-cache-dir --break-system-packages \
		-r requirements.txt && \
	python setup.py bdist_wheel

FROM alpine:3.19.1
RUN --mount=target=/builder,from=builder,source=/drozer apk add --no-cache \
		openjdk11-jre-headless \
		python3 \
		py3-openssl \
		py3-twisted \
		py3-distro \
		py3-service_identity \
		py3-yaml \
		py3-pip && \
	pip install /builder/dist/drozer*.whl --no-cache-dir --break-system-packages && \
	apk del --purge --no-cache \
		py3-pip
ENTRYPOINT ["drozer"]
