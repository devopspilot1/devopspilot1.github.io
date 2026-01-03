---
title: "How to configure free single Let’s Encrypt SSL/TLS wildcard Certificate with Nginx"
date: 2024-07-01
---

### Prerequisites

- Nginx web server up and running.

- Own or control the registered domain name for the certificate.

- Create a DNS record that associates your domain name and your server’s public IP address.

### What is certbot

Certbot is a agent for letsencrypt that runs in a server to complete the letsencrypt challenge, request a certificate and get a certificate.

### What is Letsencrypt challenge

Letsencrypt want to verify that you own the domain. So using certbot it will host some files in `/.well-known/acme-challenge/` folder and serve this files publicly using nginx webserver.

Once it verifies the files, the challenge is completed and it will issue the certificate for the requested domain.

### what is wildcard certificate

Wildcard certificate is a SSl/TLS certificate generated commonly for all subdomains.

If we dont know the subdomain to be used while generating the certificate. You can generate the wildcard certificate and we can configure any subdomain using this wildcard certificate.

Eg. We will generate certificate for domain name `*.devopspilot.tk` and later we can use this certificate to configure any subdomains like `app1.devopspilot.tk` `app2.devopspilot.tk` `app3.devopspilot.tk`

### How to install cerbot

```
sudo apt-get update
sudo apt-get install certbot
sudo apt-get install python3-certbot-nginx
```

### Create some sample application

To test wildcard certificate, we need some sample applications. Lets create one docker containers with sample python flask application.

```
docker run -d -e APP_COLOR=red -p 8081:5000 vigneshsweekaran/helloworld-flask:latest
```

Now we created one docker containers which runs on port 8081

Now open the browser and verify the applications are running.

IP-address:8081 --> Should show background color as red

![letsencrypt](../../images/app1.png)

### Configure DNS record in Domain registrar

app1.devopspilot.tk --> Public IP-address

![letsencrypt](../../images/dns-record.png)

`Note :`

- Public IP-address --> Public IP-address of your server, where docker container is running.

- Make sure ports 8081 is open.

- Replace devopspilot.tk with your domain name.

### Generate certificate

For wildcard certificate we cannot use nginx plugin, since acme-challenge will not be completed by nginx.

For wildcard certificate we have to use dns challenge to complete the verification.

While generating the certificate it will generate one token, we have to add that token as `TXT` DNS record in domain registrar.

Lets run the below command to generate the certificate

```
sudo certbot certonly --manual --preferred-challenges=dns -d *.devopspilot.tk
```

It will ask for email address, agree the terms and conditions, copy the token and add the token as `TXT` record in domain registrar with sub domain as `acme-challenge` and then press Enter to continue and the certificate will be issued.

Note:

- If you are using freenom domain registrar, wait for 5 minutes before pressing ENTER after adding the `TXT` DNS record.

![letsencrypt](../../images/generate-ssl1.png)

![letsencrypt](../../images/dns-record-txt.png)

![letsencrypt](../../images/generate-ssl2.png)

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
    server_name app1.devopspilot.tk;
    location / {
        proxy_pass http://localhost:8081;
    }
    listen 443 ssl;
    ssl_certificate /etc/letsencrypt/live/devopspilot.tk/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/devopspilot.tk/privkey.pem;
}
server {
    if ($host = app1.devopspilot.tk) {
        return 301 https://$host$request_uri;
    }
    listen 80;
    server_name app1.devopspilot.tk;
    return 404;
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

Wait for couple of minutes.

Go to browser and type `http://app1.devopspilot.tk`

Now it will automatically redirect to `https://app1.devopspilot.tk`

![letsencrypt](../../images/app-ssl.png)

Letsencrypt certificates will expire after 3 months.

Since we have generated the ssl certificate using `--manual` argument we cannot automatically renew the certificate.

If we want to automatically renew the certificates we have to use the domain-registrar plugin while generating the certificate.

I have used `freenom` domain registrar, that is not supported by letsencrpt as a plugin to automate the DNS record challenge.

If you have used Godady, AWS Route53, Google Domains you can use the letsencrypt plugin to automate this.

[Letsencrypt DNS plugin documentation link](https://certbot.eff.org/docs/using.html?highlight=dns#dns-plugins)

Hurray! we have successfully configured the SSL/TLS certificate in nginx webserver.

### Reference:

- [How to install nginx](../../webserver/nginx/install-nginx/index.md)

- [How to configure Free Let’s Encrypt SSL/TLS Certificates with NGINX](../letsencrypt-nginx/index.md)
