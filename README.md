# Sscreen

A tiny tool for taking screenshot or screen recoding of android device, by [ADB](https://developer.android.com/studio/command-line/adb.html) commands.

### Aim

Android's ADB already provide two convienent tools: `screencap`,`screenrecord` to take screenshot and screen record. If you want get a screenshot of current display, you have to:

```
adb shell screencap /sdcard/screenshot.png
adb pull /sdcard/screenshot.png ./
# remove it if you want
adb shell rm /sdcard/screenshot.png
```
however,it's annoying to type two(three) commands to get a screenshot(record) everytime.So,here is `sscreen`.

### Install

Download the `sscreen.py` and place it on your PATH

### Usage 

Before you get started, make sure `adb` is on your path:

```
export PATH=$PATH:<path to Android SDK>/platform-tools
export PATH=$PATH:<path to Android SDK>/tools
```

Examples

```
# take a screenshot:
sscreen.py ~/Download/

# record screen
sscreen.py -r ~/Download

# record a 10 seconds video with size 1280x720, 5Mbps
sscreen -r --size 1280x720 --bit-rate 5000000 --time-limt 10 ~/Downloads/ 
```

Use `sscreen.py -h` for more details, see also adb [docs](https://developer.android.com/studio/command-line/adb.html)