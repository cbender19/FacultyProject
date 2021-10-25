'use strict';

const { grabAdapter, releaseAdapater, setEnv, getEnv } = require ('./setup');

const adapterPort = process.env.ADAPTER_PORT;
const bleDeviceName = process.env.BLE_DEVICE_NAME;
const bleMacAddress = process.env.BLE_MAC_ADDRESS;

const JEST_BLE_TEST_TIME = 35000;
const SCANNING_TIME_MS = 30000;
var deviceFound = 0;

let scanner;
let bleFoundDevice;

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

    adapter.on('deviceDiscovered', device => {
        //console.log(`Discovered device ${device.address}/${device.addressType}.`);
        
        // Checks mac address or name if one or the other is null
        if (((device.address === bleMacAddress) || (device.name === bleDeviceName)) && (deviceFound == 0)){
            deviceFound = 1;
            bleFoundDevice = device;
            console.log(`Found Device: ${device.name} ${device.address}`);
            scanner.cancel();
        }
    });
}

/**
 * Start a BLE Scan
 *
 * @param {Adapter} adapter in use
 * @returns {promise}
 */
async function startScan(adapter) {
    return new Promise((resolve, reject) => {
        console.log('Started scanning...');

        const scanParameters = {
            active: true,
            interval: 100,
            window: 50,
            timeout: 0,
        };

        adapter.startScan(scanParameters, err => {
            if (err) {
                reject(new Error(`Error starting scanning: ${err}.`));
            } else {
                resolve();
            }
        });
    });
}

/**
 * Setup a cancellable promise scan timer
 *
 * @param {adapter}: USB Adapter to use
 * @returns {promise & cancel function}
 */
let scanTimer = (adapter) => {
    let bleScanTimer = 0;
    let reject = null;
    let scanTimerResolve;

    let promise = new Promise((_resolve, _reject) => {
        reject = _reject;
        scanTimerResolve = _resolve;
        bleScanTimer = setTimeout(() => {
            adapter.stopScan(stopScanError => {
                if (stopScanError) {
                    _reject(stopScanError);
                    return;
                }

                _resolve();
            });
        }, SCANNING_TIME_MS);
    });

    return {
        get promise() {
            return promise;
        },
        cancel() {
            if (bleScanTimer) {
                clearTimeout(bleScanTimer);
                adapter.stopScan(stopScanError => {
                    if (stopScanError) {
                        reject(stopScanError);
                        return;
                    }

                    scanTimerResolve();
                });
                bleScanTimer = 0;
                reject = null;
            }
        }
    };
}

/* Jest Describe Contains Group of Tests to be performed */
describe('BleAdvertising', () => {
    let adapter;

    /* Jest Setup before all tests are executed */
    beforeAll(async () => {
        adapter = await grabAdapter(adapterPort, 'v5');
        addAdapterListener(adapter);
    });

    /* Jest cleanup after all tests are executed */
    afterAll(async () => {
        await releaseAdapter(adapter);
    });

    jest.setTimeout(JEST_BLE_TEST_TIME);
    test('BLE Device Found', async() => {
        await startScan(adapter);
        scanner = scanTimer(adapter);
        await scanner.promise;

        if (deviceFound) {
            // Set Device Address so we can use for connect
            await setEnv("BLE_MAC_ADDRESS", bleFoundDevice.address);
            await setEnv("BLE_ADDR_TYPE", bleFoundDevice.addressType);
            await setEnv("BLE_DEVICE_NAME", bleFoundDevice.name);
        }

        expect(deviceFound).toBe(1);
    });
});

