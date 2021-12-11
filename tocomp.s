.global _start

_start:
    movq $0x000000, %rsp
    pop (%rdi)
    movq $0x000000, 0x8(%rdi)
    movq $0x000000, (%rsp)
