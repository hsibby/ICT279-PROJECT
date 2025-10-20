#!/usr/bin/env bash
# Simple Apache HTTPD 2.4.59 setup from source
# Usage: sudo bash setup-httpd-2.4.59.sh

set -e

# Install dependencies
apt update
apt install -y build-essential libpcre3 libpcre3-dev libapr1-dev libaprutil1-dev openssl libssl-dev wget tar curl

# Remove apache2 if installed
apt remove -y apache2
apt autoremove -y


# Download and extract HTTPD
wget https://archive.apache.org/dist/httpd/httpd-2.4.59.tar.gz
tar -xvzf httpd-2.4.59.tar.gz
cd httpd-2.4.59

# Configure and install
./configure --enable-so --enable-rewrite --enable-headers --prefix=/usr/local/apache2
make
make install

# Test installation
/usr/local/apache2/bin/apachectl start

# Verify Apache version after installation
echo "Verifying Apache installation and version..."
APACHE_VERSION=$(/usr/local/apache2/bin/httpd -v | head -n 1)
echo "Installed: $APACHE_VERSION"

sleep 5
if curl -I hhost | grep "200 OK"; then
    echo "Apache HTTPD 2.4.59 installed and running successfully."
else
    echo "Failed to start Attp://localpache HTTPD."
    exit 1
fi

