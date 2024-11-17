import os


class FileOutput:
    def __init__(self, symbol, output_dir='./output/'):
        self.symbol = symbol
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def write(self, content):
        file_path = f"{self.output_dir}{self.symbol}_output.txt"
        with open(file_path, "a") as file:
            file.write(content + "\n")
