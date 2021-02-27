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
    "abort_signal": "SIGINT",
    "commands": {
        "shutdown": "systemctl poweroff -i",
        "ping": "ping google.de",
        "stop": "true"
    }
}
```
If you want to enable authorization, set `secret_key` to a random secret value e.g. using:
```bash
$ python3 -c 'import secrets; print(secrets.token_urlsafe())'
```
Only one running command process is allowed at a time. When the user invokes a new command, any other command that might be still running will be aborted by sending `abort_signal` to the corresponding process. Please refer to the [Python Documentation](https://docs.python.org/3/library/signal.html#module-contents) for details.

## Usage
1. `$ ./run.sh`
2. Open `http://<your_ip>:8098/` in the browser (e.g. from your phone)
3. If authorization is enabled, the server terminal will prompt `Accept session from <remote_ip>? [y,N]`. After confirming with 'y', the client will be authenticated automatically and authorized permanently in future sessions. After denying by any other input than 'y', the client will be rejected automatically until the server is restarted.
4. Remotely run your commands by tapping a button while observing stdout/stderr in realtime

<p align="center">
    <img src="https://user-images.githubusercontent.com/609855/109392866-cf5eac00-791e-11eb-8512-4f606095d5dd.png" alt="screenshot" height="640">
</p>

## Notes
- The intended use case is **not** public deployment, but rather convenience in closed home network environments
- Authorization won't work with older browsers without explicitly setting same-origin credentials (due to the use of [fetch()](https://github.com/whatwg/fetch/pull/585))



