# ICT279 PROJECT

Web Server
Name: webserver
Username: emp
Passwrod: 

### Apache HTTPD 2.4.59 Installation

This project includes an automated script to install Apache HTTPD 2.4.59 from source on Ubuntu/Debian systems.

#### Prerequisites
- Ubuntu/Debian Linux system
- Root or sudo access
- Internet connection for downloading packages and source code

#### Quick Start
1. **Clone the repository:**
   ```bash
   git clone https://github.com/hsibby/ICT279-PROJECT.git
   cd ICT279-PROJECT
   ```

2. **Make the script executable:**
   ```bash
   chmod +x setup-httpd-2.4.59.sh
   ```

3. **Run the installation script:**
   ```bash
   sudo bash setup-httpd-2.4.59.sh
   ```

#### What the Script Does
- Installs required build dependencies
- Downloads Apache HTTPD 2.4.59 source code
- Compiles and installs Apache with essential modules
- Verifies the installation and version
- Tests that Apache is responding on localhost
- Provides detailed installation summary

#### After Installation
- **Access your web server:** http://localhost
- **Apache binary:** `/usr/local/apache2/bin/httpd`
- **Configuration file:** `/usr/local/apache2/conf/httpd.conf`
- **Document root:** `/usr/local/apache2/htdocs/`
- **Start/Stop Apache:** `/usr/local/apache2/bin/apachectl {start|stop|restart}`

#### CVE-2024-38475 Vulnerability Demonstration
This project includes a complete demonstration of **CVE-2024-38475**, a critical vulnerability in Apache mod_rewrite:

- **`vulnerable-httpd-2.4.59.conf`** - Vulnerable Apache configuration
- **`cve-2024-38475-demo.sh`** - Vulnerability demonstration script  
- **`test-cve-2024-38475.sh`** - Automated vulnerability testing
- **`cve-2024-38475-poc.py`** - **Python PoC script for automated testing**
- **`poc-examples.py`** - Interactive examples for using the Python PoC
- **`requirements.txt`** - Python dependencies
- **`CVE-2024-38475-README.md`** - Detailed vulnerability documentation

**Python PoC Usage:**
```bash
# Install dependencies
pip3 install -r requirements.txt

# Basic test
python3 cve-2024-38475-poc.py -u http://localhost

# Verbose output with custom files
python3 cve-2024-38475-poc.py -u http://localhost -v -f etc/passwd,etc/shadow

# Generate detailed report
python3 cve-2024-38475-poc.py -u http://localhost -o report.txt

# Interactive examples
python3 poc-examples.py
```

**⚠️ WARNING**: The vulnerability files are for educational purposes only. Never use in production!

#### Troubleshooting
- Ensure you have sudo privileges
- Check that port 80 is not being used by another service
- Review the script output for any error messages
- Check Apache logs: `/usr/local/apache2/logs/error_log`
