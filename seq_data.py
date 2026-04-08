a=open(r"C:\Users\Настя\Downloads\rosalind_gc.txt", "r")
class Seq():
    def __init__(self,file):
        self.file=file
    def my_sequence_id(self):
        self.file.seek(0)
        first_line=self.file.readline()
        if first_line.startswith ('>'):
            first_line=first_line[1:]
        return print(first_line)
    def my_sequence(self):
        k=self.file.read()
        line=k.splitlines()
        second_line= "\n".join(line[1:])
        return print(second_line)
result=Seq(a)
id=result.my_sequence_id()
sequence=result.my_sequence()
