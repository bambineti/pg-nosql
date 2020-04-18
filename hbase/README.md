** 1- Crie a tabela com 2 famílias de colunas: personal-data professional-data **

hbase(main):003:0> create 'italians','personal-data','professional-data'
Created table italians
Took 1.2427 seconds                                                                                                                                   
=> Hbase::Table - italians

** 2- Importe o arquivo via linha de comando **
root@0d4f47225a2e:/# hbase shell /tmp/italians.txt 
2020-04-18 18:52:15,855 WARN  [main] util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Took 0.4614 seconds                                                                                                                                   
Took 0.0038 seconds                                                                                                                                   
Took 0.0038 seconds                                                                                                                                   
Took 0.0036 seconds                                                                                                                                   
Took 0.0039 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0031 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0032 seconds                                                                                                                                   
Took 0.0032 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0032 seconds                                                                                                                                   
Took 0.0042 seconds                                                                                                                                   
Took 0.0045 seconds                                                                                                                                   
Took 0.0045 seconds                                                                                                                                   
Took 0.0055 seconds                                                                                                                                   
Took 0.0032 seconds                                                                                                                                   
Took 0.0042 seconds                                                                                                                                   
Took 0.0042 seconds                                                                                                                                   
Took 0.0041 seconds                                                                                                                                   
Took 0.0040 seconds                                                                                                                                   
Took 0.0030 seconds                                                                                                                                   
Took 0.0033 seconds                                                                                                                                   
Took 0.0032 seconds                                                                                                                                   
Took 0.0030 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0035 seconds                                                                                                                                   
Took 0.0030 seconds                                                                                                                                   
Took 0.0027 seconds                                                                                                                                   
Took 0.0026 seconds                                                                                                                                   
Took 0.0028 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0034 seconds                                                                                                                                   
Took 0.0031 seconds                                                                                                                                   
Took 0.0029 seconds                                                                                                                                   
Took 0.0027 seconds                                                                                                                                   
Took 0.0024 seconds                                                                                                                                   
Took 0.0025 seconds                                                                                                                                   
Took 0.0024 seconds                                                                                                                                   
HBase Shell
Use "help" to get list of supported commands.
Use "exit" to quit this interactive shell.
For Reference, please visit: http://hbase.apache.org/2.0/book.html#shell
Version 2.1.2, r1dfc418f77801fbfb59a125756891b9100c1fc6d, Sun Dec 30 21:45:09 PST 2018
Took 0.0011 seconds  

Agora execute as seguintes operações:

1 - Adicione mais 2 italianos mantendo adicionando informações como data de  nascimento  nas  informações  pessoais  e  um  atributo  de  anos  de experiência nas informações profissionais;
hbase(main):001:0> put 'italians', '1', 'personal-data:name',  'Charles Bambineti'
Took 0.0068 seconds                                                                                                                                   
hbase(main):002:0> put 'italians', '1', 'personal-data:city',  'Crema'
Took 0.0028 seconds                                                                                                                                   
hbase(main):003:0> put 'italians', '1', 'professional-data:role',  'Gestao TI'
Took 0.0033 seconds                                                                                                                                   
hbase(main):004:0> put 'italians', '1', 'professional-data:salary',  '9545'
Took 0.0041 seconds                                                                                                                                   
hbase(main):005:0> put 'italians', '2', 'personal-data:name',  'Pietro Colombi'
Took 0.0027 seconds                                                                                                                                   
hbase(main):006:0> put 'italians', '2', 'personal-data:city',  'Cremona'
Took 0.0025 seconds                                                                                                                                   
hbase(main):007:0> put 'italians', '2', 'professional-data:role',  'Lavrador'
Took 0.0028 seconds                                                                                                                                   
hbase(main):008:0> put 'italians', '2', 'professional-data:salary',  '1890'
Took 0.0032 seconds                                                         

2 - Adicione o controle de 5 versões na tabela de dados pessoais.
hbase(main):011:0> alter 'italians', NAME=> 'personal-data', VERSIONS=>5
Updating all regions with the new schema...
1/1 regions updated.
Done.
Took 1.9330 seconds    

3 - Faça 5 alterações em um dos italianos;
hbase(main):001:0> put 'italians','1','personal-data:city','Floripa'
Took 0.4555 seconds                                                                                                                                   
hbase(main):002:0> put 'italians','1','personal-data:city','Biguacu'
Took 0.0052 seconds                                                                                                                                   
hbase(main):003:0> put 'italians','1','personal-data:city','Tijucas'
Took 0.0041 seconds                                                                                                                                   
hbase(main):004:0> put 'italians','1','personal-data:city','Sao Joao Batista'
Took 0.0043 seconds                                                                                                                                   
hbase(main):005:0> put 'italians','1','personal-data:city','Blumenau'
Took 0.0037 seconds        

4 - Com o operador get, verifique como o HBase armazenou o histórico.
hbase(main):007:0> get 'italians', '1', {COLUMN => 'personal-data:city', VERSIONS=>5}
COLUMN                                 CELL                                                                                                           
 personal-data:city                    timestamp=1587237567073, value=Blumenau                                                                        
 personal-data:city                    timestamp=1587237555309, value=Sao Joao Batista                                                                
 personal-data:city                    timestamp=1587237515345, value=Tijucas                                                                         
 personal-data:city                    timestamp=1587237501230, value=Biguacu                                                                         
 personal-data:city                    timestamp=1587237472769, value=Floripa                                                                         
1 row(s)
Took 0.0391 seconds                                           

5 - Utilize o scan para mostrar apenas o nome e profissão dos italianos.
hbase(main):011:0> scan 'italians', {COLUMNS=>['personal-data:name','professional-data:role']}
ROW                                    COLUMN+CELL                                                                                                    
 1                                     column=personal-data:name, timestamp=1587236215698, value=Charles Bambineti                                    
 1                                     column=professional-data:role, timestamp=1587236215768, value=Gestao TI                                        
 10                                    column=personal-data:name, timestamp=1587235937114, value=Giovanna Caputo                                      
 10                                    column=professional-data:role, timestamp=1587235937121, value=Comunicacao Institucional                        
 2                                     column=personal-data:name, timestamp=1587236215830, value=Pietro Colombi                                       
 2                                     column=professional-data:role, timestamp=1587236215880, value=Lavrador                                         
 3                                     column=personal-data:name, timestamp=1587235936974, value=Maria Parisi                                         
 3                                     column=professional-data:role, timestamp=1587235936984, value=Optometria                                       
 4                                     column=personal-data:name, timestamp=1587235936994, value=Silvia Gallo                                         
 4                                     column=professional-data:role, timestamp=1587235937005, value=Engenharia Industrial Madeireira                 
 5                                     column=personal-data:name, timestamp=1587235937021, value=Rosa Donati                                          
 5                                     column=professional-data:role, timestamp=1587235937032, value=Mecatronica Industrial                           
 6                                     column=personal-data:name, timestamp=1587235937043, value=Simone Lombardo                                      
 6                                     column=professional-data:role, timestamp=1587235937052, value=Biotecnologia e Bioquimica                       
 7                                     column=personal-data:name, timestamp=1587235937061, value=Barbara Ferretti                                     
 7                                     column=professional-data:role, timestamp=1587235937071, value=Libras                                           
 8                                     column=personal-data:name, timestamp=1587235937080, value=Simone Ferrara                                       
 8                                     column=professional-data:role, timestamp=1587235937088, value=Engenharia de Minas                              
 9                                     column=personal-data:name, timestamp=1587235937097, value=Vincenzo Giordano                                    
 9                                     column=professional-data:role, timestamp=1587235937106, value=Marketing                                        
10 row(s)
Took 0.0549 seconds    

6 - Apague os italianos com row id ímpar.

7 - Crie um contador de idade 55 para o italiano de row id 5
hbase(main):019:0> incr 'italians','5','personal-data:idade',55
COUNTER VALUE = 55
Took 0.0117 seconds     
   

8 - Incremente a idade do italiano em 1
hbase(main):020:0> incr 'italians','5','personal-data:idade'
COUNTER VALUE = 56
Took 0.0098 seconds


