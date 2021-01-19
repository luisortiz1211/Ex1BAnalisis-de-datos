# Ex1BAnalisis-de-datos
#1 twitter-to-couch, con las claves de acceso que se obtuvo en Twitter son la llave para realizar un scraping, la función listener será la encargada de ir almacenando en el array la búsqueda de tweets sobre un contenido en específico. Se inicializa el servidor de couchdb y se crea la base twitter_couch_dakar2021 la misma que contendrá los tweets sobre dakar2021.

#2 web-to-mongo, Se crea 2 funciones las cuales se encargarán de evaluar con que símbolo inicializa la etiqueta que se busca en el scraping , response almacenara el contenido de la web que se evalúa.
A continuación, post_pilots extrae en contenido de cada etiqueta de acuerdo a una class de búsqueda.
Este contenido ingresa en un bucle 'for' que se ejecuta hasta guardar el contenido de las etiquetas devueltas.

#3 facebook-to-mongo, se inicializa el servidor de mongodb, el bucle 'for' se ejecutar de acuerdo a la función get_posts la misma que se encarga de devolver las características de una página en el caso de 'dakar2021' devuelve: likes, text, commets. El contenido referente a ese tema.

#5 couch-to-mongo, se inicializa el servidor de couchdb al ingresar en 'try' verifica si la conexión se realizó con éxito. Se crea una variable server la cual contiene la dirección de origen de la base de datos: De igual manera se realiza la conexión con mongodb. La variable 'db' almacena la base de datos cuyo origen es couchdb al ingresar en el bucle 'for' se almacenarán los datos en la nueva base llamada couch_mongo_dakar2021 la misma que contiene una colección llamada dakar2021.

#6 mongo-to-couch, se inicializa el servidor en couchdb el cual almacenara la base de datos que se extrae de mongodb. se confirma que el servidor mongodb este inicializado, la variable 'DBS' será la encargada de guardar el contenido de la base de datos. Se ejecuta un bucle 'for' para almacenar el contenido de la colección ahora en una base en couchdb.

#7 couch-to-atlas, se inicia el servidor de couchdb, lugar del que se obtendrá la base de datos. Para enlazar couch con atlas se necesita el link del cluster. Además de la dirección y usuario contiene el nombre que se asignara a la base. La variable 'DBm' contiene información de la base en mongodb. 'DBma' será la colección en atlas donde se guardará la información que se migra.

#8 mongo-to-atlas, la migración de información en este caso es similar a la de couchdb. Se inicializa el servidor en mongodb que contiene la base de datos a migrar. Se obtiene el link del cluster para realizar la conexión, la variable 'DBm' será la que guarde el contenido que se obtiene de mongodb. 'DBma' almacena la nueva colección que se crea en atlas.

#9 #10 mongo-to-csv, se realiza una conexión con casa el cluster de atlas que contiene el archivo a descargar. La variable 'colección' almacenara todo el contenido de la colección de la base de datos en atlas con ayuda de la función to_csv se crea un archivo csv.

