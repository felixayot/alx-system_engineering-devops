# Incident Report - Postmortem on Flexco server hosting the AirBnB clone
```
fayot@sysadmin:~$ curl -sI 54.160.92.115
curl: 😢😢😢 I'm sorry I don't know what they have done to me. I can't understand this request
fayot@sysadmin:~$
```

The following is the incident report for the Flexco server hosting the AirBnB clone downtime that occurred on October 5, 2023. We understand this service issue has impacted our valued property owners and renters, and we sincerely apologize to everyone who was affected.

## Issue Summary
From 9:05 PM to 10:23 PM East African Time(EAT), requests to flexco.tech resulted in `This site can’t be reached`, `flexco.tech refused to connect`. The issue affected 100% of traffic to the site, since the server was, well, the web server(`NGINX`) hosting the site was down, we took it down. The root cause of this server downtime was an invalid configuration change to renew the Secure Socket Layer certificate for SSL termination in the website.

## Timeline (All times in EAT)
- 9:00 PM: SSL termination configuration begins
- 9:05 PM: SSL termination fails on our load balancer and users' encrypted requests fail to be served.
- 9:05 PM: Pagers alerted teams
- 9:07 PM: Web server restarts fail to correct the issue
- 9:10 PM: Rollbacks to bring up the load balancer running with successful SSL termination fail
- 9:12 PM: Flexco server goes down completely
- 10:18 PM: Server restarts begin
- 10:23 PM: 100% of traffic back online

## Root Cause and Resolution
At 9:00 PM EAT, an auto-renewal for the `certbot` SSL certificate began as the old one was just expiring. At 9:05 PM EAT, when our HaProxy  was reloaded, it failed to decrypt encrypted user requests causing the malfunction. Our `Datadog` monitoring system alerted our on-call engineers. At 9:05 PM EAT, they quickly restarted our main server and the proxy server since they thought that the SSL certificate change in the load balancer would have required the `nginx` web servers to be restarted. This unfortunately failed and they had to escalate the issue by 9:07 PM EAT.

I got the escalation alert at 9:07 PM EAT and did a quick status check at the HaProxy load balancer. As expected, Haproxy was not running. I checked its error logs with no luck. At 9:12 PM EAT, I decided to take the `nginx` web servers offline, just to stop overwhelming the server monitors with system malfunction alerts(Not apologizing for this) since I needed a peaceful and calm environment to figure out how to get `haproxy` running and SSL terminating successfully.
I had a substantial level of experience working with `haproxy`, so after minutes of fruitless efforts, I decided to check if the configuration file was okay(Just to make sure) at 10:09 PM EAT. To my surprise, I found out that the file had some outdated configuration directives, which were not recognized by the latest version of `haproxy`. Oops! Who would have thought. I then embarked on getting the new directives on the configuration file.

At 10:18 PM EAT, I was done correcting the errors on the HaProxy configuration and restarted it and as expected, it was running and ready to distribute traffic to our servers. Next, I brought up the `nginx` web servers to receive and serve user requests. By 10:23 PM EAT, our systems were fully online again.

## Corrective and preventative Measures
Lessons from this world-class embarrassment led us to introduce a comprehensive update to all our packages and a decision to get an alert to update the relevant configuration files to the latest directives whenever an automatic package update is initiated and of course, run a simulation test on our UAT environment. This would prevent outages due to automatic update failures.
