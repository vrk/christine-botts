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
- `python -m venv env` then install the missing thing with sudo
- `python -m venv env`
- `source env/bin/activate`
- `pip install gpiozero`
- [Wiring a button](https://gpiozero.readthedocs.io/en/stable/recipes.html#button)
