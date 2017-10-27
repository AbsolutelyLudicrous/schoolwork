	.file	"fizzbuzz.c"
	.section	.rodata.str1.1,"aMS",@progbits,1
.LC0:
	.string	"fizz"
.LC1:
	.string	"buzz"
.LC2:
	.string	"%d\n"
	.text
	.globl	main
	.type	main, @function
main:
.LFB11:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	pushq	%rbx
	.cfi_def_cfa_offset 24
	.cfi_offset 3, -24
	subq	$8, %rsp
	.cfi_def_cfa_offset 32
	movl	$1, %ebx
	movl	$1431655766, %ebp
	jmp	.L4
.L12:
	movl	$.LC0, %edi
	call	puts
	movl	$1717986919, %edx
	movl	%ebx, %eax
	imull	%edx
	sarl	%edx
	movl	%ebx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	leal	(%rdx,%rdx,4), %eax
	cmpl	%eax, %ebx
	je	.L5
.L3:
	addl	$1, %ebx
	cmpl	$101, %ebx
	je	.L11
.L4:
	movl	%ebx, %eax
	imull	%ebp
	movl	%ebx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	leal	(%rdx,%rdx,2), %eax
	cmpl	%eax, %ebx
	je	.L12
	movl	$1717986919, %edx
	movl	%ebx, %eax
	imull	%edx
	sarl	%edx
	movl	%ebx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	leal	(%rdx,%rdx,4), %eax
	cmpl	%eax, %ebx
	jne	.L13
.L5:
	movl	$.LC1, %edi
	call	puts
	jmp	.L3
.L13:
	movl	%ebx, %esi
	movl	$.LC2, %edi
	movl	$0, %eax
	call	printf
	jmp	.L3
.L11:
	addq	$8, %rsp
	.cfi_def_cfa_offset 24
	popq	%rbx
	.cfi_def_cfa_offset 16
	popq	%rbp
	.cfi_def_cfa_offset 8
	ret
	.cfi_endproc
.LFE11:
	.size	main, .-main
	.ident	"GCC: (Solus) 6.4.0"
	.section	.note.GNU-stack,"",@progbits
