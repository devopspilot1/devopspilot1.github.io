---
title: "How to configure free Let’s Encrypt SSL/TLS Certificates with NGINX and auto renew certificates"
date: 2024-07-01
---

### Prerequisites

- Have NGINX or NGINX Plus installed.

- Own or control the registered domain name for the certificate.

- Create a DNS record that associates your domain name and your server’s public IP address.

### What is certbot

Certbot is a agent for letsencrypt that runs in a server to complete the letsencrypt challenge, request a certificate and get a certificate.

### What is Letsencrypt challenge

Letsencrypt want to verify that you own the domain. So using certbot it will host some files in `/.well-known/acme-challenge/` folder and serve this files publicly using nginx webserver.

Once it verifies the files, the challenge is completed and it will issue the certificate for the requested domain.

### How to install cerbot

```
sudo apt-get update
sudo apt-get install certbot
sudo apt-get install python3-certbot-nginx
```

### Configure DNS record in Domain registrar

www.devopspilot.tk --> IP-address

### Configure Nginx

Remove the default configuration file in nginx

```
sudo rm -f /etc/nginx/sites-enabled/default
```

Create new config file `devopspilot.tk.conf` in `/etc/nginx/conf.d/` folder and put the following content

`Info:` Configuration file name can be anything

```
sudo vi /etc/nginx/conf.d/devopspilot.tk.conf
```

Replace `devopspilot.tk` with your domain name in config file

```
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name www.devopspilot.tk;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

Run the following command to check for syntax error in conf file

```
sudo nginx -t
```

`Output :`

```
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

Run the following command to reload the nginx webserver

```
nginx -s reload
```

Change the `devopspilot.tk` to your domain name and run the below command.

It will complete the letsencrpt challenge, generate the certificate and map the certificate path in `devopspilot.tk.conf` conf file

```
sudo certbot --nginx -d www.devopspilot.tk
```

It will ask for email address, agree the terms and conditions, certificate will be issued and finally enter `2` to automatically redirect `http` to `https`

![letsencrypt](../../images/generate-ssl1.png)

![letsencrypt](../../images/generate-ssl2.png)

Check the nginx conf file `/etc/nginx/conf.d/devopspilot.tk.conf` which was updated by certbot

Now the nginx conf file looks like below.

```
server {
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name www.devopspilot.tk;

    location / {
        try_files $uri $uri/ =404;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/www.devopspilot.tk/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/www.devopspilot.tk/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot

}
server {
    if ($host = www.devopspilot.tk) {
        return 301 https://$host$request_uri;
    } # managed by Certbot

    listen 80 default_server;
    listen [::]:80 default_server;

    server_name www.devopspilot.tk;
    return 404; # managed by Certbot

}
```

Wait for couple of minutes.

Go to browser and type the domain name `devopspilot.tk`

![letsencrypt](../../images/nginx.png)

Now it will automatically redirect to `https://www.devopspilot.tk`

Now lets see how to automatically renew the certificates.

Letsencrypt certificates will expire after 3 months.

Create a cron job with `certbot renew` command. This job will daily run at 12 AM and check whether certificates are going to expire or not.

If it is going to expire it will regenerate the certificate and map the new certificate path in nginx conf file

Run the following command to create a cron job.

```
crontab -e
```

After running the `crontab -e` command it will open a file, type the below command and save the file.

```
0 12 * * * /usr/bin/certbot renew --quiet
```

Hurray! we have successfully configured the SSL/TLS certificate in nginx webserver.

### Reference:

- [How to install nginx](../../webserver/nginx/how-to-install-nginx.md)
