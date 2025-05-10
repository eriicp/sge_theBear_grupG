# sge_theBear_grupG
# Mòdul d'Empleats

## Crear Empleat  
 Aquesta captura mostra el formulari per crear un nou empleat. S'han d'omplir camps obligatoris com Nom, Puesto, Departament, Email i Telèfon. L'ID del gerent és opcional. En enviar, s'afegirà un nou empleat a la base de dades.
![img.png](img/img.png)
## Llistar Empleats  
 Aquesta petició GET retorna una llista amb tots els empleats registrats al sistema. Cada empleat es mostra amb tots els seus detalls.
![img_1.png](img/img_1.png)
## Obtenir Empleat per ID  
 Introduint un ID específic, es retornen les dades d'un empleat concret. Si l'ID no existeix, es retornarà un error 404.
![img_2.png](img/img_2.png)
## Actualitzar Empleat  
 Permet modificar les dades d’un empleat existent. Només cal enviar els camps que es volen canviar.
![img_3.png](img/img_3.png)
## Eliminar Empleat  
 Aquesta operació esborra un empleat segons l’ID proporcionat. Si s’elimina correctament, es retorna una confirmació.
![img_4.png](img/img_4.png)
---

# Mòdul de Planificació

## Crear Tasca  
 Formulari per crear una nova tasca de planificació. Requereix projecte, tasca, responsable, dates, estat, etc. Els camps de material i comentaris són opcionals.
![img_5.png](img/img_5.png)
## Llistar Tasques  
 Retorna totes les tasques planificades. Cada entrada mostra les dades com dates, responsable i estat.
![img_6.png](img/img_6.png)
## Obtenir Tasca per ID  
 En introduir l’ID d’una tasca, es mostren els seus detalls complets.
![img_7.png](img/img_7.png)
## Actualitzar Tasca  
 Permet modificar una tasca existent. Només cal incloure els camps que es volen actualitzar. La resposta mostra la tasca amb els nous valors.
![img_8.png](img/img_8.png)
## Eliminar Tasca  
 Elimina una tasca segons el seu ID. Retorna una resposta de confirmació si es fa correctament.
![img_9.png](img/img_9.png)
---

# Mòdul d'Events

## Crear Event  
 Crea un nou esdeveniment introduint la data, hora, ubicació i organitzador. També es pot indicar si és privat.
![img_10.png](img/img_10.png)
## Llistar Events  
 Retorna tots els events registrats. Cada event inclou detalls com data, hora, ubicació, estat i entrades disponibles.
![img_11.png](img/img_11.png)
## Obtenir Event per ID  
 Mostra les dades d’un esdeveniment concret donat el seu ID.
![img_12.png](img/img_12.png)
## Actualitzar Event  
 Aquesta operació permet modificar informació d’un event ja registrat. Pot ser qualsevol camp.
![img_13.png](img/img_13.png)
## Eliminar Event  
 Enviant una petició DELETE amb l'ID d'un event, aquest s'eliminarà del sistema. La resposta confirma l'èxit de l'operació.
![img_14.png](img/img_14.png)
---

# Mòdul de Costos

## Crear Cost  
 Formulari per registrar un nou cost. Requereix descripció, categoria, quantitat, data i qui l'ha pagat. La resposta mostra el cost creat.
![img_15.png](img/img_15.png)
## Llistar Costos  
 Retorna un llistat de totes les despeses registrades.
![img_16.png](img/img_16.png)
## Obtenir Cost per ID  
 Mostra el detall d’un cost concret donat el seu ID.
![img_17.png](img/img_17.png)
## Actualitzar Cost  
 Permet modificar un cost existent, com canviar la quantitat, data o responsable del pagament.
![img_18.png](img/img_18.png)
## Eliminar Cost  
 Elimina una despesa del sistema segons el seu ID. La resposta indica si s’ha completat amb èxit.
![img_19.png](img/img_19.png)
---

# Mòdul de Compres

## Crear Compra  
 Permet registrar una nova compra a un proveïdor, incloent producte, quantitat, preu i estat.
![img_20.png](img/img_20.png)
## Llistar Compres  
 Mostra totes les compres fetes, útil per fer seguiment de comandes.
![img_21.png](img/img_21.png)
## Obtenir Compra per ID  
 Retorna els detalls d'una comanda específica, incloent proveïdor, producte, quantitat, preu i estat.
![img_22.png](img/img_22.png)
## Actualitzar Compra  
 Aquesta operació serveix per modificar dades d’una compra, com estat, quantitat o preu.
![img_23.png](img/img_23.png)
## Eliminar Compra  
 Suprimeix una compra del sistema indicant l’ID corresponent.
![img_24.png](img/img_24.png)
---

# Mòdul de Punts de Venda

## Crear Punt de Venda  
 Registra una nova transacció de venda. Es pot indicar si s’envia tiquet per correu.
![img_25.png](img/img_25.png)
## Llistar Punts de Venda  
 Llista totes les vendes realitzades als punts de venda.
![img_26.png](img/img_26.png)
## Obtenir Punt de Venda per ID  
 Mostra les dades detallades d’un punt de venda concret.
![img_27.png](img/img_27.png)
## Actualitzar Punt de Venda  
 Permet modificar la informació d'un punt de venda. Es poden actualitzar camps com el mètode de pagament o si s'envia tiquet per email.
![img_28.png](img/img_28.png)
## Eliminar Punt de Venda  
 Elimina una entrada de venda segons l’ID indicat.
![img_29.png](img/img_29.png)
---

# Mòdul de Vendes

## Crear Venda  
 Formulari per registrar una nova venda. Relaciona la venda amb un punt de venda específic i inclou detalls del client, producte i pagament.
![img_30.png](img/img_30.png)
## Llistar Vendes  
 Mostra totes les vendes registrades en el sistema.
![img_31.png](img/img_31.png)
## Obtenir Venda per ID  
 Dona accés als detalls d’una venda concreta.
![img_32.png](img/img_32.png)
## Actualitzar Venda  
 Permet actualitzar informació d’una venda, com import o punt de venda associat.
![img_33.png](img/img_33.png)
## Eliminar Venda  
 Elimina una venda registrada, retornant una resposta de confirmació.
![img_34.png](img/img_34.png)
---

# Mòdul de Calendari

## Crear Reunió  
 Permet crear una nova reunió amb data, hora, ubicació i informació sobre si és recurrent.
![img_35.png](img/img_35.png)
## Llistar Reunions  
 Retorna totes les reunions programades, mostrant data, hores, ubicació i si tenen recurrència.
![img_36.png](img/img_36.png)
## Obtenir Reunió per ID  
 Dona accés als detalls d’una reunió concreta mitjançant el seu ID.
![img_37.png](img/img_37.png)
## Actualitzar Reunió  
 Permet modificar dades d’una reunió ja existent, com la ubicació o l’hora.
![img_38.png](img/img_38.png)
## Eliminar Reunió  
 Elimina una reunió del calendari. La resposta inclou un missatge de confirmació i els detalls de la reunió eliminada.
![img_39.png](img/img_39.png)
![BD](https://github.com/user-attachments/assets/19069a15-24d3-466b-ae2e-39b21675da32)
