
#include <stdio.h>
#include <stdint.h>
#include <time.h>
#include <string.h>

uint32_t totalImuSamples = 0;
uint32_t startTime = 0;
uint32_t lastTime = 0;
FILE *fw;


uint16_t msgLength( uint8_t msgType, FILE *fh) {
    uint16_t msgLen = 0;

    switch (msgType) {
    case 0x01: // time
        msgLen = 6;
        break;
    case 0x02: // imu
        fread( &msgLen, 2, 1, fh);
        msgLen = ((msgLen>>8) | (msgLen<<8)) * 7;
        break;
    case 0x03: // in-range
        msgLen = 6;
        break;
    case 0x04: // out-range
        msgLen = 6;
        break;
    case 0x05: // battery
        msgLen = 2;
        break;
    case 0x06: // temp
        msgLen = 1;
        break;
    case 0x07: // version (date)
        msgLen = 3;
        break;
    case 0x08: // rate
        msgLen = 1;
        break;
    case 0x09: // no move
        msgLen = 0;
        break;
    case 0x0a: // ssid
        fread( &msgLen, 1, 1, fh);
        break;
    case 0x0b: // version
        msgLen = 3;
        break;
    default:
        printf("unknown msg type=0x%02X\n", msgType);
    }
    return(msgLen);
}

void processMsg(uint8_t msgType, uint8_t * data, uint16_t msgLen) {
    struct tm ts;
    static char   buf[80];

    switch (msgType) {
    case 0x01:
        lastTime = (((uint32_t) data[0])<<24) + (((uint32_t) data[1])<<16) + (((uint32_t) data[2])<<8) + data[3];
        ts = *localtime((const time_t *)&lastTime);
        strftime(buf, sizeof(buf), "%Y-%m-%d %H:%M:%S,", &ts);
        if (startTime == 0) {startTime = lastTime;}
        //printf("%s\n",buf);
        break;
    case 0x02:
        //printf("%s imu len=%d sec=%f\n",buf, msgLen, (double) msgLen/6/2/104); // 6 bytes per sample, 2 types, 104 mHz
        totalImuSamples += msgLen/6;
        break;
    case 0x03:
        //printf("%s in-range %02X%02X%02X%02X%02X%02X\n", buf, data[0],data[1],data[2],data[3],data[4],data[5]);
        break;
    case 0x04:
        //printf("%s out-range\n", buf);
        break;
    case 0x05:
        printf("%s %d%%\n", buf, data[0]);
        fprintf( fw, "%s %d%%\n", buf, data[0]);
        break;
    case 0x06:
        //printf("%s temp %2d\n",buf,data[0]-50);
        break;
    case 0x07:
        //printf("%s version (data) %d.%d.%d\n",buf, data[0],data[1],data[2]);
        break;
    case 0x08:
        //printf("%s rate\n", buf);
        break;
    case 0x09:
        //printf("%s no move\n", buf);
        break;
    case 0x0a:
        //printf(".... .. .. .. .. .. ssid\n");
        break;
    case 0x0b:
        //printf("%s version (current) %d.%d.%d\n",buf, data[0],data[1],data[2]);
        break;
    default:
        printf("unknown msg type=0x%02X\n", msgType);
    }
}

int main( void ) {
    uint8_t data[10*1024];
    uint8_t msgType;
    uint16_t msgLen;
    FILE *fh;

    fh = fopen("binarySample3.bin","r");
    fw = fopen("binarySample3.csv","w+");

    if (fh == NULL) {
        printf("File Open Error\n");
        return(1);
    }

    while (fread( &msgType, 1, 1, fh) == 1) {
        msgLen = msgLength( msgType, fh );
        fread( data, msgLen, 1, fh);
        processMsg( msgType, data, msgLen);
    }

    fclose(fw);

    printf("total Imu Samples = %d\n", totalImuSamples);
    printf("total seconds = %d\n",lastTime - startTime);
    printf("Samples per second = %d\n",totalImuSamples / (lastTime - startTime));
}
