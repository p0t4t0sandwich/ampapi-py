# WatchFerret

Credit to sneakysnek#8707 for thinking of the name

## Download

`wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/p0t4t0sandwich/ampapi-python/main/watchferret/WatchFerret.py`

`wget --no-check-certificate --content-disposition https://raw.githubusercontent.com/p0t4t0sandwich/ampapi-python/main/watchferret/config.yml`

## How to find `Instance Name`

You can find the instance's name by running `ampinstmgr status` in your CLI/SSH window, or on the right hand side of the AMP web ui when selecting an instance.

## Example Config

```yaml
---
# Global default config for instance management.
global:
  # The address to your AMP instance web port.
  amp_url: "http://localhost:8080"
  # True if the instance is being accessed via the main ADS/Controller.
  # False if the instance is being accessed directly via it's web port.
  is_ads: True
  amp_username: "username"
  amp_password: "password"
  # Path to logs
  logging_path: "./"
  # Time in seconds for how often you want to ping the server.
  sample_interval: 300
  # Average rescue threshold in minutes: INTERVAL*THRESHOLD/60 (plus or minus ~0.95*INTERVAL/60).
  # How many pings during a server restart before rescuing the server.
  restart_threshold: 2
  # How many pings during a server start before rescuing the server.
  start_threshold: -1
  # How many pings during a server stop before rescuing the server.
  stop_threshold: -1

# Instances are identified using the instance name listed in the AMP web ui.
instances:
  # Leave the instance's config as {} for it to inherit the global config.
  Lobby01: {}
  # Any entry listed here will override the global config, and any unspecified entries will be pulled from the global config.
  CoolSMP01:
    amp_url: "http://localhost:8081"
    is_ads: False
    start_threshold: 3
```

## Notes on using your main Controller/ADS

If you are not running this program on the AMP system, it is recommended that you use the main Controller/ADS to authenticate the instance. This way you don't need to open the instance's web port. If you are running this program within your home/local network you can safely disregard this note.
