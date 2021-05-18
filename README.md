## Requirements
    - simple LED
    - use resistor to avoid burning

![layout](pics/layout.png)

You should run this service at startup, ex using cronbtab with screen

install screen service: <br>
`sudo apt install screen`

edit crontab:  <br>
`crontab -e`

Copy the following line to crontab file: <br>
`@reboot screen -S statusled -d -m /usr/bin/python ...yourpath.../cpustatus.py`
