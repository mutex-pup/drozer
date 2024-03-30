FROM alpine:3.19.1 as builder
RUN apk add --no-cache \
		openjdk11-jdk \
		python3-dev \
		git \
		py3-pip \
		py3-openssl \
		py3-twisted \
		py3-yaml \
		protobuf-dev \
		bash \
		gcc \
		py3-wheel && \
	pip install --no-cache-dir --break-system-packages \
		protobuf==4.25.2 \
		distro && \
	git clone https://github.com/WithSecureLabs/drozer/ /tmp/drozer && \
	cd /tmp/drozer && \
	python setup.py bdist_wheel

FROM alpine:3.19.1
RUN --mount=target=/builder,from=builder,source=/tmp/drozer/dist apk add --no-cache \
		openjdk11-jre-headless \
		python3 \
		bash \
		musl-dev \
		gcc \
		python3-dev \
		libffi-dev \
		py3-pip && \
	pip install --no-cache-dir --break-system-packages \
		pyOpenSSL \
		service_identity \
		twisted \
		pyyaml \
		protobuf==4.25.2 \
		distro && \
	pip install /builder/drozer*.whl --no-cache-dir --break-system-packages && \
	apk del --purge --no-cache \
		py3-pip \
		gcc \
		bash \
		musl-dev \
		python3-dev \
		libffi-dev \
		alpine-baselayout \
		alpine-keys \
		libc-utils \
		apk-tools && \
	rm -rf /root \
		/etc/apk \
		/lib/apk \
		/usr/share/apk \
		/var/lib/apk \
		/usr/lib/python3.11/ensurepip
ENTRYPOINT ["drozer"]
