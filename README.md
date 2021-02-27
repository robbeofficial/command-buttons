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
    "secret_key": null,
    "commands": {
        "shutdown": "systemctl poweroff -i",
        "ping": "ping -c 3 google.de"
    }
}
```
If you want to enable authorization, set `secret_key` to a random secret value e.g. using:
```bash
$ python3 -c 'import secrets; print(secrets.token_urlsafe())'
```

## Usage
1. `$ ./run.sh`
2. Open `http://<your_ip>:8098/` in the browser (e.g. from your phone)
3. If authorization is enabled, the server terminal will prompt `Accept session from <remote_ip>? [y,N]`. After confirming with 'y', the client will be authenticated automatically and authorized permanently in future sessions. After denying by any other input than 'y', the client will be rejected automatically until the server is restarted.
4. Remotely run your commands by tapping a button while observing stdout/stderr in realtime

<p align="center">
    <img src="https://user-images.githubusercontent.com/609855/109354034-78ed6100-787d-11eb-9106-87c7bf6d692d.png" alt="screenshot" height="640">
</p>

## Notes
- The intended use case is **not** public deployment, but rather convenience in closed home network environments
- It won't work with older browsers without explicitly setting same-origin credentials (due to the use of [fetch()](https://github.com/whatwg/fetch/pull/585))



