global _start

section .text
_start:
	mov rax,1
	mov rdi,1
	mov rsi,print
	mov rdx,5
	syscall

_exit:
	mov rax,60
	mov rdi,22
	syscall

section .data
	print: db 'hello'
