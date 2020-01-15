import http.client 
import os
import ssl

>>> h1 = http.client.HTTPConnection('https://192.168.2.188', 8091)
<http:client.HTTPConnection at 0x7f1742c47710>
>>> h1.request("GET", "/")
gaierror: [[Errno -5] No address associated with hostname

>>> h1 = http.client.HTTPConnection('https://192.168.2.118', 8091)
>>> h1.request("GET", "/")
gaierror: [[Errno -2] Name or service not known

>>> h3 = http.cllient.HTTPConnection('https://www.python.org')
InvalidURL: nonnumeirc port: '//www.python.org'

>>> h3 = http.cllient.HTTPConnection('www.python.org')
>>> h3.request("GET", "/")
>>> data3 = h3.read()
AttributeError: 'HTTPConnection' object has no attribute 'read'

>>> h4 = http.cllient.HTTPSConnection('www.python.org')
>>> h4.request("GET", "/")
>>> print(h4.status, h4.reason)
AttributeError: 'HTTPSConnection' object has no attribute 'status'

>>>r4 = h4.getresponse
<bound method HTTPConnection.getresponse of <http.client.HTTPSConnectio
n object at 0x7f17423331d0>>
""" (wrong typing, is this a method? ??) """
>>> print(r4.status, r4.reason)
AttributeError: 'function' object has no attribute 'status'

>>> r4 = h4.getresponse()
>>> print(r4.status, r4.reason)
200 OK
>>> data4 = r4.read()
>>> data4
b'<!doctype html> ... </html>\n'

>>> h4.close()
""" Good job """




>>> h5 = http.client.HTTPSConnection('https://192.168.2.118', 8091)
>>> h5.request("GET", "/")
gaierror: [[Errno -2] Name or service not known
""" your hostname is wrong """

>>> h6 = http.client.HTTPSConnection('https://192.168.2.118', 8091, key_fil
    e='~/Downloads/PODM_keypair/pi.key', cert_file='~/Downloads/PODM_keypai
    r/pi.crt')
FileNotFoundError                    Traceback (most recent call last)
FileNotFoundError: [[Errno 2] No such file or directory
""" can not use relative path """

>>> h6 = http.client.HTTPSConnection('https://192.168.2.118', 8091, key_fil
    e='/home/jlo/Downloads/PODM_keypair/pi.key', cert_file='/home/jlo/Downl
    oads/PODM_keypair/pi.crt')
>>> h6.request("GET", "/")
gaierror                             Traceback (most recent call last)
gaierror: [[Errno -2] Name or service not known

>>> h7 = http.client.HTTPSConnection('192.168.2.118', 8091, key_file='/home
    /jlo/Downloads/PODM_keypair/pi.key', cert_file='/home/jlo/Downloads/POD
    M_keypair/pi.crt')
>>> h7.request("GET", "/")
SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:645
)

>>> h7.request("GET", "/")
CannotSendRequest: Request-sent










ssl.PROTOCOL_TLSv1
ssl.PROTOCOL_TLSv1.1
ssl.PROTOCOL_TLSv1.2

>>> s = ssl.sslContext
Type Error               Traceback (most recent call last)
Type Error: __new__() missing 1 required positional argument: 'protocol'



>>> s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

>>> s.verify_mode = ssl.CERT_REQUIRED
>>> s.vefigy_mode
2
>>> 

ssl. verify_mode		value
ssl.CERT_NONE			0
ssl.CERT_OPTIONAL		1
ssl.CERT_REQUIRED		2


client / server 	SSLv2 	SSLv3 	TLS 	TLSv1   TLSv1.1 TLSv1.2
SSLv2                   yes 	no 	yes 	no 	no 	no
SSLv3                   no 	yes 	yes 	no 	no 	no
TLS (SSLv23) 	        no 	yes 	yes 	yes 	yes 	yes
TLSv1 	                no 	no 	yes 	yes 	no 	no
TLSv1.1 	        no 	no 	yes 	no 	yes 	no
TLSv1.2 	        no 	no 	yes 	no 	no 	yes
""" How to do assignments?  """
ssl.PROTOCOL_SSLv2
ssl.PROTOCOL_SSLv3
ssl.PROTOCOL_TLS
ssl.PROTOCOL_SSLv23 (same as above)
ssl.PROTOCOL_TLSv1
ssl.PROTOCOL_TLSv1_1
ssl.PROTOCOL_TLSv1_2


ssl.verify_flags		value
ssl.VERIFY_DEFAULT		0
ssl.VERIFY_CRL_CHECK_LEAF	
ssl.VERIFY_CRL_CHECK_CHAIN
ssl.VERIFY_X509_STRICT
ssl.VERIFY_X509_TRUSTED_FIRST

>>> hex(s.verify_flags)
'0x8000'

>>> hex(s.options)
'0x8300 03ff'





>>> h7 = http.client.HTTPSConnection("192.168.2.118", 8091, ...)
>>> h7.request("GET", "/")
SSLError                        Traceback (most recent call last)
SSLEror: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl
.c:645)



>>> m = ssl.get_default_verify_paths()

>>> m
    DefaultVerifyPaths(cafile=None, capath='/usr/lib/ssl/certs', openssl_ca
file_env='SSL_CERT_FILE', openssl_cafiles='/usr/lib/ssl/cert.pem', openssl_capath
_env='SSL_CERT_DIR', openssl_capath='/usr/lib/ssl/certs')



>>> s2 = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)

>>> h8 = http.client.HTTPSConnection('192.168.2.118', 8091, key_file='/home
    /jlo/Downloads/PODM_keypair/pi.key', cert_file='/home/jlo/Downloads/POD
    M_keypair/pi.crt', context=s2)
>>> h8.request("GET", "/")
SSLError: [SSL: SSLV3_ALERT_BAD_CERTIFICATE] sslv3 alert bad certificate (_ssl.c
:645)


openssl s_client -connect 192.168.2.118:8091 -CAfile server_ca.pem  -cert client_cert.pem -key client_key.pem


Script started on Wed Jan 17 18:18:18 2018
jlo@psme-001:~/Pyroot/uione/accton$ sudo openssl genrsa -out serv                    cd ..
]0;jlo@psme-001: ~/Pyroot/uionejlo@psme-001:~/Pyroot/uione$ ls
[0m[34;42maccton[0m  [01;34mgraveyard[0m  [01;34mmysite[0m  [01;34mpodmone[0m  [01;34mrestone[0m  [01;34mskyone[0m  [01;34mtmsone[0m  [01;34mtutorial[0m  [01;34muienv[0m
]0;jlo@psme-001: ~/Pyroot/uionejlo@psme-001:~/Pyroot/uione$ mk  cd accton
]0;jlo@psme-001: ~/Pyroot/uione/acctonjlo@psme-001:~/Pyroot/uione/accton$ ls
[0m[01;34m__pycache__[0m  [01;34matnutils[0m    fibo.py      [01;34mstatic[0m      typescript1
accton.py    [01;34mcreateform[0m  [01;32mmanage.py[0m    [01;34mtemplates[0m
[01;34mapplication[0m  [01;32mdb.sqlite3[0m  [01;34mpod_manager[0m  typescript
]0;jlo@psme-001: ~/Pyroot/uione/acctonjlo@psme-001:~/Pyroot/uione/accton$ md kdir ssl
]0;jlo@psme-001: ~/Pyroot/uione/acctonjlo@psme-001:~/Pyroot/uione/accton$ cd ssl
]0;jlo@psme-001: ~/Pyroot/uione/accton/ssljlo@psme-001:~/Pyroot/uione/accton/ssl$ sudo openssl genrsa -out server.key 2048 
[A
[sudo] password for jlo: 
Generating RSA private key, 2048 bit long modulus
.....................+++
...................+++
e is 65537 (0x10001)
]0;jlo@psme-001: ~/Pyroot/uione/accton/ssljlo@psme-001:~/Pyroot/uione/accton/ssl$ [Kls
server.key
]0;jlo@psme-001: ~/Pyroot/uione/accton/ssljlo@psme-001:~/Pyroot/uione/accton/ssl$ sudo openssl req -sha512 -new -key serve 
r.key -out ca.csr -subj "/C=TW/ST=TAICHUNG/L=TAIPEII[1@P[1@E[1@I[1P[1P[1P[1P[1P/L=TAIPEI/O=accton/OU=tms/CN=192.168.2.1 
08"
jlo@psme-001:~/Pyroot/uione/accton/ssl$ ls
ca.csr  server.key
jlo@psme-001:~/Pyroot/uione/accton/ssl$ sudo openssl req -in ca.csr -noout -text 
[A
Certificate Request:
    Data:
        Version: 0 (0x0)
        Subject: C=TW, ST=TAIPEI, L=TAIPEI, O=accton, OU=tms, CN=192.168.2.108
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:bd:6b:13:d0:9d:12:1c:9e:af:e5:45:70:f4:38:
                    34:8f:3f:de:99:1b:0d:b4:62:8e:a2:5d:35:85:5f:
                    29:a2:29:44:f2:81:4c:23:63:0a:d5:68:7e:50:b4:
                    8f:5b:b7:5d:82:c4:0c:2d:bb:cc:4b:6e:82:5e:40:
                    28:6e:b4:fa:4a:22:a5:47:f6:ad:af:02:3a:87:bc:
                    33:8a:5c:94:9f:6e:f1:0a:15:70:51:18:64:8a:ec:
                    e4:7f:5e:32:aa:8a:30:6e:59:1e:99:76:84:7e:90:
                    2b:b1:6c:9b:3d:b1:89:1f:41:b9:a7:8f:2c:15:19:
                    34:2a:22:8a:99:f7:20:fd:5f:69:ce:1f:0f:90:0e:
                    9c:a2:12:c4:8c:d9:a1:10:5a:51:66:44:ec:be:6d:
                    97:b1:97:84:49:0c:be:92:3e:17:00:00:19:73:2b:
                    8a:2f:91:9f:94:ae:d6:c2:a2:73:de:89:be:c9:6e:
                    e7:02:aa:7b:2d:26:34:63:15:9d:52:30:f1:4d:c1:
                    c3:80:47:19:ce:05:b7:c5:cc:97:8c:51:5a:a0:b7:
                    ff:fd:5d:03:e6:11:1f:62:ad:43:b9:08:ba:a4:fc:
                    47:9c:f0:ab:b0:ae:fd:5c:27:d7:8c:e7:4a:be:90:
                    be:2c:7a:9d:c4:dd:70:8e:1a:54:c4:93:ac:ac:e6:
                    f3:11
                Exponent: 65537 (0x10001)
        Attributes:
            a0:00
    Signature Algorithm: sha512WithRSAEncryption
         46:df:21:9e:f4:70:7b:0b:ea:90:8a:96:44:06:ad:55:97:4a:
         fa:f4:2b:dd:7d:6b:b9:f2:68:92:52:38:99:89:f0:23:86:0b:
         04:52:9e:50:9a:24:55:ae:5d:86:ba:78:35:6d:06:9a:de:71:
         4a:45:1b:25:f7:61:50:05:6a:cc:bb:a0:bb:c6:11:6d:c7:35:
         93:4f:c4:1b:b9:fa:cf:24:f2:59:07:11:84:24:9d:3d:14:32:
         60:89:e8:3d:83:1f:da:e5:44:1b:ab:f7:9e:8a:82:13:88:be:
         59:0c:2d:df:fd:37:ff:9b:65:0c:22:fd:68:00:58:aa:6f:19:
         d5:59:e7:ac:c5:16:fe:57:b4:ac:3f:75:13:5b:42:47:3f:a9:
         ea:80:8a:c9:61:3e:1f:80:03:c6:48:7a:ca:00:c7:da:8e:4e:
         a0:e6:8c:14:83:e1:96:ec:b9:d8:8e:8f:46:3b:e5:44:f5:f9:
         8c:4a:c4:e3:15:9b:7c:fb:6f:1a:a6:d3:c0:a6:aa:b6:ed:a1:
         3a:84:07:27:4c:5a:ee:82:9f:c2:a5:4d:00:49:68:05:16:71:
         ff:1f:f3:51:5c:6c:e5:0f:51:5a:8c:15:05:dd:d7:c4:ae:27:
         88:e0:ca:4e:33:bd:60:d0:72:54:f2:fd:71:93:35:67:8d:1b:
         fa:b9:f7:bc
jlo@psme-001:~/Pyroot/uione/accton/ssl$ sudo openssl x509 -sha512 -req -days 365 
0 -in ca.csr -signkey server.key -out server.crt
Signature ok
subject=/C=TW/ST=TAIPEI/L=TAIPEI/O=accton/OU=tms/CN=192.168.2.108
Getting Private key
jlo@psme-001:~/Pyroot/uione/accton/ssl$ ls
ca.csr  server.crt  server.key
jlo@psme-001:~/Pyroot/uione/accton/ssl$ cat server.crt
-----BEGIN CERTIFICATE-----
MIIDSDCCAjACCQCHuQfdzlK2fzANBgkqhkiG9w0BAQ0FADBmMQswCQYDVQQGEwJU
VzEPMA0GA1UECAwGVEFJUEVJMQ8wDQYDVQQHDAZUQUlQRUkxDzANBgNVBAoMBmFj
Y3RvbjEMMAoGA1UECwwDdG1zMRYwFAYDVQQDDA0xOTIuMTY4LjIuMTA4MB4XDTE4
MDExNzEwMjYyN1oXDTI4MDExNTEwMjYyN1owZjELMAkGA1UEBhMCVFcxDzANBgNV
BAgMBlRBSVBFSTEPMA0GA1UEBwwGVEFJUEVJMQ8wDQYDVQQKDAZhY2N0b24xDDAK
BgNVBAsMA3RtczEWMBQGA1UEAwwNMTkyLjE2OC4yLjEwODCCASIwDQYJKoZIhvcN
AQEBBQADggEPADCCAQoCggEBAL1rE9CdEhyer+VFcPQ4NI8/3pkbDbRijqJdNYVf
KaIpRPKBTCNjCtVoflC0j1u3XYLEDC27zEtugl5AKG60+koipUf2ra8COoe8M4pc
lJ9u8QoVcFEYZIrs5H9eMqqKMG5ZHpl2hH6QK7Fsmz2xiR9BuaePLBUZNCoiipn3
IP1fac4fD5AOnKISxIzZoRBaUWZE7L5tl7GXhEkMvpI+FwAAGXMrii+Rn5Su1sKi
c96Jvslu5wKqey0mNGMVnVIw8U3Bw4BHGc4Ft8XMl4xRWqC3//1dA+YRH2KtQ7kI
uqT8R5zwq7Cu/Vwn14znSr6Qvix6ncTdcI4aVMSTrKzm8xECAwEAATANBgkqhkiG
9w0BAQ0FAAOCAQEAL/8VMTlKASlmhw6j6PcM3iHM9Nvd50+8v1syryVZ79om73Na
5g2mKimDbcyOgfNMid9yuHIG/1vWUGA4vJypBjKahqLsm8IIF2YGGUlWbDD7u13O
qNmPR5ZXHwpv5YA13dWTxdOwD94WTBTSbXoehw5InRNC7dQDwnXnloN7lWnxSKVm
JV5X44zzxD5Jbl6cg3p34yBcQ3N2PYGQR3Z1kKzK5ZsDAS0ayRSd7oMNpn4hhKnE
Du1tJ3+K19RaU89I9Vl+6d0/1fkeH2xiScbup7M2T+8Ft13UzMA7d349SwaUHyAC
CkWw4bOY86oZN5fo7/93aH+r2pHeUr4RC/366w==
-----END CERTIFICATE-----
jlo@psme-001:~/Pyroot/uione/accton/ssl$ 
[18P(reverse-i-search)`': o': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr -sign
nkey server.key -out server.crt[A)`op': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr -sig[1@n[Aeverse-i-search)`op': sudo e': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr -si[1@g[Aeverse-i-search)`ope': sudo n': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr -s[1@i[Aeverse-i-search)`open': sudo s': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr -[1@s[Aeverse-i-search)`opens': sudo s': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr [1@-[Aeverse-i-search)`openss': sudo l': sudo openssl x509 -sha512 -req -days 3650 -in ca.csr[1@ [Aeverse-i-search)`openssl': sudo  ': sudo openssl x509 -sha512 -req -days 3650 -in ca.cs[1@r[Aeverse-i-search)`openssl ': sudo s': openssl s_client -connect 192.168.2.118:8091 -cert[18P pi.crt -key pi.key[Apenssl s': 

jlo@psme-001:~/Pyroot/uione/accton/ssl$ openssl s_client -connect 192.168.2.118:8091 -cert:~/Pyroot/uione/accton/ssl$ openssl s_client -connect 192.168.2.118

8091 -cert pi[1@s[1@e[1@r[1@v[1@e[1@r[1P[1P.crt -key [1@s[1@e[1@r[1@v[1@e[1@r[1P[1P
CONNECTED(00000003)
depth=0 C = EX, O = Intel, CN = 10.3.0.7
verify error:num=18:self signed certificate
verify return:1
depth=0 C = EX, O = Intel, CN = 10.3.0.7
verify error:num=10:certificate has expired
notAfter=Jan 11 15:20:50 2017 GMT
verify return:1
depth=0 C = EX, O = Intel, CN = 10.3.0.7
notAfter=Jan 11 15:20:50 2017 GMT
verify return:1
140506240685720:error:14094418:SSL routines:ssl3_read_bytes:tlsv1 alert unknown ca:s3_pkt.c:1487:SSL alert number 48
140506240685720:error:140790E5:SSL routines:ssl23_write:ssl handshake failure:s23_lib.c:177:
---
Certificate chain
 0 s:/C=EX/O=Intel/CN=10.3.0.7
   i:/C=EX/O=Intel/CN=10.3.0.7
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIBjjCCARMCCQCxl7CncGITCzAKBggqhkjOPQQDAjAwMQswCQYDVQQGEwJFWDEO
MAwGA1UECgwFSW50ZWwxETAPBgNVBAMMCDEwLjMuMC43MB4XDTE2MTIxMjE1MjA1
MFoXDTE3MDExMTE1MjA1MFowMDELMAkGA1UEBhMCRVgxDjAMBgNVBAoMBUludGVs
MREwDwYDVQQDDAgxMC4zLjAuNzB2MBAGByqGSM49AgEGBSuBBAAiA2IABC8Wb6mF
2pmLC2Jp5ts3Vlo4QgmWqzRXH9QKhVkzzcM0omwXQ952gMKSw0+83DNVMdTOBdi4
AeUWqiRbAtid6i3W0cbdgOrQ4IvPy04juUXeMkRgkeQKkHXbMJAxgO49cDAKBggq
hkjOPQQDAgNpADBmAjEAtfahWojUivS+H+kL32r689CFOe4B1hwI7cPy42xXCjdP
PQJaX9mtULyKA/zqBQ41AjEA2MqoHeq2d9rvwc0tCGWUbSvSOugTqAmu4gPVbjVr
llacYSZ6ysCxudaOW/1YP/YQ
-----END CERTIFICATE-----
subject=/C=EX/O=Intel/CN=10.3.0.7
issuer=/C=EX/O=Intel/CN=10.3.0.7
---
Acceptable client certificate CA names
/C=TW/ST=TAICHUNG/L=TAICHUNG/O=example/OU=Personal/CN=www.example.com
Client Certificate Types: RSA sign, DSA sign, ECDSA sign
Requested Signature Algorithms: RSA+SHA512:DSA+SHA512:ECDSA+SHA512:RSA+SHA384:DSA+SHA384:ECDSA+SHA384:RSA+SHA256:DSA+SHA256:ECDSA+SHA256:RSA+SHA224:DSA+SHA224:ECDSA+SHA224:RSA+SHA1:DSA+SHA1:ECDSA+SHA1
Shared Requested Signature Algorithms: RSA+SHA512:DSA+SHA512:ECDSA+SHA512:RSA+SHA384:DSA+SHA384:ECDSA+SHA384:RSA+SHA256:DSA+SHA256:ECDSA+SHA256:RSA+SHA224:DSA+SHA224:ECDSA+SHA224:RSA+SHA1:DSA+SHA1:ECDSA+SHA1
Peer signing digest: SHA512
Server Temp Key: ECDH, P-256, 256 bits
---
SSL handshake has read 878 bytes and written 1254 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-ECDSA-AES128-GCM-SHA256
Server public key is 384 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-ECDSA-AES128-GCM-SHA256
    Session-ID: F45F422E9D711B3802918765D6BE2993B017093CDBE91C06C1C3339B502910B5
    Session-ID-ctx: 
    Master-Key: D48F308BDE2686E22F6F57DBD99DF2884A9E2CFD5CFC559D1A9D777E05A5426C6F0698C9940EE1A93BDD81E9E978BC87
    Key-Arg   : None
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    Start Time: 1516184923
    Timeout   : 300 (sec)
    Verify return code: 10 (certificate has expired)
---
jlo@psme-001:~/Pyroot/uione/accton/ssl$ openssl s_client -connect 192.168.2.118:88091 -cert server.crt -key server.key                                 
jlo@psme-001:~/Pyroot/uione/accton/ssl$ openssl s_client -connect 192.168.2.118: 
jlo@psme-001:~/Pyroot/uione/accton/ssl$ openssl s_client -connect 192.168.2.118[K

jlo@psme-001:~/Pyroot/uione/accton/ssl$ openssl s_client -connect 192.168.2.118                                       exit

Script done on Wed Jan 17 19:23:03 2018

$ openssl s_client -connect 192.168.2.118:8091 -cert server.crt -key server.key


#define HOST_PORT "443"







