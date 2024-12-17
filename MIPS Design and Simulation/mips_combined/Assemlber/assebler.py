# DEBUGGING and ETC
bin_output = True
bin_code = []

# Instructions mapping by ID
instructions_ids = {
    "A" : "add",
    "B" : "addi",
    "C" : "sub",
    "D" : "subi",
    "E" : "and",
    "F" : "andi",
    "G" : "or",
    "H" : "ori",
    "I" : "sll",
    "J" : "srl",
    "K" : "nor",
    "L" : "sw",
    "M" : "lw",
    "N" : "beq",
    "O" : "bneq",
    "P" : "j"
}

sequence = "PHLMEJGAFNICBKOD"

# Instructions opcode
opcodes = {}

for i in range(len(sequence)):
    opcodes[instructions_ids[sequence[i]]] = format(i, '04b')
    bin_code.append(instructions_ids[sequence[i]] + " " + format(i, '04b'))
    

# Register mapping
registers = {
    '$zero': '0000',
    '$t0': '0001',
    '$t1': '0010',
    '$t2': '0011',
    '$t3': '0100',
    '$t4': '0101',
    '$sp': '0110',
}

# Categories of instructions
instructions_categories = {
    "R" : ["add", "sub", "and", "or", "sll", "srl", "nor"],
    "I" : ["addi", "subi", "andi", "ori", "sw", "lw", "beq", "bneq"],
    "J" : ["j"]
}

# Handling labels
labels = {}

# Functions for each instruction category
def hadnle_r_type(instruction):
    instruction_name = instruction[0]
    opcode = opcodes[instruction_name]
    
    rd = registers[instruction[1]]
    rs = registers[instruction[2]]
    
    if instruction_name in ["sll", "srl"]:
        rt = "0000"
        shamt = int(instruction[3])
        if shamt < 0:
            shamt = abs(shamt)
            if instruction_name == "sll":
                opcode = opcodes["srl"]
            else:
                opcode = opcodes["sll"]
        shamt = format(shamt, '04b')
        code = f"{opcode} {rs} {rt} {rd} {shamt}"
        bin_code.append(code)
        return code.replace(" ", "")
    else :
        rt = registers[instruction[3]]
        code = f"{opcode} {rs} {rt} {rd} 0000"
        bin_code.append(code)
        return code.replace(" ", "")


def hadnle_i_type(instruction):
    instruction_name = instruction[0]
    opcode = opcodes[instruction_name]
    
    if instruction_name in ["sw", "lw"]:
        rt = registers[instruction[1]]
        offset,rs = instruction[2].split('(')
        rs = registers[rs[:-1]]
        offset = int(offset)
        if offset < 0:
            offset = abs(offset)
            offset = (1 << 8) - offset
        offset = format(offset, '08b')
        code = f"{opcode} {rs} {rt} {offset}"
        bin_code.append(code)
        return code.replace(" ", "")
    
    elif instruction_name in ["beq", "bneq"]:
        rt = registers[instruction[1]]
        rs = registers[instruction[2]]
        label = format(labels[instruction[3]], '08b')
        code = f"{opcode} {rs} {rt} {label}"
        bin_code.append(code)
        return code.replace(" ", "")
    else:
        rt = registers[instruction[1]]
        rs = registers[instruction[2]]
        imm = int(instruction[3])
        if imm < 0:
            imm = abs(imm)
            imm = (1 << 8) - imm
        imm = format(imm, '08b')
        code = f"{opcode} {rs} {rt} {imm}"
        bin_code.append(code)
        return code.replace(" ", "")
        

def hadnle_j_type(instruction):
    instruction_name = instruction[0]
    opcode = opcodes[instruction_name]
    imm = format(labels[instruction[1]], '08b')
    code = f"{opcode} {imm} 00000000"
    bin_code.append(code)
    return code.replace(" ", "")

def convert_to_hex(machine_code):
    hex_code = []
    for code in machine_code:
        hex_code.append(format(int(code, 2), '05x'))
    return hex_code

# Function to convert an assembly instruction to machine code
def convert_to_machine_code(instructions):

    # Program end loop (in case it was not provided)
    program_end_loop = ["PROGRAM_END_LOOP:", "j PROGRAM_END_LOOP"]
    instructions += program_end_loop

    # Handling labels
    label_count = 0
    for i in range(len(instructions)):
        if instructions[i][-1] == ":":
            labels[instructions[i][:-1]] = i - label_count
            label_count += 1
            instructions[i] = ""
    
    instructions = [i for i in instructions if i]   # replace empty lines

    machine_code = []
    for instruction in instructions:
        instruction = instruction.split()
        
        instruction_name = instruction[0]
        instruction_args = "".join(instruction[1:]).split(',')
        instruction_args = [instruction_name] + instruction_args
        
        if instruction_name in instructions_categories["R"]:
            mc = hadnle_r_type(instruction_args)
        elif instruction_name in instructions_categories["I"]:
            mc = hadnle_i_type(instruction_args)
        elif instruction_name in instructions_categories["J"]:
            mc = hadnle_j_type(instruction_args)
        else:
            raise ValueError(f"Invalid instruction: {instruction_name}")
        
        machine_code.append(mc)
    
    machine_code = convert_to_hex(machine_code)
    return machine_code
        
# Main function to process a file
def process_file(input_file, output_file):
    with open(input_file, 'r') as f:
        # read lines untill "end:" is found
        assembly_code = []
        for line in f:
            # skip empty lines
            if line.strip() and line.strip().startswith("#") == False:
                # remove parts afterr ; (comments)
                line = line.split(';')[0]
                # print(line.strip())
                assembly_code.append(line.strip())
            # skip comments starts with #
    
    machine_code = convert_to_machine_code(assembly_code)
    
    # Write the machine code output to the output file
    with open(output_file, 'w') as f:
        f.write(f"v2.0 raw\n")
        for code in machine_code:
            f.write(code + ' ')
        f.write('\n')
    
    if bin_output:
        with open(output_file.split('.')[0] + '.bin', 'w') as f:
            for code in bin_code:
                f.write(code + '\n')
        
        
# Example usage:
# input_file = 'testCase#.asm'
# output_file = 'testCaseOut#.asm'

# input_file = 'input.mc'
# output_file = 'output.asm'

input_file = input("Enter the input file name: ")
output_file = input("Enter the output file name: ")

process_file(input_file, output_file)
