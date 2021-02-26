# command-buttons
Simple web app that allows running preconfigured shell commands on host via buttons

## Installation
`$ ./setup.sh`

## Configuration
Add your custom command definitions to `config.json`:
```json
{
    "host": "0.0.0.0",
    "port": 8098,
    "commands": {
        "shutdown": "systemctl poweroff -i",
        "ping": "ping -c 3 google.de"
    }
}
```

## Usage
1. `$ ./run.sh`
1. Open `http://<your_ip>:8098/` in the browser (e.g. from your phone)
1. Remotely run your commands by tapping a button while observing stdout/stderr in realtime

<p align="center">
    <img src="https://user-images.githubusercontent.com/609855/109354034-78ed6100-787d-11eb-9106-87c7bf6d692d.png" alt="screenshot" height="640">
</p>



