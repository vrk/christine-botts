# christine-botts

### RPI instructions

What to do when starting from a fresh raspberry pi lite install:

On the machine you're sshing from:
- Reset ssh keys so you can ssh in: `ssh-keygen -R <HOST>`
- Then ssh in

On the raspberry pi:
- `sudo apt update`
- `sudo apt upgrade`
- `sudo apt install vim git pip`
- `sudo apt install sox libsox-fmt-all` for playing test sounds
- `sudo vim /boot/config.txt` and add `dtoverlay=hifiberry-dac` under `[all]`
- restart the pi: `sudo reboot`
- [Set up GitHub ssh keys](https://gist.github.com/xirixiz/b6b0c6f4917ce17a90e00f9b60566278)
- Clone this repo
- cd into `christine-botts`
- Try playing some audio thing: `play test-audio/piano2.wav`
- `python3 -m venv .venv` then install the missing thing with sudo
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `pip install gpiozero RPi.GPIO pygame`
- `sudo apt install python3-gpiozero` idk if this is needed, but gpiozero docs mention
- `sudo apt install python3-sdl2 libsdl-ttf2.0-0`
  - it's possible this just needs to be `sudo apt install libsdl2-mixer-2.0-0`
- `sudo pip3 install pygame --break-system-packages` -- needed for running script on sudo
- [Start script on launch](https://learn.sparkfun.com/tutorials/how-to-run-a-raspberry-pi-program-on-startup#method-1-rclocal)
  - `sudo vim /etc/rc.local`
  - add:
    ```
    sudo bash -c 'source /home/vrk/christine-botts/.venv/bin/activate > /home/vrk/blink1.log 2>&1' & 
    sudo python3 /home/vrk/christine-botts/audio-button.py &
    ```

### Viewing logs of background process

1. get the process id: `sudo ps -ax | grep python`
2. `sudo strace -p <PID> -e write`

### Query pisugar battery

- `echo "get battery" | nc -q 0 127.0.0.1 8423`
- go to http://rpi.local:8421/

### Helpful documentation:
- [Wiring a button](https://gpiozero.readthedocs.io/en/stable/recipes.html#button)

