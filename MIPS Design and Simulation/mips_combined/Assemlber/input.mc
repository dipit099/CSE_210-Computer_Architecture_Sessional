
# calculating nth term of fibonacci series, $t0
# contains the value of n and $t3 contains the result
start:
addi $t0, $zero, 5

addi $t1, $zero, 1
beq $t0, $t1, baseCase

addi $t1, $zero, 2
beq $t0, $t1, baseCase

addi $t1, $zero, 1
addi $t2, $zero, 1
addi $t4, $zero, 2

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

# storing the result in stack #8    ($t3=8)
sw $t3, 0($sp)
subi $sp, $sp, 1

# now multiplying the result by 16 #8*16=80 ($t0=80)
sll $t0, $t3, 4
sw $t0, 0($sp)
subi $sp, $sp, 1

# now again dividing $t0 by 4 #80/4=20 ($t4=20)
srl $t4, $t0, 2
sw $t4, 0($sp)
subi $sp, $sp, 1

# storing in memory #20 in loc:2
sw $t4, -18($t4)
sw $t4, 0($sp)
subi $sp, $sp, 1

# loading the value from memory #20
lw $t1, -18($t4)
sw $t1, 0($sp)
subi $sp, $sp, 1

# addi 96 + -120 #e8
addi $t2, $t1, -120
sw $t2, 0($sp)
subi $sp, $sp, 1

# sub 104 - -24 #7f
subi $t3, $t2, -127
sub $t3, $t3, $t2
sw $t3, 0($sp)
subi $sp, $sp, 1

# and 01000110 & 01010101 #44

addi $t0, $zero, 70
addi $t1, $zero, 85
and $t2, $t0, $t1
sw $t2, 0($sp)
subi $sp, $sp, 1

# andi 01000100 & 11111110 #44
andi $t3, $t2, -2
sw $t3, 0($sp)
subi $sp, $sp, 1

# or 10000000 | 10101010 #aa
addi $t3, $zero, -128
addi $t4, $zero, -86
or $t1, $t3, $t4
sw $t1, 0($sp)
subi $sp, $sp, 1

# ori 10101010 | 11111111 #ff

ori $t2, $t1, -1
sw $t2, 0($sp)
subi $sp, $sp, 1

complete:

j complete

# final stack result :
#  ff aa 44 44 7f e8 60 60 60 03 37
