def generate_opcodes():
    opcodes = []
    for opcode in range(256):
        opcode_hex = hex(opcode)[2:].zfill(2)
        opcode_binary = bin(opcode)[2:].zfill(8)
        opcodes.append((opcode_hex, opcode_binary))
    return opcodes

def print_opcodes(opcodes):
    print("{:<10} {:<10} {:<10}".format("Opcode", "Hexadecimal", "Binary"))
    print("=" * 30)
    for opcode, binary in opcodes:
        print("{:<10} {:<10}".format(opcode, binary))

opcodes = generate_opcodes()
print_opcodes(opcodes)
