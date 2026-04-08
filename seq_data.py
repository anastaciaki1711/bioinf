class Seq():
    def __init__(self,file):
        self.file=file
    def my_sequence(self):
        return print(self.file.read())
a=open(r"C:\Users\Настя\Downloads\rosalind_gc.txt", "r")
result=Seq(a)
result.my_sequence()