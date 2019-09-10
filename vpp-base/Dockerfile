FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
		apt-transport-https \
		ca-certificates \
		curl \
		gnupg \
		iproute2 \
		iputils-ping \
		linux-tools-common \
		linux-tools-4.4.0-161-generic \
		linux-cloud-tools-4.4.0-161-generic \
		nano \
		linux-tools-generic \
 	&& rm -rf /var/lib/apt/lists/*

ARG REPO
ARG VPP_VERSION

WORKDIR /vpp

COPY get-vpp.sh /get-vpp.sh

RUN set -eux; \
	/get-vpp.sh; \
	apt-get update && apt-get install -y -V ./*.deb; \
	dpkg-query -f '${Version}\n' -W vpp > /vpp/version; \
	rm -rf /var/lib/apt/lists/*;

RUN mkdir -p /var/log/vpp


