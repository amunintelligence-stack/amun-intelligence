# ACI backend on Hugging Face Spaces (Docker) — wipe-proof deploy.
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    ACI_DB_PATH=/app/data/aci.db

# System recon tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    nmap whois dnsutils sqlmap git curl ca-certificates unzip \
    && rm -rf /var/lib/apt/lists/*

# Go recon binaries (static, pinned versions)
RUN mkdir -p /tmp/gb /usr/local/bin && cd /tmp/gb && \
    curl -sL -o subfinder.zip https://github.com/projectdiscovery/subfinder/releases/download/v2.17.0/subfinder_2.17.0_linux_amd64.zip && \
    curl -sL -o httpx.zip https://github.com/projectdiscovery/httpx/releases/download/v1.12.0/httpx_1.12.0_linux_amd64.zip && \
    curl -sL -o nuclei.zip https://github.com/projectdiscovery/nuclei/releases/download/v3.11.1/nuclei_3.11.1_linux_amd64.zip && \
    curl -sL -o amass.tgz https://github.com/owasp-amass/amass/releases/download/v5.1.1/amass_linux_amd64.tar.gz && \
    curl -sL -o ffuf.tgz https://github.com/ffuf/ffuf/releases/download/v2.3.0/ffuf_2.3.0_linux_amd64.tar.gz && \
    curl -sL -o gobuster.tgz https://github.com/OJ/gobuster/releases/download/v3.8.2/gobuster_Linux_x86_64.tar.gz && \
    curl -sL -o naabu.zip https://github.com/projectdiscovery/naabu/releases/download/v2.6.1/naabu_2.6.1_linux_amd64.zip && \
    curl -sL -o dnsx.zip https://github.com/projectdiscovery/dnsx/releases/download/v1.3.1/dnsx_1.3.1_linux_amd64.zip && \
    curl -sL -o tlsx.zip https://github.com/projectdiscovery/tlsx/releases/download/v1.4.0/tlsx_1.4.0_linux_amd64.zip && \
    curl -sL -o katana.zip https://github.com/projectdiscovery/katana/releases/download/v1.8.0/katana_1.8.0_linux_amd64.zip && \
    curl -sL -o phoneinfoga.tgz https://github.com/sundowndev/phoneinfoga/releases/download/v2.11.0/phoneinfoga_Linux_x86_64.tar.gz && \
    curl -sL -o waybackurls.tgz https://github.com/tomnomnom/waybackurls/releases/download/v0.1.0/waybackurls-linux-amd64-0.1.0.tgz && \
    for f in *.zip; do unzip -o -q "$f"; done && \
    for f in *.tgz; do tar xzf "$f"; done && \
    cp subfinder httpx nuclei ffuf gobuster naabu dnsx tlsx katana phoneinfoga waybackurls /usr/local/bin/ && \
    cp amass_linux_amd64/amass /usr/local/bin/ && \
    chmod +x /usr/local/bin/subfinder /usr/local/bin/httpx /usr/local/bin/nuclei \
             /usr/local/bin/amass /usr/local/bin/ffuf /usr/local/bin/gobuster \
             /usr/local/bin/naabu /usr/local/bin/dnsx /usr/local/bin/tlsx \
             /usr/local/bin/katana /usr/local/bin/phoneinfoga /usr/local/bin/waybackurls && \
    cd / && rm -rf /tmp/gb

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install "setuptools<81"

COPY app.py console.html ./
COPY static ./static
RUN mkdir -p /app/data

EXPOSE 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860", "--workers", "1"]
