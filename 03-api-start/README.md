# API 

http + (json|xml)

## fake data web

 https://mockaroo.com/

## instalación

https://www.getpostman.com/

```
$ python3 -m venv env
$ source venv/bin/activate
$ pip freeze
$ pip install -r requirements.txt
```

## debuggear python (pdb)

```
import pdb; pdb.set_trace()
(Pdb) colegas.get(1000)
{'id': 1000, 'first_name': 'Reinhard', 'last_name': 'Serridge', 'email': 'rserridger
r@businessinsider.com', 'gender': 'Male', 'company': 'Toyota'}
(Pdb) pp colegas.get(1000)
{'company': 'Toyota',
 'email': 'rserridgerr@businessinsider.com',
 'first_name': 'Reinhard',
 'gender': 'Male',
 'id': 1000,
 'last_name': 'Serridge'}
(Pdb) colegas.get(1001) is None
True
(Pdb) len(colegas)
1000
(Pdb) 100 in colegas
True
(Pdb) 1001 in colegas
False
(Pdb) 'Opel' in VALID_COMPANIES
False
(Pdb) 'Subaru' in VALID_COMPANIES
True
(Pdb) l
 15  
 16     import pdb; pdb.set_trace()
 17     # pp colegas
 18     # colegas.get(1)
 19  
 20  -> VALID_COMPANIES = set(colega["company"] for colega in colegas.values())
 21     CAR_NOT_FOUND = 'Colega no encontrado'
 22  
 23     print(colegas)
 24     print(VALID_COMPANIES)
 25  
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb
 
```






