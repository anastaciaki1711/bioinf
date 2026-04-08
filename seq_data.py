a=open(r"C:\Users\Настя\Downloads\rosalind_gc.txt", "r")
class Seq():
    def __init__(self,file):
        self.file=file
    def my_sequence(self):
        self.file.seek(0)
        first_line=self.file.readline()
        if first_line.startswith ('>'):
            first_line=first_line[1:]
        return print(first_line)

result=Seq(a)
id=result.my_sequence()