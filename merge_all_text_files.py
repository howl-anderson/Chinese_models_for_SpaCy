import pathlib
import sys

input_dir = sys.argv[1]
input_path = pathlib.Path(input_dir)
input_files = input_path.glob("*")

output_file = sys.argv[2]
output_path = pathlib.Path(output_file)


with output_path.open("wt") as outfile:
    for fname in input_files:
        with fname.open("rt") as infile:
            for line in infile:
                if not line.endswith("\n"):
                    line = line + "\n"
                outfile.write(line)
