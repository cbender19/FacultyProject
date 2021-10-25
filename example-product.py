##############################################################################
#    Copyright (C) 2021  Optimal Design Company All Rights Reserved
#    Unauthorized copying of this file, via any medium is strictly prohibited
#    Proprietary and confidential
#
#    Product Script that runs BLE tests for this product.
#
#    NOTES:
#
##############################################################################

#!/usr/bin bash

import sys
import argparse
import os
import subprocess
import json

JEST_JSON_FILENAME = "testResult.json";

"""
If there are no arguments, then should just reuse
the help function print out the usage statement.
"""
def helpFunction(parser):
    args = parser.parse_args(['-h']);
    print(args.echo)

"""
Setup the parser with appropriate arguments.
Return the copy of the parser to use else where.
"""
def setupCommandLineParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="USB Port Identifier", nargs=1)
    parser.add_argument("-d", "--device", help = "BLE device name", nargs=1)
    parser.add_argument("-m", "--mac", help = "BLE mac address", nargs=1)

    return parser

"""
Actually do the command line parsing
"""
def parseCommandLine(parser, new_env):
    args = parser.parse_args()

    # Check to see if we have valid inputs
    # first prior to setting environment variables
    if (args.port == None):
        print("No adapter port specified!");
        return False;

    if (args.device == None and args.mac == None):
        print("Need a device name and mac address!");
        return False;

    new_env['ADAPTER_PORT'] = args.port[0]
    new_env['BLE_DEVICE_NAME'] = "0"
    new_env['BLE_DEVICE_TYPE'] = "0"
    new_env['BLE_MAC_ADDRESS'] = "0"

    if (args.device != None):
        new_env['BLE_DEVICE_NAME'] = args.device[0];

    if (args.mac != None):
        new_env['BLE_MAC_ADDRESS'] = args.mac[0];

    print("Selected to use: Port = %s, Device Name: %s, MAC Address: %s\n" %
          (new_env['ADAPTER_PORT'], new_env['BLE_DEVICE_NAME'],
            new_env['BLE_MAC_ADDRESS']));
    return True

def run_test(fileName, new_env):
    success = False;

    try:
        cmd = "npx jest --json --outputFile="
        cmd += JEST_JSON_FILENAME
        cmd += " --detectOpenHandles --forceExit"
        cmd += " "
        cmd += fileName
        print(cmd)

        subprocess.run(cmd, shell=True, env=new_env).wait()
    except AttributeError:
        print("Error with running test!")

    # AttributeError occurs with some issues of timeouts, will need to fix, but for
    # now will assume it's ok and check the result from a json file output.
    filename = os.getcwd() + "/" + JEST_JSON_FILENAME;

    success = False;
    try:
        json_file = open(filename, 'r');
        data = json.load(json_file);

        print("numFailedTestSuites: %s" % data['numFailedTestSuites'])
        if (data['numFailedTestSuites'] == 0):
            success = True;
    except FileNotFoundError:
        print("Jest Results File Not Found!");

    return success;

def verifySuccess(result):
    if (result == False):
        sys.exit(1);

def main(argv):
    parser = setupCommandLineParser();

    ### Easiest way to check if any arguments
    if (len(sys.argv) == 1):
        helpFunction(parser);
        sys.exit();

    ### Parse the command line
    new_env = os.environ.copy()
    if parseCommandLine(parser, new_env) == False:
        sys.exit(1);

    ### Run the Tests
    verifySuccess(run_test("advertise.test.js", new_env));
    verifySuccess(run_test("connection.test.js", new_env));

if __name__ == "__main__":
    main(sys.argv)
