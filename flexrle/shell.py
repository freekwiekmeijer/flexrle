from datetime import datetime
from os import path, SEEK_END
from sys import argv, exit, stderr


def print_usage(e=None):
    msg = "Usage: %s <source file> <destination file>\n" % \
          path.basename(argv[0])
    if e:
        msg = "Error: %s\n" % e + msg
    stderr.write(msg)
    exit(1)


def run_from_shell(func):
    if len(argv) < 3:
        print_usage()
    src_file = argv[1]
    dst_file = argv[2]
    if not path.isfile(src_file):
        print_usage("Source file does not exist")

    f_in = open(src_file, "rb")
    f_out = open(dst_file, "w+b")

    t1 = datetime.now()
    func(f_in, f_out)
    runtime = (datetime.now() - t1).total_seconds()

    bytes_in = f_in.tell()
    bytes_out = f_out.tell()

    if func.__name__ == "encode":
        stderr.write(
            "Compressed %d bytes of input to %d bytes of output (%.1f %%)\n" %
            (bytes_in, bytes_out, 100.0 * bytes_out / bytes_in))
    else:
        stderr.write(
            "Uncompressed %d bytes of input to %d bytes of output\n" %
            (bytes_in, bytes_out))

    stderr.write("Runtime: %.2f seconds (%d kB/s)\n" %
                 (runtime, bytes_in/1024/runtime))
