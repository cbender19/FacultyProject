'use strict';

const adapterPort = process.env.ADAPTER_PORT;
const { grabAdapter, releaseAdapater, setEnv, getEnv, updateEnv } = require ('./setup');

const JEST_BLE_TEST_TIME_MS = 30000;

var deviceConnected = 0;
var deviceMacAddress = "";

let connectedDevice;
let bleDeviceName = "0";
let bleMacAddress = "0";
let bleDeviceType = "0";


/**
 * Handling events emitted by adapter.
 *
 * @param {Adapter} adapter Adapter in use.
 * @returns {void}
 */
function addAdapterListener(adapter)
{
    adapter.on('scanTimedOut', () => {
        console.log('scanTimedOut: Scanning timed-out. Exiting.');
    });

    /**
     * Handling error and log message events from the adapter.
     */
    adapter.on('logMessage', (severity, message) => { if (severity > 3) console.log(`${message}.`); });
    adapter.on('error', error => { console.log(`error: ${JSON.stringify(error, null, 1)}.`); });

    /**
     * Handling the Application's BLE Stack events.
     */
    adapter.on('deviceConnected', device => {
        console.log(`Device ${device.address}/${device.addressType} connected.`);
        deviceConnected = 1;
        connectedDevice = device;
    });

    adapter.on('deviceDisconnected', device => {
        console.log(`Device ${device.address} disconnected.`);
    });

    adapter.on('deviceDiscovered', device => {
        //console.log(`Discovered device ${device.address}/${device.addressType}.`);
    });

    adapter.on('scanTimedOut', () => {
        console.log('scanTimedOut: Scanning timed-out. Exiting.');
    });
}

function connect(adapter, connectToAddress) {
    return new Promise((resolve, reject) => {
        if (connectToAddress === "0") {
            reject();
        }

        console.log(`Connecting to device ${connectToAddress}...`);

        const options = {
            scanParams: {
                active: false,
                interval: 100,
                window: 50,
                timeout: 0,
            },
            connParams: {
                min_conn_interval: 7.5,
                max_conn_interval: 30,
                slave_latency: 0,
                conn_sup_timeout: 4000,
            },
        };

        let connectionParams = {};

        connectionParams.address = connectToAddress;
        connectionParams.type = bleDeviceType;

        console.log("Connection Info: " + JSON.stringify(connectionParams));
        jest.setTimeout(5000)
        adapter.connect(connectionParams, options, err => {
            if (err) {
                reject(Error(`Error connecting to target device: ${err}.`));
                return;
            }

            resolve();
        });
    });
}

function disconnect(adapter, device) {
    return new Promise((resolve, reject) => {
        adapter.disconnect(device.instanceId, disconnectErr => {
            if (disconnectErr) {
                reject(disconnectErr);
                return;
            }

            console.log(`Initiated disconnect from ${device.address}/${device.addressType}.`);
            resolve();
        });
    });
}

describe('BLE Connection', () => {
    let adapter;

    beforeAll(async () => {
        adapter = await grabAdapter(adapterPort, 'v5');
        addAdapterListener(adapter);

        await updateEnv();
    });

    afterAll(async () => {
        await releaseAdapter(adapter);
    });

    test('BLE Device ENV Check', () => {
        bleDeviceName = getEnv("BLE_DEVICE_NAME");
        bleMacAddress = getEnv("BLE_MAC_ADDRESS");
        bleDeviceType = getEnv("BLE_ADDR_TYPE");

        expect(bleMacAddress).not.toBe("0");
        expect(bleDeviceName).not.toBe("0");
        expect(bleDeviceType).not.toBe("0");
    });

    jest.setTimeout(JEST_BLE_TEST_TIME_MS);
    test('BLE Device Connected', async() => {
        await connect(adapter, bleMacAddress).then(() => {
        }).catch(error =>{
            console.log(error);
        });

        if (deviceConnected === 1) {
            await disconnect(adapter, connectedDevice);
        }

        expect(deviceConnected).toBe(1);
    });
})
