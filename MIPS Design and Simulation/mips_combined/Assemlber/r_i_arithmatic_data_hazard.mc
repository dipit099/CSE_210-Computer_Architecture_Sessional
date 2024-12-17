addi $t3, $zero, 10 // t3=10
addi $t0, $zero, 10 // t0=10
addi $t1, $zero, 10 // t1=10
addi $t1, $t1, 5    // t1=15
add $t2, $t0, $t1   // t2=t0+t1=25
sub $t2, $t2, $t1   // t2=t2-t1=10
add $t4, $t3, $t2   // t4=t3+t2=20
addi $t3, $t2, 10   // t3=t2+10=20

// Final value of each register:
// $t0 = 10
// $t1 = 15
// $t2 = 10
// $t3 = 20
// $t4 = 20



write above line without the comments besides the instruction
addi $t3, $zero, 10
addi $t0, $zero, 10
addi $t1, $zero, 10
addi $t1, $t1, 5
add $t2, $t0, $t1
sub $t2, $t2, $t1
add $t4, $t3, $t2
addi $t3, $t2, 10

