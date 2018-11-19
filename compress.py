import time;
import zlib;
import json;
import struct;

file_object = open('manifest.json', 'rb')
try:
     all_the_text = file_object.read()
finally:
     file_object.close()


json = json.loads(all_the_text)
     
#print(json["initial"])

#print(json["initial"][0].split('/'))


output = open('game.cfg', 'wb')

#buff = zlib.compress(all_the_text, zlib.Z_BEST_COMPRESSION)
#output.write( struct.pack('!L', len(buff)) )
#output.write( buff )

for url in json["initial"]:
    if 'zlib' in url:
        print(url+"        ====>  break")
        continue
    else:
        print(url)
    
    tf = open("./"+url, 'rb')
    try:
        file_txt = tf.read()
    finally:
        tf.close()

    str1 = zlib.compress(file_txt, zlib.Z_BEST_COMPRESSION)
    output.write( struct.pack('!L', len(str1)) )
    output.write( str1 )
    print(len(str1))

for url in json["game"]:
    print(url)
    tf = open("./"+url, 'rb')
    try:
        file_txt = tf.read()
    finally:
        tf.close()

    str1 = zlib.compress(file_txt, zlib.Z_BEST_COMPRESSION)
    output.write( struct.pack('!L', len(str1)) )
    output.write( str1 )
    print(len(str1))

output.write( struct.pack('!L', 0) )
output.close()
time.sleep(1);

