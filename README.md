# Project3

Objective:

Write a program that creates a database to store information about gourmet chocolate bars. This data was originally retrieved from Kaggle (https://www.kaggle.com/rtatman/chocolate-bar-ratings/data) and JSON data from (https://restcountries.eu/).

After loading the data into a database, the ability for a user to issue several different types of queries to extract information from the database will be made.

Learning Goals
Be able to import data from CSVs and JSON into a relational database
Be able to write a range of SQL queries to extract data from a relational database
Gain experience writing interactive command line programs that support a range of commands and options


Here is an example run:

Yongjaes-MacBook-Air:project-3-yongjaekwon Yongjae$ python3 proj3_choc.py
Enter a command: bars ratings

Enter a command: bars ratings
Chuao           Amedei          Italy           5.0  70%  Venezuela (B...
Toscano Blac... Amedei          Italy           5.0  70%  Unknown
Pablino         A. Morin        France          4.0  70%  Peru
Chuao           A. Morin        France          4.0  70%  Venezuela (B...

Chanchamayo ... A. Morin        France          4.0  63%  Peru
Morobe          Amano           United State... 4.0  70%  Papua New Gu...
Guayas          Amano           United State... 4.0  70%  Ecuador
Porcelana       Amedei          Italy           4.0  70%  Venezuela (B...
Nine            Amedei          Italy           4.0  75%  Unknown
Madagascar      Amedei          Italy           4.0  70%  Madagascar

Enter a command: bars sellcountry=US cocoa bottom=5
Peru, Madaga... Ethel's Arti... United State... 2.5  55%  Unknown
Trinidad        Ethel's Arti... United State... 2.5  55%  Trinidad and...
O'ahu, N. Sh... Guittard        United State... 3.0  55%  United State...
O'ahu, N. Sh... Malie Kai (G... United State... 3.5  55%  United State...
O'ahu, N. Sh... Malie Kai (G... United State... 2.8  55%  United State...

Enter a command: companies region=Europe bars_sold
Bonnat          France          27
Pralus          France          25
A. Morin        France          23
Domori          Italy           22
Valrhona        France          21
Hotel Chocol... United Kingd... 19
Coppeneur       Germany         18
Zotter          Austria         17
Artisan du C... United Kingd... 16
Szanto Tibor    Hungary         15

Enter a command: companies ratings top=8
Amedei          Italy           3.8
Patric          United State... 3.8
Idilio (Felc... Switzerland     3.8
Benoit Nihan... Belgium         3.7
Cacao Sampak... Spain           3.7
Bar Au Choco... United State... 3.6

Soma            Canada          3.6
Brasstown ak... United State... 3.6

Enter a command: countries bars_sold
United State... Americas        764
France          Europe          156
Canada          Americas        125
United Kingd... Europe          107
Italy           Europe          63
Ecuador         Americas        55
Australia       Oceania         49
Belgium         Europe          40
Switzerland     Europe          38
Germany         Europe          35

Enter a command: countries region=Asia ratings
Viet Nam        Asia            3.4
Israel          Asia            3.2
Korea (Repub... Asia            3.2
Japan           Asia            3.1

Enter a command: regions bars_sold
Americas        1085
Europe          568
Oceania         70
Asia            46
Africa          26

Enter a command: regions ratings
Oceania         3.3
Asia            3.2
Europe          3.2
Americas        3.2
Africa          3.0

Enter a command: bad command
Command not recognized: bad command

Enter a command:

Enter a command: bars nothing
Command not recognized: bars nothing

Enter a command: exit
bye
