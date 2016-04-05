def tvr_inter(tvr):
    bytes = bytearray.fromhex(tvr) 
    data = []
    if (int(bytes[0]) & int('10000000',2)):
        data.append("Byte 1 bit 8   = 1      Offline data authentication was not performed")
    else:
        data.append("Byte 1 bit 8   = 0      Offline data authentication was performed");

    if (int(bytes[0]) & int('01000000',2)):
        data.append("       bit 7   = 1      SDA failed");
    else:
        data.append("       bit 7   = 0      SDA passed or not performed");

    if (int(bytes[0]) & int('00100000',2)):
        data.append("       bit 6   = 1      ICC data missing");
    else:  
        data.append("       bit 6   = 0      No ICC data missing");

    if(int(bytes[0]) & int('00010000',2)):
        data.append("       bit 5   = 1      Card appears on terminal exception file");
    else:
        data.append("       bit 5   = 0      Card does not appear on terminal exception file");

    if(int(bytes[0]) & int('00001000',2)):
        data.append("       bit 4   = 1      DDA failed");
    else:  
        data.append("       bit 4   = 0      DDA passed or not performed");

    if(int(bytes[0]) & int('00000100',2)):
        data.append("       bit 3   = 1      CDA failed");
    else:
        data.append("       bit 3   = 0      CDA passed or not performed");

    if(int(bytes[0]) & int('00000010',2)):
        data.append("       bit 2   = 1      SDA selected");
    else:
        data.append("       bit 2   = 0      SDA not selected");

    if(int(bytes[0]) & int('00000001',2)):
        data.append("       bit 1   = 1      RFU");
    else:
        data.append("       bit 1   = 0      RFU");


    if(int(bytes[1]) & int('10000000',2)):
        data.append("Byte 2 bit 8   = 1      ICC and terminal have different application versions");
    else:
        data.append("Byte 2 bit 8   = 0      ICC and terminal do not have different application versions");

    if(int(bytes[1]) & int('01000000',2)):
        data.append("       bit 7   = 1      Expired application");
    else:
        data.append("       bit 7   = 0      No Expired application");

    if(int(bytes[1]) & int('00100000',2)):
        data.append("       bit 6   = 1      Application not yet effective");
    else:
        data.append("       bit 6   = 0      Application effective");

    if(int(bytes[1]) & int('00010000',2)):
        data.append("       bit 5   = 1      Requested service not allowed for card product");
    else:
        data.append("       bit 5   = 0      Requested service allowed for card product");

    if(int(bytes[1]) & int('00001000',2)):
        data.append("       bit 4   = 1      New card");
    else:
        data.append("       bit 4   = 0      No New card");

    if(int(bytes[1]) & int('00000100',2)):
        data.append("       bit 3   = 1      RFU");
    else:
        data.append("       bit 3   = 0      RFU");

    if(int(bytes[1]) & int('00000010',2)):
        data.append("       bit 2   = 1      RFU");
    else:
        data.append("       bit 2   = 0      RFU");

    if(int(bytes[1]) & int('00000001',2)):
        data.append("       bit 1   = 1      RFU");
    else:
        data.append("       bit 1   = 0      RFU");


    if(int(bytes[2]) & int('10000000',2)):
        data.append("Byte 3 bit 8   = 1      Cardholder verification was not successful");
    else:
        data.append("Byte 3 bit 8   = 0      Cardholder verification was successful or not performed");

    if(int(bytes[2]) & int('01000000',2)):
        data.append("       bit 7   = 1      Unrecognised CVM");
    else:
        data.append("       bit 7   = 0      Recognised CVM");

    if(int(bytes[2]) & int('00100000',2)):
        data.append("       bit 6   = 1      PIN Try Limit exceeded");
    else:
        data.append("       bit 6   = 0      PIN Try Limit not exceeded");

    if(int(bytes[2]) & int('00010000',2)):
        data.append("       bit 5   = 1      PIN entry required and PIN pad not present or not working");
    else:
        data.append("       bit 5   = 0      No PIN entry required (PIN pad may or may not be present or may or may not be working)");

    if(int(bytes[2]) & int('00001000',2)):
        data.append("       bit 4   = 1      PIN entry required, PIN pad present, but PIN was not entered");
    else:
        data.append("       bit 4   = 0      No PIN entry required (PIN pad may or may not be present)");

    if(int(bytes[2]) & int('00000100',2)):
        data.append("       bit 3   = 1      Online PIN entered");
    else:
        data.append("       bit 3   = 0      No Online PIN entered");

    if(int(bytes[2]) & int('00000010',2)):
        data.append("       bit 2   = 1      RFU");
    else:
        data.append("       bit 2   = 0      RFU");

    if(int(bytes[2]) & int('00000001',2)):
        data.append("       bit 1   = 1      RFU");
    else:
        data.append("       bit 1   = 0      RFU");


    if(int(bytes[3]) & int('10000000',2)):
        data.append("Byte 4 bit 8   = 1      Transaction exceeds floor limit");
    else:
        data.append("Byte 4 bit 8   = 0      Transaction does not exceed floor limit");

    if(int(bytes[3]) & int('01000000',2)):
        data.append("       bit 7   = 1      Lower consecutive offline limit exceeded");
    else:
        data.append("       bit 7   = 0      Lower consecutive offline limit not exceeded");

    if(int(bytes[3]) & int('00100000',2)):
        data.append("       bit 6   = 1      Upper consecutive offline limit exceeded");
    else:
        data.append("       bit 6   = 0      Upper consecutive offline limit not exceeded");

    if(int(bytes[3]) & int('00010000',2)):
        data.append("       bit 5   = 1      Transaction selected randomly for online processing");
    else:
        data.append("       bit 5   = 0      Transaction not selected randomly for online processing");

    if(int(bytes[3]) & int('00001000',2)):
        data.append("       bit 4   = 1      Merchant forced transaction online");
    else:
        data.append("       bit 4   = 0      Merchant did not force transaction online");

    if(int(bytes[3]) & int('00000100',2)):
        data.append("       bit 3   = 1      RFU");
    else:
        data.append("       bit 3   = 0      RFU");

    if(int(bytes[3]) & int('00000010',2)):
        data.append("       bit 2   = 1      RFU");
    else:
        data.append("       bit 2   = 0      RFU");

    if(int(bytes[3]) & int('00000001',2)):
        data.append("       bit 1   = 1      RFU");
    else:
        data.append("       bit 1   = 0      RFU");


    if (int(bytes[4]) & int('10000000',2)):
        data.append("Byte 5 bit 8   = 1      Default TDOL used");
    else:
        data.append("Byte 5 bit 8   = 0      No Default TDOL used");

    if (int(bytes[4]) & int('01000000',2)):
        data.append("       bit 7   = 1      Issuer authentication failed");
    else:
        data.append("       bit 7   = 0      Issuer authentication passed or not performed");

    if (int(bytes[4]) & int('00100000',2)):
        data.append("       bit 6   = 1      Script processing failed before final GENERATE AC");
    else:
        data.append("       bit 6   = 0      Script processing passed before final GENERATE AC or no script received");

    if (int(bytes[4]) & int('00010000',2)):
        data.append("       bit 5   = 1      Script processing failed after final GENERATE AC");
    else:
        data.append("       bit 5   = 0      Script processing passed after final GENERATE AC or no script received");

    if (int(bytes[4]) & int('00001000',2)):
        data.append("       bit 4   = 1      RFU");
    else:
        data.append("       bit 4   = 0      RFU");

    if (int(bytes[4]) & int('00000100',2)):
        data.append("       bit 3   = 1      RFU");
    else:
        data.append("       bit 3   = 0      RFU");

    if (int(bytes[4]) & int('00000010',2)):
        data.append("       bit 2   = 1      RFU");
    else:
        data.append("       bit 2   = 0      RFU");

    if (int(bytes[4]) & int('00000001',2)):
        data.append("       bit 1   = 1      RFU");
    else:
        data.append("       bit 1   = 0      RFU");
    return data

def term_cap_inter(termCap):
    bytes = bytearray.fromhex(termCap)
    data = []
    if  (int(bytes[0]) & int('10000000',2)):
         data.append("Byte 1 bit 8 = 1      Manual key entry is supported");
    else: 
         data.append("Byte 1 bit 8 = 0      Manual key entry is NOT supported");

    if  (int(bytes[0]) & int('01000000',2)):
         data.append("       bit 7 = 1      Magnetic stripe is supported");
    else:
         data.append("       bit 7 = 0      Magnetic stripe is NOT supported");

    if  (int(bytes[0]) & int('00100000',2)):
         data.append("       bit 6 = 1      IC with contacts is supported");
    else:
       data.append("       bit 6 = 0      IC with contacts is NOT supported");

    if  (int(bytes[0]) & int('00010000',2)):
         data.append("       bit 5 = 1      RFU");
    else:
       data.append("       bit 5 = 0      RFU");

    if  (int(bytes[0]) & int('00001000',2)):
         data.append("       bit 4 = 1      RFU");
    else:
       data.append("       bit 4 = 0      RFU");

    if  (int(bytes[0]) & int('00000100',2)):
         data.append("       bit 3 = 1      RFU");
    else:
       data.append("       bit 3 = 0      RFU");

    if  (int(bytes[0]) & int('00000010',2)):
         data.append("       bit 2 = 1      RFU");
    else:
       data.append("       bit 2 = 0      RFU");

    if  (int(bytes[0]) & int('00000001',2)):
         data.append("       bit 1 = 1      RFU");
    else:
       data.append("       bit 1 = 0      RFU");


    if  (int(bytes[1]) & int('10000000',2)):
         data.append("Byte 2 bit 8 = 1      Plaintext PIN for ICC verification is supported");
    else:
       data.append("Byte 2 bit 8 = 0      Plaintext PIN for ICC verification is NOT supported");

    if  (int(bytes[1]) & int('01000000',2)):
         data.append("       bit 7 = 1      Enciphered PIN for online verification is supported");
    else:
       data.append("       bit 7 = 0      Enciphered PIN for online verification is NOT supported");

    if  (int(bytes[1]) & int('00100000',2)):
         data.append("       bit 6 = 1      Signature (paper) is supported");
    else:
       data.append("       bit 6 = 0      Signature (paper) is NOT supported");

    if  (int(bytes[1]) & int('00010000',2)):
         data.append("       bit 5 = 1      Enciphered PIN for offline verification is supported");
    else:
       data.append("       bit 5 = 0      Enciphered PIN for offline verification is NOT supported");

    if  (int(bytes[1]) & int('00001000',2)):
         data.append("       bit 4 = 1      No CVM Required is supported");
    else:
       data.append("       bit 4 = 0      No CVM Required is NOT supported");

    if  (int(bytes[1]) & int('00000100',2)):
         data.append("       bit 3 = 1      RFU");
    else:
       data.append("       bit 3 = 0      RFU");

    if  (int(bytes[1]) & int('00000010',2)):
         data.append("       bit 2 = 1      RFU");
    else:
       data.append("       bit 2 = 0      RFU");

    if  (int(bytes[1]) & int('00000001',2)):
         data.append("       bit 1 = 1      RFU");
    else:
       data.append("       bit 1 = 0      RFU");


    if  (int(bytes[2]) & int('10000000',2)):
         data.append("Byte 3 bit 8 = 1      SDA is supported");
    else:
       data.append("Byte 3 bit 8 = 0      SDA is NOT supported");

    if  (int(bytes[2]) & int('01000000',2)):
         data.append("       bit 7 = 1      DDA is supported");
    else:
       data.append("       bit 7 = 0      DDA is NOT supported");

    if  (int(bytes[2]) & int('00100000',2)):
         data.append("       bit 6 = 1      Card capture is supported");
    else:
       data.append("       bit 6 = 0      Card capture is NOT supported");

    if  (int(bytes[2]) & int('00010000',2)):
         data.append("       bit 5 = 1      RFU");
    else:
       data.append("       bit 5 = 0      RFU");

    if  (int(bytes[2]) & int('00001000',2)):
         data.append("       bit 4 = 1      CDA is supported");
    else:
       data.append("       bit 4 = 0      CDA is NOT supported");

    if  (int(bytes[2]) & int('00000100',2)):
         data.append("       bit 3 = 1      RFU");
    else:
       data.append("       bit 3 = 0      RFU");

    if  (int(bytes[2]) & int('00000010',2)):
         data.append("       bit 2 = 1      RFU");
    else:
       data.append("       bit 2 = 0      RFU");

    if  (int(bytes[2]) & int('00000001',2)):
         data.append("       bit 1 = 1      RFU");
    else:
       data.append("       bit 1 = 0      RFU");
    
    return data    

def aip_inter(AIP):
    bytes = bytearray.fromhex(AIP)
    data = []
    if  ( int(bytes[0]) & int('10000000',2)):
         data.append("Byte 1 bit 8 = 1      RFU")
    else:  
         data.append("Byte 1 bit 8 = 0      RFU");

    if  ( int(bytes[0]) & int('01000000',2)):
         data.append("       bit 7 = 1      Offline static data authentication is supported");
    else:
         data.append("       bit 7 = 0      Offline static data authentication is NOT supported");

    if  ( int(bytes[0]) & int('00100000',2)):
         data.append("       bit 6 = 1      Offline dynamic data authentication is supported");
    else:
         data.append("       bit 6 = 0      Offline dynamic data authentication is NOT supported");

    if  ( int(bytes[0]) & int('00010000',2)):
         data.append("       bit 5 = 1      Cardholder verification is supported");
    else:
         data.append("       bit 5 = 0      Cardholder verification is NOT supported");

    if  ( int(bytes[0]) & int('00001000',2)):
         data.append("       bit 4 = 1      Terminal risk management is to be performed");
    else:
         data.append("       bit 4 = 0      Terminal risk management MAY NOT be performed");

    if  ( int(bytes[0]) & int('00000100',2)):
         data.append("       bit 3 = 1      Issuer authentication is supported");
    else:
         data.append("       bit 3 = 0      Issuer authentication is NOT supported");

    if  ( int(bytes[0]) & int('00000010',2)):
         data.append("       bit 2 = 1      Reserved for use by the EMV Contactless Specifications");
    else:
         data.append("       bit 2 = 0      Reserved for use by the EMV Contactless Specifications");

    if  ( int(bytes[0]) & int('00000001',2)):
         data.append("       bit 1 = 1      Combined DDA / GENERATE AC supported");
    else:
         data.append("       bit 1 = 0      Combined DDA / GENERATE AC NOT supported");

    if  ( int(bytes[1]) & int('10000000',2)):
         data.append("Byte 2 bit 8 = 1      EMV Contactless supported");
    else:
         data.append("Byte 2 bit 8 = 0      EMV Contactless NOT supported");

    if  ( int(bytes[1]) & int('01000000',2)):
         data.append("       bit 7 = 1      Reserved for use by the EMV Contactless Specifications");
    else:
         data.append("       bit 7 = 0      Reserved for use by the EMV Contactless Specifications");

    if  ( int(bytes[1]) & int('00100000',2)):
         data.append("       bit 6 = 1      RFU");
    else:
         data.append("       bit 6 = 0      RFU");

    if  ( int(bytes[1]) & int('00010000',2)):
         data.append("       bit 5 = 1      RFU");
    else:
         data.append("       bit 5 = 0      RFU");

    if  ( int(bytes[1]) & int('00001000',2)):
         data.append("       bit 4 = 1      RFU");
    else:
         data.append("       bit 4 = 0      RFU");

    if  ( int(bytes[1]) & int('00000100',2)):
         data.append("       bit 3 = 1      RFU");
    else:
         data.append("       bit 3 = 0      RFU");

    if  ( int(bytes[1]) & int('00000010',2)):
         data.append("       bit 2 = 1      RFU");
    else:
         data.append("       bit 2 = 0      RFU");

    if  ( int(bytes[1]) & int('00000001',2)):
         data.append("       bit 1 = 1      RFU");
    else:
         data.append("       bit 1 = 0      RFU");
    return data

def tsi_inter(tsi):
    data = []
    bytes=bytearray.fromhex(tsi)

    if (int(bytes[0]) & int('10000000',2)):
        data.append("Byte 1 bit 8 = 1      Offline data authentication was performed");
    else:
        data.append("Byte 1 bit 8 = 0      Offline data authentication was NOT performed");

    if  (int(bytes[0]) & int('01000000',2)):
        data.append("       bit 7 = 1      Cardholder verification was performed");
    else:
        data.append("       bit 7 = 0      Cardholder verification was NOT performed");

    if  (int(bytes[0]) & int('00100000',2)):
        data.append("       bit 6 = 1      Card risk management was performed");
    else:
        data.append("       bit 6 = 0      Card risk management was NOT performed");

    if  (int(bytes[0]) & int('00010000',2)):
        data.append("       bit 5 = 1      Issuer authentication was performed");
    else:
        data.append("       bit 5 = 0      Issuer authentication was NOT performed");

    if  (int(bytes[0]) & int('00001000',2)):
        data.append("       bit 4 = 1      Terminal risk management was performed");
    else:
        data.append("       bit 4 = 0      Terminal risk management was NOT performed");

    if  (int(bytes[0]) & int('00000100',2)):
        data.append("       bit 3 = 1      Script processing was performed");
    else:
        data.append("       bit 3 = 0      Script processing was NOT performed");

    if  (int(bytes[0]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[0]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if  (int(bytes[1]) & int('10000000',2)):
        data.append("Byte 2 bit 8 = 1      RFU");
    else:
        data.append("Byte 2 bit 8 = 0      RFU");

    if  (int(bytes[1]) & int('01000000',2)):
        data.append("       bit 7 = 1      RFU");
    else:
        data.append("       bit 7 = 0      RFU");

    if  (int(bytes[1]) & int('00100000',2)):
        data.append("       bit 6 = 1      RFU");
    else:
        data.append("       bit 6 = 0      RFU");

    if  (int(bytes[1]) & int('00010000',2)):
        data.append("       bit 5 = 1      RFU");
    else:
        data.append("       bit 5 = 0      RFU");

    if  (int(bytes[1]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[1]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[1]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[1]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");

    return data

def add_term_cap_inter(add_term_cap):
    bytes = bytearray.fromhex(add_term_cap)
    data = []
    if (int(bytes[0]) & int('10000000',2)):
        data.append("Byte 1 bit 8 = 1      Cash supported");
    else:
        data.append("Byte 1 bit 8 = 0      Cash NOT supported");

    if  (int(bytes[0]) & int('01000000',2)):
        data.append("       bit 7 = 1      Goods supported");
    else:
        data.append("       bit 7 = 0      Goods NOT supported");

    if  (int(bytes[0]) & int('00100000',2)):
        data.append("       bit 6 = 1      Services supported");
    else:
        data.append("       bit 6 = 0      Services NOT supported");

    if  (int(bytes[0]) & int('00010000',2)):
        data.append("       bit 5 = 1      Cashback supported");
    else:
        data.append("       bit 5 = 0      CashBack NOT supported");

    if  (int(bytes[0]) & int('00001000',2)):
        data.append("       bit 4 = 1      Inquiry supported");
    else:
        data.append("       bit 4 = 0      Inquiry NOT supported");

    if  (int(bytes[0]) & int('00000100',2)):
        data.append("       bit 3 = 1      Transfer supported");
    else:
        data.append("       bit 3 = 0      Transfer NOT supported");

    if  (int(bytes[0]) & int('00000010',2)):
        data.append("       bit 2 = 1      Payment supported");
    else:
        data.append("       bit 2 = 0      Payment NOT supported");

    if  (int(bytes[0]) & int('00000001',2)):
        data.append("       bit 1 = 1      Administrative supported");
    else:
        data.append("       bit 1 = 0      Administrative NOT supported");


    if (int(bytes[1]) & int('10000000',2)):
        data.append("Byte 2 bit 8 = 1      CashBack Deposit supported");
    else:
        data.append("Byte 2 bit 8 = 0      CashBack Deposit NOT supported");

    if  (int(bytes[1]) & int('01000000',2)):
        data.append("       bit 7 = 1      RFU");
    else:
        data.append("       bit 7 = 0      RFU");

    if  (int(bytes[1]) & int('00100000',2)):
        data.append("       bit 6 = 1      RFU");
    else:
        data.append("       bit 6 = 0      RFU");

    if  (int(bytes[1]) & int('00010000',2)):
        data.append("       bit 5 = 1      RFU");
    else:
        data.append("       bit 5 = 0      RFU");

    if  (int(bytes[1]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[1]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[1]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[1]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");

    if (int(bytes[2]) & int('10000000',2)):
        data.append("Byte 3 bit 8 = 1      Numeric keys supported");
    else:
        data.append("Byte 3 bit 8 = 0      Numeric keys NOT supported");

    if  (int(bytes[2]) & int('01000000',2)):
        data.append("       bit 7 = 1      Alphabetic and special characters keys supported");
    else:
        data.append("       bit 7 = 0      Alphabetic and special characters keys NOT supported");

    if  (int(bytes[2]) & int('00100000',2)):
        data.append("       bit 6 = 1      Command keys supported");
    else:
        data.append("       bit 6 = 0      Command keys NOT supported");

    if  (int(bytes[2]) & int('00010000',2)):
        data.append("       bit 5 = 1      Function keys supported");
    else:
        data.append("       bit 5 = 0      Function keys NOT supported");

    if  (int(bytes[2]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[2]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[2]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[2]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if (int(bytes[3]) & int('10000000',2)):
        data.append("Byte 4 bit 8 = 1      Print, attendant supported");
    else:
        data.append("Byte 4 bit 8 = 0      Print, attendant NOT supported");

    if  (int(bytes[3]) & int('01000000',2)):
        data.append("       bit 7 = 1      Print, cardholder supported");
    else:
        data.append("       bit 7 = 0      Print, cardholder NOT supported");

    if  (int(bytes[3]) & int('00100000',2)):
        data.append("       bit 6 = 1      Display, attendant supported");
    else:
        data.append("       bit 6 = 0      Display, attendant NOT supported");

    if  (int(bytes[3]) & int('00010000',2)):
        data.append("       bit 5 = 1      Display, cardholder supported");
    else:
        data.append("       bit 5 = 0      Display, cardholder NOT supported");

    if  (int(bytes[3]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[3]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[3]) & int('00000010',2)):
        data.append("       bit 2 = 1      Code table 10 supported");
    else:
        data.append("       bit 2 = 0      Code table 10 NOT supported");

    if  (int(bytes[3]) & int('00000001',2)):
        data.append("       bit 1 = 1      Code table 9 supported");
    else:
        data.append("       bit 1 = 0      Code table 9 NOT supported");


    if (int(bytes[4]) & int('10000000',2)):
        data.append("Byte 5 bit 8 = 1      Code table 8 supported");
    else:
        data.append("Byte 5 bit 8 = 0      Code table 8 NOT supported");

    if  (int(bytes[4]) & int('01000000',2)):
        data.append("       bit 7 = 1      Code table 7 supported");
    else:
        data.append("       bit 7 = 0      Code table 7 NOT supported");

    if  (int(bytes[4]) & int('00100000',2)):
        data.append("       bit 6 = 1      Code table 6 supported");
    else:
        data.append("       bit 6 = 0      Code table 6 NOT supported");

    if  (int(bytes[4]) & int('00010000',2)):
        data.append("       bit 5 = 1      Code table 5 supported");
    else:
        data.append("       bit 5 = 0      Code table 5 NOT supported");

    if  (int(bytes[4]) & int('00001000',2)):
        data.append("       bit 4 = 1      Code table 4 supported");
    else:
        data.append("       bit 4 = 0      Code table 4 NOT supported");

    if  (int(bytes[4]) & int('00000100',2)):
        data.append("       bit 3 = 1      Code table 3 supported");
    else:
        data.append("       bit 3 = 0      Code table 3 NOT supported");

    if  (int(bytes[4]) & int('00000010',2)):
        data.append("       bit 2 = 1      Code table 2 supported");
    else:
        data.append("       bit 2 = 0      Code table 2 NOT supported");

    if  (int(bytes[4]) & int('00000001',2)):
        data.append("       bit 1 = 1      Code table 1 supported");
    else:
        data.append("       bit 1 = 0      Code table 1 NOT supported");

    return data

def action_codes_inter(action_code,TACDEF,TACDEN,TACONL):
    bytes = bytearray.fromhex(action_code)
    data = []
    if(TACDEN):
        action = "Decline"
    elif(TACONL):
        action = "Go online"
    else:
        action = "Reject if unable to process online and"

    if  (int(bytes[0]) & int('10000000',2)):
        data.append("Byte 1 bit 8 = 1      "+action+" if Offline data authentication was not performed");
    else:
        data.append("Byte 1 bit 8 = 0      Do not "+action+" if Offline data authentication was not performed");

    if  (int(bytes[0]) & int('01000000',2)):
        data.append("       bit 7 = 1      "+action+" if Offline static data authentication failed");
    else:
        data.append("       bit 7 = 0      Do not "+action+" if Offline static data authentication failed");

    if  (int(bytes[0]) & int('00100000',2)):
        data.append("       bit 6 = 1      "+action+" if ICC data missing");
    else:
        data.append("       bit 6 = 0      Do not "+action+" if ICC data missing");

    if  (int(bytes[0]) & int('00010000',2)):
        data.append("       bit 5 = 1      "+action+" if Card appears on terminal exception file");
    else:
        data.append("       bit 5 = 0      Do not "+action+" if Card appears on terminal exception file");

    if  (int(bytes[0]) & int('00001000',2)):
        data.append("       bit 4 = 1      "+action+" if Offline dynamic data authentication failed");
    else:
        data.append("       bit 4 = 0      Do not "+action+" if Offline dynamic data authentication failed");

    if  (int(bytes[0]) & int('00000100',2)):
        data.append("       bit 3 = 1      "+action+" if Combined DDA/AC Generation failed");
    else:
        data.append("       bit 3 = 0      Do not "+action+" if Combined DDA/AC Generation failed");

    if  (int(bytes[0]) & int('00000010',2)):
        data.append("       bit 2 = 1      "+action+" if SDA selected");
    else:
        data.append("       bit 2 = 0      Do not "+action+" if SDA selected");

    if  (int(bytes[0]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if  (int(bytes[1]) & int('10000000',2)):
        data.append("Byte 2 bit 8 = 1      "+action+" if ICC and terminal have different application versions");
    else:
        data.append("Byte 2 bit 8 = 0      Do not "+action+" if ICC and terminal have different application versions");

    if  (int(bytes[1]) & int('01000000',2)):
        data.append("       bit 7 = 1      "+action+" if Expired application");
    else:
        data.append("       bit 7 = 0      Do not "+action+" if Expired application");

    if  (int(bytes[1]) & int('00100000',2)):
        data.append("       bit 6 = 1      "+action+" if Application not yet effective");
    else:
        data.append("       bit 6 = 0      Do not "+action+" if Application not yet effective");

    if  (int(bytes[1]) & int('00010000',2)):
        data.append("       bit 5 = 1      "+action+" if Requested service not allowed for card product");
    else:
        data.append("       bit 5 = 0      Do not "+action+" if Requested service not allowed for card product");

    if  (int(bytes[1]) & int('00001000',2)):
        data.append("       bit 4 = 1      "+action+" if New card");
    else:
        data.append("       bit 4 = 0      Do not "+action+" if New card");

    if  (int(bytes[1]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[1]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[1]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if  (int(bytes[2]) & int('10000000',2)):
        data.append("Byte 3 bit 8 = 1      "+action+" if Cardholder verification was not successful");
    else:
        data.append("Byte 3 bit 8 = 0      Do not "+action+" if Cardholder verification was not successful");

    if  (int(bytes[2]) & int('01000000',2)):
        data.append("       bit 7 = 1      "+action+" if Unrecognised CVM");
    else:
        data.append("       bit 7 = 0      Do not "+action+" if Unrecognised CVM");

    if  (int(bytes[2]) & int('00100000',2)):
        data.append("       bit 6 = 1      "+action+" if PIN Try Limit exceeded");
    else:
        data.append("       bit 6 = 0      Do not "+action+" if PIN Try Limit exceeded");

    if  (int(bytes[2]) & int('00010000',2)):
        data.append("       bit 5 = 1      "+action+" if PIN entry required and PIN pad not present or not working");
    else:
        data.append("       bit 5 = 0      Do not "+action+" if PIN entry required and PIN pad not present or not working");

    if  (int(bytes[2]) & int('00001000',2)):
        data.append("       bit 4 = 1      "+action+" if PIN entry required, PIN pad present, but PIN was not entered");
    else:
        data.append("       bit 4 = 0      Do not "+action+" if PIN entry required, PIN pad present, but PIN was not entered");

    if  (int(bytes[2]) & int('00000100',2)):
        data.append("       bit 3 = 1      "+action+" if Online PIN entered");
    else:
        data.append("       bit 3 = 0      Do not "+action+" if Online PIN entered");

    if  (int(bytes[2]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[2]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if  (int(bytes[3]) & int('10000000',2)):
        data.append("Byte 4 bit 8 = 1      "+action+" if Transaction exceeds floor limit");
    else:
        data.append("Byte 4 bit 8 = 0      Do not "+action+" if Transaction exceeds floor limit");

    if  (int(bytes[3]) & int('01000000',2)):
        data.append("       bit 7 = 1      "+action+" if Lower consecutive offline limit exceeded");
    else:
        data.append("       bit 7 = 0      Do not "+action+" if Lower consecutive offline limit exceeded");

    if  (int(bytes[3]) & int('00100000',2)):
        data.append("       bit 6 = 1      "+action+" if Upper consecutive offline limit exceeded");
    else:
        data.append("       bit 6 = 0      Do not "+action+" if Upper consecutive offline limit exceeded");

    if  (int(bytes[3]) & int('00010000',2)):
        data.append("       bit 5 = 1      "+action+" if Transaction selected randomly for online processing");
    else:
        data.append("       bit 5 = 0      Do not "+action+" if Transaction selected randomly for online processing");

    if  (int(bytes[3]) & int('00001000',2)):
        data.append("       bit 4 = 1      "+action+" if Merchant forced transaction online");
    else:
        data.append("       bit 4 = 0      Do not "+action+" if Merchant forced transaction online");

    if  (int(bytes[3]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[3]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[3]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if  (int(bytes[4]) & int('10000000',2)):
        data.append("Byte 5 bit 8 = 1      "+action+" if Default TDOL used");
    else:
        data.append("Byte 5 bit 8 = 0      Do not "+action+" if Default TDOL used");

    if  (int(bytes[4]) & int('01000000',2)):
        data.append("       bit 7 = 1      "+action+" if Issuer authentication was unsuccessful");
    else:
        data.append("       bit 7 = 0      Do not "+action+" if Issuer authentication was unsuccessful");

    if  (int(bytes[4]) & int('00100000',2)):
        data.append("       bit 6 = 1      "+action+" if Script processing failed before final GENERATE AC");
    else:
        data.append("       bit 6 = 0      Do not "+action+" if Script processing failed before final GENERATE AC");

    if  (int(bytes[4]) & int('00010000',2)):
        data.append("       bit 5 = 1      "+action+" if Script processing failed after final GENERATE AC");
    else:
        data.append("       bit 5 = 0      Do not "+action+" if Script processing failed after final GENERATE AC");

    if  (int(bytes[4]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[4]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[4]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[4]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");
    return data

def tacdef_inter(TACDEF):
    return action_codes_inter(TACDEF,1,0,0)

def tacden_inter(TACDEN):
    return action_codes_inter(TACDEN,0,1,0)

def taconl_inter(TACONL):
    return action_codes_inter(TACONL,0,0,1)

def ttq_inter(ttq):
    bytes = bytearray.fromhex(ttq)
    data = []
    
    if (int(bytes[0]) & int('10000000',2)):
        data.append("Byte 1 bit 8 = 1      Contactless MSD supported");
    else:
        data.append("Byte 1 bit 8 = 0      Contactless MSD NOT supported");

    if  (int(bytes[0]) & int('01000000',2)):
        data.append("       bit 7 = 1      Contactless VSDC supported");
    else:
        data.append("       bit 7 = 0      Contactless VSDC NOT supported");

    if  (int(bytes[0]) & int('00100000',2)):
        data.append("       bit 6 = 1      Contactless qVSDC supported");
    else:
        data.append("       bit 6 = 0      Contactless qVSDC NOT supported");

    if  (int(bytes[0]) & int('00010000',2)):
        data.append("       bit 5 = 1      EMV contact chip supported");
    else:
        data.append("       bit 5 = 0      EMV contact chip NOT supported");

    if  (int(bytes[0]) & int('00001000',2)):
        data.append("       bit 4 = 1      Offline-only reader");
    else:
        data.append("       bit 4 = 0      NOT Offline-only reader");

    if  (int(bytes[0]) & int('00000100',2)):
        data.append("       bit 3 = 1      Online PIN supported");
    else:
        data.append("       bit 3 = 0      Online PIN NOT supported");

    if  (int(bytes[0]) & int('00000010',2)):
        data.append("       bit 2 = 1      Signature supported");
    else:
        data.append("       bit 2 = 0      Signature NOT supported");

    if  (int(bytes[0]) & int('00000001',2)):
        data.append("       bit 1 = 1      Offline Data Authentication (ODA) for Online Authorizations supported.");
    else:
        data.append("       bit 1 = 0      Offline Data Authentication (ODA) for Online Authorizations NOT supported.");


    if (int(bytes[1]) & int('10000000',2)):
        data.append("Byte 2 bit 8 = 1      Online cryptogram required");
    else:
        data.append("Byte 2 bit 8 = 0      Online cryptogram NOT required");

    if  (int(bytes[1]) & int('01000000',2)):
        data.append("       bit 7 = 1      CVM required");
    else:
        data.append("       bit 7 = 0      CVM NOT required");

    if  (int(bytes[1]) & int('00100000',2)):
        data.append("       bit 6 = 1      (Contact Chip) Offline PIN supported");
    else:
        data.append("       bit 6 = 0      (Contact Chip) Offline PIN NOT supported");

    if  (int(bytes[1]) & int('00010000',2)):
        data.append("       bit 5 = 1      RFU");
    else:
        data.append("       bit 5 = 0      RFU");

    if  (int(bytes[1]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[1]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[1]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[1]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");

    if (int(bytes[2]) & int('10000000',2)):
        data.append("Byte 3 bit 8 = 1      Issuer Update Processing Supported");
    else:
        data.append("Byte 3 bit 8 = 0      Issuer Update Processing NOT Supported");

    if  (int(bytes[2]) & int('01000000',2)):
        data.append("       bit 7 = 1      Mobile functionality supported (Consumer Device CVM)");
    else:
        data.append("       bit 7 = 0      Mobile functionality NOT supported (Consumer Device CVM)");

    if  (int(bytes[2]) & int('00100000',2)):
        data.append("       bit 6 = 1      RFU");
    else:
        data.append("       bit 6 = 0      RFU");

    if  (int(bytes[2]) & int('00010000',2)):
        data.append("       bit 5 = 1      RFU");
    else:
        data.append("       bit 5 = 0      RFU");

    if  (int(bytes[2]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[2]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[2]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[2]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");

    if (int(bytes[2]) & int('10000000',2)):
        data.append("Byte 4 bit 8 = 1      RFU");
    else:
        data.append("Byte 4 bit 8 = 0      RFU");

    if  (int(bytes[2]) & int('01000000',2)):
        data.append("       bit 7 = 1      RFU");
    else:
        data.append("       bit 7 = 0      RFU");

    if  (int(bytes[2]) & int('00100000',2)):
        data.append("       bit 6 = 1      RFU");
    else:
        data.append("       bit 6 = 0      RFU");

    if  (int(bytes[2]) & int('00010000',2)):
        data.append("       bit 5 = 1      RFU");
    else:
        data.append("       bit 5 = 0      RFU");

    if  (int(bytes[2]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[2]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[2]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[2]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");

    return data

def ctq_inter(ctq):    
    bytes = bytearray.fromhex(ttq)
    data = []
    
    if (int(bytes[0]) & int('10000000',2)):
        data.append("Byte 1 bit 8 = 1      Online PIN Required");
    else:
        data.append("Byte 1 bit 8 = 0      Online PIN NOT Required");

    if  (int(bytes[0]) & int('01000000',2)):
        data.append("       bit 7 = 1      Signature Required");
    else:
        data.append("       bit 7 = 0      Signature NOT Required");

    if  (int(bytes[0]) & int('00100000',2)):
        data.append("       bit 6 = 1      Go Online if Offline Data Authentication Fails and Reader is online capable.");
    else:
        data.append("       bit 6 = 0      NOT go Online if Offline Data Authentication Fails and Reader is online capable.");

    if  (int(bytes[0]) & int('00010000',2)):
        data.append("       bit 5 = 1      Switch Interface if Offline Data Authentication fails and Reader supports VIS.");
    else:
        data.append("       bit 5 = 0      Dont switch Interface if Offline Data Authentication fails and Reader supports VIS.");

    if  (int(bytes[0]) & int('00001000',2)):
        data.append("       bit 4 = 1      Go Online if Application Expired.");
    else:
        data.append("       bit 4 = 0      Dont go Online if Application Expired.");

    if  (int(bytes[0]) & int('00000100',2)):
        data.append("       bit 3 = 1      Switch Interface for CashTransactions.");
    else:
        data.append("       bit 3 = 0      Dont switch Interface for CashTransactions.");

    if  (int(bytes[0]) & int('00000010',2)):
        data.append("       bit 2 = 1      Switch Interface for Cashback Transactions");
    else:
        data.append("       bit 2 = 0      Dont switch Interface for Cashback Transactions");

    if  (int(bytes[0]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");


    if (int(bytes[1]) & int('10000000',2)):
        data.append("Byte 2 bit 8 = 1      Consumer Device CVM Performed.Note: Bit 8 is not used by cards compliant with VISA specification, and is commonly set to False.");
    else:
        data.append("Byte 2 bit 8 = 0      Consumer Device CVM NOT Performed.Note: Bit 8 is not used by cards compliant with VISA specification, and is commonly set to False.");

    if  (int(bytes[1]) & int('01000000',2)):
        data.append("       bit 7 = 1      Card supports Issuer Update Processing at the POS.");
    else:
        data.append("       bit 7 = 0      Card NOT supports Issuer Update Processing at the POS.");

    if  (int(bytes[1]) & int('00100000',2)):
        data.append("       bit 6 = 1      RFU");
    else:
        data.append("       bit 6 = 0      RFU");

    if  (int(bytes[1]) & int('00010000',2)):
        data.append("       bit 5 = 1      RFU");
    else:
        data.append("       bit 5 = 0      RFU");

    if  (int(bytes[1]) & int('00001000',2)):
        data.append("       bit 4 = 1      RFU");
    else:
        data.append("       bit 4 = 0      RFU");

    if  (int(bytes[1]) & int('00000100',2)):
        data.append("       bit 3 = 1      RFU");
    else:
        data.append("       bit 3 = 0      RFU");

    if  (int(bytes[1]) & int('00000010',2)):
        data.append("       bit 2 = 1      RFU");
    else:
        data.append("       bit 2 = 0      RFU");

    if  (int(bytes[1]) & int('00000001',2)):
        data.append("       bit 1 = 1      RFU");
    else:
        data.append("       bit 1 = 0      RFU");
    return data


def resp_code_inter( respCode ):
    data = []
    switch = {
        "00"  : "Approved or completed succesfully",
        "01"  : "Refer to card issuer",
        "02"  : "Refer to card issuer special conditions",
        "03"  : "Invalid merchant",
        "04"  : "Pick-up",
        "05"  : "Do not honour",
        "06"  : "Error",
        "07"  : "Pick-up card special condition",
        "08"  : "Honour with identification",
        "09"  : "Request in progress",
        "10"  : "Approved for partial amount",
        "Y1"  : "Requesting for offline approval",
        "Z1"  : "Requesting for offline decline",
  
        "Y2"  : "Approved (after card-initiated referral)",
        "Z2"  : "Declined (after card-initiated referral)",
        "Y3"  : "Unable to go online, Requesting for offline approval",
        "Z3"  : "Unable to go online, Requesting for offline decline",
    }
    if(respCode in switch):
        data.append(switch.get(respCode))
    return data
"""
def cvr_inter( cvm ):
    bytes = bytearray.fromhex( cvm )

    CVMtype = {
        "0x0"  : "       bit 6-1= 000000 (Fail CVM processing)",
        "0x1"  : "       bit 6-1= 000001 (Plaintext PIN verification performed by ICC)",
        "0x2"  : "       bit 6-1= 000010 (Enciphered PIN verified online)",
        "0x3"  : "       bit 6-1= 000011 (Plaintext PIN verification performed by ICC and signature (paper))",
        "0x4"  : "       bit 6-1= 000100 (Enciphered PIN verification performed by ICC)",
        "0x5"  : "       bit 6-1= 000101 (Enciphered PIN verification performed by ICC and signature (paper))",
        "0x1e"  : "       bit 6-1= 011110 (Signature (paper))",
        "0x1f"  : "       bit 6-1= 011111 (No CVM required)",
        "0x3e"  : "       bit 6-1= 111111 (Not available for use)",
    }

    print( CVMtype.get(hex(int(bin(bytes[0])[4:],2))))
 
    if( int(bytes[0]) & int('10000000',2)):
        print("Byte 1 bit 8  = 1      (default value is 0)")
    else:  
        print("Byte 1 bit 8  = 0      (default value)")
  
    if( int(bytes[0]) & int('01000000',2)):
        print("       bit 7  = 1      (Apply succeeding CVM field if this CVM is unsuccessful)")
    else : 
        print("       bit 7  = 0      (Fail Cardholder Verification if this CVM is unsuccessful))")

    CVMRule = {
        '00'  : "Byte 2        = '00'   (Always)",
        '01'  : "Byte 2        = '01'   (If unattended cash)",
        '02'  : "Byte 2        = '02'   (If not unattended cash and not manual cash and not purchase with cashback)",
        '03'  : "Byte 2        = '03'   (If terminal supports the CVM type)",
        '04'  : "Byte 2        = '04'   (If manual cash)",
        '05'  : "Byte 2        = '05'   (If purchase with cashback)",
        '06'  : "Byte 2        = '06'   (If transaction is in Application Currency Code and is under X value)",
        '07'  : "Byte 2        = '07'   (If transaction is in Application Currency Code and is over X value)",
        '08'  : "Byte 2        = '08'   (If transaction is in Application Currency Code and is under Y value)",
        '09'  : "Byte 2        = '09'   (If transaction is in Application Currency Code and is over Y value)",
    }

    print(CVMRule.get(cvm[2:4]))

    result = {
        '00' : "Byte 3        = '00'   (Unknown)",
        '01' : "Byte 3        = '01'   (Failed)",
        '02' : "Byte 3        = '02'   (Successful)",
    }

    print(result.get(cvm[4:]))




proc InterpretTrack1Data(data, mask, masker):
{
  EquivalentData:
  {
    FormatCode    : '42';
    PAN           : '??'{0-19};
    PAN_SF        : '5E';
    Name          : '??'{2-26};
    PAN_SF2       : '5E';
    ExpDate       : '?? ?? ?? ??';
    ServCode      : '?? ?? ??';
    DiscrData     : *;
  };

  var H_data = data;
  try
  {
    compare data, EquivalentData -> H_data;
  }
  passed:
  {
    print("Format Code              = " ++ ByteToHex(H_data.FormatCode));
    var pan = "";
    MaskPAN('01', H_data.PAN, var pan, masker, mask);
    pan = GetHexOutput(pan);
    print("PAN                      = " ++ pan);
    print("Separator field          = " ++ ByteToHex(H_data.PAN_SF));
    print("Name                     = " ++ H_data.Name);
    print("Separator field          = " ++ ByteToHex(H_data.PAN_SF2));
    print("Expiry Date (YY/MM)      = " ++ Sub(H_data.ExpDate, 0, 2) ++ "/" ++ Sub(H_data.ExpDate, 2, 2));
    print("Service Code             = " ++ AlignRight(FilterString(H_data.ServCode, " "), "   "));
    print("Discretionary Data       = " ++ H_data.DiscrData);
  }
  failed:
  {
    Log("W", "Data could not be interpreted correctly.");
  }
};

//------------------------------------------------------------------------------


proc InterpretTrack2EquivalentData(data):
{
  InterpretTrack2EquivalentData(data, 0, "");
};

proc InterpretTrack2EquivalentData(data, mask, masker):
{
  EquivalentData:
  {
    PAN           : *;
    SF_ExpDate_SC : 'D? ?? ?? ??';
    DiscrData     : *;
  };

  EquivalentData2:
  {
    PAN           : *;
    PAN_SF        : '?D';
    ExpDate       : '?? ??';
    ServCode      : '?? ??';
    DiscrData     : *;
  };

  var H_data = data;
  try match H_data, EquivalentData;
  passed:
  {
    compare H_data, EquivalentData->H_data;
    var pan = "";
    MaskPAN('57', H_data.PAN, var pan, masker, mask);
    print("PAN                      = "++FilterString(pan," "));

    var v_xdate = Sub(H_data.SF_ExpDate_SC,0,3)>>4; v_xdate = Sub(v_xdate,1,2);
    var v_SC    = (Sub(H_data.SF_ExpDate_SC,2,2) and '0F FF');
    LogD("Separator field          = D");
    LogD("Expiry Date (YY/MM)      = "++ByteToHex(Sub(v_xdate,0,1))++"/"++ByteToHex(Sub(v_xdate,1,1)));
    LogD("Service Code             = "++AlignRight(FilterString(ByteToHex(v_SC)," "),"   "));
    LogD("Discretionary Data       = "++FilterString(ByteToHex(H_data.DiscrData)," "));
    LogD("(may be padded with one 'F')");
  }
  failed:
  {
    try match H_data, EquivalentData2;
    passed:
    {
      compare H_data, EquivalentData2->H_data;
      var l = Length(FilterString(ByteToHex(H_data.PAN)++" "++ByteToHex(H_data.PAN_SF)," "))-1;
      var spaces = "";
      for (var i=1;i<=l;i=i+1) spaces = spaces ++ " ";
      var pan = "";
      MaskPAN('57', H_data.PAN++H_data.PAN_SF, var pan, masker, mask);
      LogD("PAN                      = "++AlignLeft(FilterString(pan," "),spaces));
      LogD("Separator field          = D");
      LogD("Expiry Date              = "++ByteToHex(Sub(H_data.ExpDate,0,1))++"/"++ByteToHex(Sub(H_data.ExpDate,1,1)));
      LogD("Service Code             = "++AlignLeft(FilterString(ByteToHex(H_data.ServCode)," "),"   "));
      l = Length(FilterString(ByteToHex(( Sub(H_data.ServCode,1,1)++H_data.DiscrData) )," "))-1;
      spaces = "";
      for (var i=1;i<=l;i=i+1) spaces = spaces ++ " ";
      LogD("Discretionary Data       = "++AlignRight(FilterString(ByteToHex(( Sub(H_data.ServCode,1,1)++H_data.DiscrData) )," "),spaces));
      LogD("(may be padded with one 'F')");
    }
    failed:
    {
      Log("W", "No separator nibble 'D' found, data could not be interpreted correctly.");
    }
  }
};

//-----

roc InterpretCryptogramInformationData(cid):
{
  if (Length(cid) == 1)
  {
    switch (cid)
    {
      '00??????'b : LogD("Byte 1 bit 8-7 = 00     AAC");
      '01??????'b : LogD("Byte 1 bit 8-7 = 01     TC");
      '10??????'b : LogD("Byte 1 bit 8-7 = 10     ARQC");
      '11??????'b : LogD("Byte 1 bit 8-7 = 11     AAR");
    }

    switch (cid)
    {
      '??00????'b : Log_("       bit 6-5 = 00     Payment System specific cryptogram");
      '??01????'b : Log_("       bit 6-5 = 01     Payment System specific cryptogram");
      '??10????'b : Log_("       bit 6-5 = 10     Payment System specific cryptogram");
      '??11????'b : Log_("       bit 6-5 = 11     Payment System specific cryptogram");
    }

    switch (cid)
    {
      '????0???'b : Log_("       bit 4   = 0      No advice required");
      '????1???'b : Log_("       bit 4   = 1      Advice required");
    }

    switch (cid)
    {
      '?????000'b : Log_("       bit 3-1 = 000    No information given");
      '?????001'b : Log_("       bit 3-1 = 001    Service not allowed");
      '?????010'b : Log_("       bit 3-1 = 010    PIN Try Limit exceeded");
      '?????011'b : Log_("       bit 3-1 = 011    Issuer authentication failed");
      * :           Log_("       bit 3-1 = " ++ AlignRight(ByteToString(cid and '00000111'b,2),"000") ++   "    RFU");
    }
  }
  else
  {
    LogD("Length of CID is not 1 byte, interpretation not possible");
  }
};
'''"""