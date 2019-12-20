## Docker Proxy ##

This is an example of a Docker's proxy configuration file in Ubuntu.
Sometimes we need to deploy docker applications in environments where we don't have a direct internet connection. In this situation, won't be enough to configure a global proxy in the host but configure Docker Proxy with its exemptions instead. Those exemptions are intended to avoid unnecessary external connections with internal containers.
Here is an example of "/root/.docker/config.json"

```json
{
	"proxies": {
		"default": {
			"httpProxy": "http://172.24.244.241:3128",
			"httpsProxy": "http://172.24.244.241:3128",
			"noProxy": "172.24.244.81, 172.24.244.82, 172.24.244.83, some-internal-url.com, another-internal-url.net, postgres"
		}
	}
}

```
Note: Since you're not connected to internet, the system's time could be wrong. To  solve this, you can add the proxy details to the host's apt configuration adding a new file and running the following commands:
```bash

sudo vim /etc/apt/apt.conf.d/proxy.conf
Acquire {
  HTTP::proxy "http://172.24.244.241:3128";
  HTTPS::proxy "http://172.24.244.241:3128";
}

sudo apt-get update

sudo apt-get install ntp ntpdate

Config the ntp server:
sudo vim /etc/ntp.conf

Add the next line to the ntp.conf file under "# Specify one or more NTP servers." section:
server [YOUR_NTP_SERVER]

Restart the ntp daemon:
sudo /etc/init.d/ntp restart

Check ntp synchronization (Can take a while):
ntpq -pn

```
