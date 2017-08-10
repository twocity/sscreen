#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import subprocess
import time
import os

DEFAULT_DIR = '/sdcard/Pictures/sscreen'
ADB = ['adb']
ADB_SHELL = ADB + ['shell']
ADB_SCREEN_CAP = ADB_SHELL + ['screencap']
ADB_SCREEN_RECORD = ADB_SHELL + ['screenrecord']

parser = argparse.ArgumentParser(description='Tiny tool for taking screenshot or screen recoding of android devices.')
parser.add_argument('output', nargs=1, help='screenshot file directory')
parser.add_argument('-r', '--record', help='take screen record',action='store_true')
parser.add_argument('-s', '--size', help='video size <WIDTHxHEIGHT> eg. 1280x720')
parser.add_argument('-b', '--bit-rate', type=int, help='the video bit rate for the recorded video')
parser.add_argument('-t', '--time-limit', type=int, help='the maximum recording time, in seconds')
parser.add_argument('-k', '--keep', help='save screenshot file on device', action='store_true')

args = parser.parse_args()
output_dir = args.output[0]
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
assert os.path.isdir(output_dir)

subprocess.check_call(ADB_SHELL + ['mkdir', '-p', DEFAULT_DIR])

def pull(filename, output):
    subprocess.check_call(ADB + ['pull', filename, output])

def remove(filename):
    subprocess.check_call(ADB_SHELL + ['rm', filename])

def screencap():
    filepath = DEFAULT_DIR + '/' + str(int(time.time())) + '.png'
    print 'taking screenshot...'
    subprocess.check_call(ADB_SCREEN_CAP + [filepath])
    return filepath

def screen_record(r_args):
    filepath = DEFAULT_DIR + '/' + str(int(time.time())) + '.mp4'
    command = ADB_SCREEN_RECORD + r_args +  [filepath]
    if args.time_limit:
        timeout = args.time_limit
        assert timeout <= 180, 'time-limit must in [1, 180]'
        print 'Record will stop after %d seconds' % args.time_limit
        sub = subprocess.Popen(command)
        sub.wait()
    else:
        sub = subprocess.Popen(command)
        if not raw_input("Start recoding... Press enter to stop"):
            print 'Stopping...'
            sub.terminate()
            time.sleep(1)
    return filepath

if args.record:
    r_args = []
    if args.size:
        r_args += ['--size', args.size]
    if args.bit_rate:
        r_args += ['--bit-rate', str(args.bit_rate)]
    if args.time_limit:
        r_args += ['--time-limit', str(args.time_limit)]
    output_file = screen_record(r_args)
else:
    output_file = screencap()

pull(output_file, output_dir)
print 'Output file: ' + os.path.join(output_dir, os.path.basename(output_file))
if not args.keep:
    remove(output_file)
