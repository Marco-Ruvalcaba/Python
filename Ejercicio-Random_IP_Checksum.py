def ip_checksum(ip_header, size):
    cksum = 0
    pointer = 0
    while size > 1:
        cksum += int((str("%02x" % (ip_header[pointer],)) +
                      str("%02x" % (ip_header[pointer+1],))), 16)
        size -= 2
        pointer += 2
    if size: #This accounts for a situation where the header is odd
        cksum += ip_header[pointer]
    cksum = (cksum >> 16) + (cksum & 0xffff)
    cksum += (cksum >>16)
    return (~cksum) & 0xFFFF


header = {}
header[0] = 0x45
header[1] = 0x00
header[2] = 0x00
header[3] = 0x60
header[4] = 0x21
header[5] = 0x08
header[6] = 0x40
header[7] = 0x00
header[8] = 0x20
header[9] = 0x06
header[10] = 0x0
header[11] = 0x0
header[12] = 0x82
header[13] = 0x82
header[14] = 0x01
header[15] = 0x37
header[16] = 0x82
header[17] = 0x82
header[18] = 0x01
header[19] = 0x32

for x in header:
    print( type( header[x] ) )
    print( header[x] )

print("Checksum is: %x" % (ip_checksum(header, len(header)),))
print(% ( ip_checksum(header, len(header) ) , ) )
print("Should be BD92")
