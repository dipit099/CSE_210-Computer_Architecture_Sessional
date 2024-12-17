addi $t1, $zero, 3
START:
addi $t0, $t0, 1
sw $t0, -1($t0)
sw $t0, 0($sp)
addi $sp, $sp, -1
bneq $t1, $t0, START
j DONE
DONE: