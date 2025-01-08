from pathlib import Path

def list_files(directory: str) -> tuple:
    path = Path(directory)
    if not path.is_dir():
        return None
    files = tuple(file.name for file in path.iterdir() if file.is_file())
    
    return files
   
#C:\Users\Админ\Scripts\Markina\2024.12.14>tree /f
#Folder PATH listing
#Volume serial number is 7E4C-9A13
#C:.
#│   # HW 2024.12.14.txt
#│  1.py
#│
#└───data
#    │   7MD9i.chm
#    │   conf.py
#    │   E3ln1.txt
#    │   F1jws.jpg
#    │   le1UO.txt
#    │   q40Kv.docx
#    │   questions.quiz
#    │   r62Bf.txt
#    │   vars.py
#    │   xcD1a.zip
#    │
#    ├───c14KE
#    │       5vsIh.dat
#    │       P2a91.dat
#    │
#    ├───mXbd9
#    │       RoBjg.pt
#    │       z03EN.pt
#    │
#    └───names
#            женские_имена.txt
#            мужские_имена_отчества.txt
#            фамилии.txt
#C:\Users\Админ\Scripts\Markina\2024.12.14>python -i 1.py
#None
#>>> list_files(r'C:\Users\Админ\Scripts\Markina\2024.12.14\data')
#('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')