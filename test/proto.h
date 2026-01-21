typedef struct __attribute__((packed)) {
    _Bool value1;
    unsigned short value2;
} Boh;

typedef struct __attribute__((packed)) {
    _Bool value1;
    unsigned short value2;
    short value3;
    unsigned char value4;
    char value5;
    unsigned long value7;
    long value6;
    unsigned long long value8;
    long long value9;
    float value10;
    double value11;
    Boh value12;
} Test;

