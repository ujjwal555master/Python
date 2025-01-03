;We creat a program to check that the key is equal or not
global _start

section .text

_start:
	mov rax,1
	mov rdi,1
	mov rsi,messages
	mov rdx,length_of_message
	syscall

_inputKey:
	mov rax,0
	mov rdi,0
	mov rsi,input
	mov rdx,100
	syscall
	mov rbx,rax

_printuserinput:
	mov rax,1
	mov rdi,1
	mov rsi,input
	mov rdx,rbx
	syscall

_compareKey:
	mov rsi,key
	mov rdi,input
	mov rcx,lengthofkey
	repe cmpsb
	je _accessPermit
	jne _accessDenied

_accessPermit:
	mov rax,1
	mov rdi,1
	mov rsi,acess
	mov rdx,6
	syscall
	jmp _exit

_accessDenied:
	mov rax,1
	mov rdi,1
	mov rsi,acessd
	mov rdx,15
	syscall


_exit:
	mov rax,60
	mov rdi,11
	syscall


section .data
	messages: db 'Enter the key: ',10,0
	length_of_message: equ $-messages

	acess: db 'Access !',0xa,0
	acessd: db 'acess Denied!',0xa,0

	key: db '405-7895-6356-82637-hfyhv'
	lengthofkey: equ $-key

section .bss
	input: resb 100














