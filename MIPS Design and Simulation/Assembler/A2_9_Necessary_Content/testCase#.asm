start:
addi $t0, $zero, 10
addi $t1, $zero, 1
beq $t0, $t1, baseCase
addi $t1, $zero, 2

beq $t0, $t1, baseCase
addi $t1, $zero, 1
addi $t2, $zero, 1
addi $t4, $zero, 2
# t1 = 1, t2 = 1, t4 = 2

loop:
add $t3, $t1, $t2
add $t1, $zero, $t2
add $t2, $zero, $t3
addi $t4, $t4, 1
bneq $t4, $t0, loop
j done

baseCase:
addi $t3, $zero, 1

done:
sw $t3, 0($sp)
subi $sp, $sp, 1

srl $t0, $t3, 4
sw $t0, 0($sp)
subi $sp, $sp, 1

sll $t4, $t0, 5
sw $t4, 0($sp)
subi $sp, $sp, 1

sw $t4, -94($t4)
sw $t4, 0($sp)
subi $sp, $sp, 1

lw $t1, -94($t4)
sw $t1, 0($sp)
subi $sp, $sp, 1

addi $t2, $t1, -120
sw $t2, 0($sp)
subi $sp, $sp, 1

subi $t3, $t2, -127
sub $t3, $t3, $t2
sw $t3, 0($sp)
subi $sp, $sp, 1

addi $t0, $zero, 70
addi $t1, $zero, 85
and $t2, $t0, $t1
sw $t2, 0($sp)
subi $sp, $sp, 1

andi $t3, $t2, -2
sw $t3, 0($sp)
subi $sp, $sp, 1

addi $t3, $zero, -128
addi $t4, $zero, -86
or $t1, $t3, $t4
sw $t1, 0($sp)
subi $sp, $sp, 1

ori $t2, $t1, -1
sw $t2, 0($sp)
subi $sp, $sp, 1

complete:
j complete
