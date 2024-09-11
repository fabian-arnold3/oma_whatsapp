# oma_whatsapp
## Description
A Python script using pywhatkit to send my grandmother a good moring message and image every Sunday at 8:00 a.m. using corn.

edit cron table 
``` bash
crontab -e
```
contab entry
```bash
0 8 * * SUN /Users/fabianarnold/projects/oma_whatsapp/script.sh > /dev/null 2>&1
```
