# sens-fov-scalar
Creates .cfg files for testing different sensitivities (algorithms from mouse-sensitivity.com) at different FOV's in CSGO _similar_ to the method created by Drimzi here: https://www.mouse-sensitivity.com/forum/topic/3280-perceived-sensitivity/?do=findComment&comment=14119

## What you will need:
* Python, > v3

## Prior notes
* You don't need to delete the files after each run, the script will over write them with the correct values if you typed in a different %, however the base file will remain.
* This code has no input validation, but as long as you follow the instructions there should be no errors.

## Video Tutorial:
[![Video tutorial](http://img.youtube.com/vi/9Cte4PKWfQI/0.jpg)](http://www.youtube.com/watch?v=9Cte4PKWfQI "CS:GO - FOV + SENS Scalar")

## How to use:
1. Create a new folder somewhere, e.g. desktop, to store the files you download from this repository
2. Clone or download this directory into that folder (green button top right of this page), unzip if needed.
3. You can now move these [into your config folder](https://www.reddit.com/r/GlobalOffensive/comments/3xci8w/fyi_the_default_config_folder_has_changed_please/) with all the other config files which is probably in `...\Steam\userdata\<YOURID>\730\local\cfg` or maybe here `...\Counter-Strike Global Offensive\csgo\cfg`, I recommend putting it into the second path, as there's less to screw up here.
3. If you've done all these steps correctly, you should now be able to run the python file you put into the cfg folder, you can do this in the cmd by `python creator.py` or `python3 creator.py`, depending on your python installation, or simply double click the file (recommended).
4. Enter the values it asks for just as you would do in the calculator
5. Input the FOV ranges you want it to calculate: max - min read carefully which way round
6. The program will start to calculate the sensitivities and put them in the files (it will overwrite files with the same name, so you don't need to delete files inbetween runs).
7. In the folder, you should now have lots of files which start with up_[fov].cfg and down_[fov].cfg and one named fovscale[minFOV]+[maxFOV].cfg
9. Now you have these files, you need to enter CS, [I recommend this map](https://steamcommunity.com/sharedfiles/filedetails/?id=1104441138) and run the cfg file named 'fovscale[minFOV]+[maxFOV]' by opening console and typing: 'exec fovscale[minFOV]+[maxFOV]', a drop down menu should come up which you can pick from when typing it in.
10. Now you can run the script called 'keypresser.py', enter the delay between zoom intervals, if you go below about 10ms, the stream of instantaneous inputs can lag programs and cause them to crash, also, CSGO cannot handle this speed.
11. As soon as you pressed enter after inputting a delay, alt-tab into CS and wait for the zooming to start!
12. To stop, alt-tab into the window running the python script, it should look black, and press ctrl+c, or just close the window.
