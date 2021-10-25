/*******************************************************************************
 Copyright (C) 2021  Optimal Design Company All Rights Reserved
 Unauthorized copying of this file, via any medium is strictly prohibited
 Proprietary and confidential

 Common functions and inclusions of API's needed for Javascript Jest framework
 to run.

 These common functions are used by multiple BLE tests.

 NOTES:

 *******************************************************************************/

'use strict';

const api = require('../../pc-ble-driver-js/index');
const fs = require('fs');
const { parse, stringify } = require('envfile');
const pathToEnvFile = './config.env';

const adapterFactory = api.AdapterFactory.getInstance(undefined, { enablePolling: false });
const serviceFactory = new api.ServiceFactory();

var dotenv = require('dotenv').config({ path: pathToEnvFile });

/**
 * Open an adapter on port provided
 *
 * @param {string} Port number
 * @param {string} API Version (SD version V2 or V5)
 * @returns {Promise<Adapter>} An opened adapter ready to use
 */
async function grabAdapter(portNumber, apiVersion) {
    const adapter = adapterFactory.createAdapter(apiVersion, portNumber, '');
    //addAdapterListener(adapter);

    adapter.on('error', err => console.log(`[${portNumber}] Adapter error ${err.message}`));

    return new Promise((resolve, reject) => {
        const baudRate = 1000000;
        console.log(`Opening adapter with ID: ${adapter.instanceId} and baud rate: ${baudRate}...`);

        adapter.open({ baudRate, logLevel: 'error' }, err => {
            if (err) {
                reject(Error(`Error opening adapter: ${err}.`));
                return;
            }

            resolve(adapter);
        });
    });
}

/**
 * Release a previously grabbed adapter
 *
 * @param {string} Port number
 * @returns {Promise<portNumber>} Resolved promise with released adapater if OK, rejected if not
 */
async function releaseAdapter(adapter) {
    return new Promise((resolve, reject) => {
        adapter.close(closeError => {
            if (closeError) {
                reject(error);
                return;
            }

            resolve(adapter);
        });
    });
}

/**
 * Function to reload config file between tests
 *
 */
async function updateEnv() {
    return new Promise((resolve, reject) => {
        fs.readFile(pathToEnvFile, 'utf8', function (err, data) {
            if (err) {
                console.log(err);
                reject();
            }

            let updatedEnv = parse(data);
            let size = Object.keys(updatedEnv).length;
            let keys = Object.keys(updatedEnv);
            console.log("Size of keys is: " + size + " keys: " + JSON.stringify(keys));
            for (let i = 0; i < size; i++) {
                console.log("KEY[" + keys[i] + "] = " + updatedEnv[keys[i]]);
                dotenv[keys[i]] = updatedEnv[keys[i]];
            }

            console.log("updateEnv dump: " + JSON.stringify(dotenv));
            resolve();
        });
    });
}

/**
 * Function to set environment variables.
 *
 * @param {string} key
 * @param {string} value
 */
async function setEnv(key, value) {
    dotenv[key] = value;
    return new Promise((resolve, reject) => {
        // TODO: Handle if file doesn't exist
        //console.log("setEnv(" + key + ") = " + value);
        fs.readFile(pathToEnvFile, 'utf8', function (err, data) {
            if (err) {
                console.log(err);
                reject();
            }
            var result = parse(data);
            result[key] = value;
            fs.writeFile(pathToEnvFile, stringify(result), function (err) {
                if (err) {
                    console.log(err);
                    reject();
                }
                //console.log("File Saved");
                resolve();
            })

        });
    });
}

/**
 * Function to get value from env
 *
 * @param {string} key
 */
function getEnv(key) {
    //console.log("getEnv[" + key + "] = " + dotenv[key]);
    return dotenv[key];
}

module.exports = {
    grabAdapter,
    releaseAdapter,
    getEnv,
    setEnv,
    updateEnv
};
