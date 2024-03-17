![alt text](https://github.com/NaoNexus/ChallengeNao23/blob/main/images/logo_con_scritta.png)
# ONERETAIL
## Contents
* [NAO Challenge 2024](#nao-challenge-2024)
	* [Project](#project)
		* [Coding](#coding)
			* [Dataset](#dataset)
    		* [App](#app)
			* [Server](#server)
				* [Database](#database)
			* [Sequence Diagram](#sequence-diagram)
		* [Social](#social)
			* [Logos](#logos)
     		* [Merch](#merch)
       		* [Website](#website)
* [Wiki](#wiki)
* [Time-Table](#time-table)
* [Authors](#authors)
## NAO Challenge 2024

Every year, the theme of the NaoChallenge changes, but its goal remains the same: to use robotics as a means to solve current problems. The NaoNexus team this year has focused on Retail, specifically in-store sales and warehouse management.

### Project

For the NAO Challenge 2024, the NaoNexus team has developed the OneRetail app, focusing on both physical and online retail. OneRetail utilizes the NAO robot and the emotional artificial intelligence of MorphCast to recommend products to customers and provide valuable data to retailers. For customers, the app offers a personalized and accessible experience both online and through direct assistance from NAO. For retailers, OneRetail provides a customized inventory and sales management system, along with in-depth analysis of customer interactions, all without additional costs.

- [X] Accessibility
- [X] Sustainability
- [X] Integration

##### REQUIREMENTS:
> [!IMPORTANT]
> - opencv-python==4.2.0.32 <br>
> - opencv-python-headless==4.2.0.32 <br>
> - flask <br>
> - flask_login <br>
> - yieldfrom <br>
> - PyYAML <br>
> - numpy <br>
> - requests <br>
> - selenium <br>
> - speechRecognition==3.8.1 <br>
> - paramiko <br>
> - psycopg2 <br>
> - psycopg2-binary <br>

## Coding

### Database:

The folder [database](https://github.com/NaoNexus/ChallengeNao24/tree/main/coding/database) contains the ER diagram, the complete database with defined tables and attributes. 

- This SQL script defines the structure of a database for an e-commerce application, organizing information into different tables to manage data related to customers, products, orders, emotions. The insertion of sample data provides a practical context, illustrating how the tables are interconnected. The queries retrieve information through join operations, allowing for a thorough analysis of user activity. In summary, the script provides a foundation for managing the online shopping experience, from customer registration to the analysis of preferences and interactions with products.
```ruby
CREATE TABLE Ordine (
	id			SERIAL,
	id_cliente		INT,
	prezzo_totale		DECIMAL,
	data_acquisto		DATE,
	ora_acquisto		TIME,
	modalita_pagamento	VARCHAR,
	
	PRIMARY KEY(id),
	FOREIGN KEY(id_cliente) REFERENCES Cliente(id) ON UPDATE CASCADE ON DELETE SET NULL
);
```
<div align="center">
  <img src="https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/database/diagramma%20ER.png" hight="300" width="700"/>
</div>

### Dataset:

The [dataset](https://github.com/NaoNexus/ChallengeNao24/tree/main/coding/dataset) folder encompasses a comprehensive collection of images featuring the jewelry items utilized in constructing the catalog for the application. These images serve as visual representations of the various products available in the app's inventory, providing users with a detailed and aesthetically pleasing showcase of the jewelry selection.

### App:
The folder [App/OneRitail](https://github.com/NaoNexus/ChallengeNao24/tree/main/coding/app/one_retail) contains the source code of the app. The app is the way the end user interfaces with the system for inventory control, market analysis, and enhancing business efficiency within the retail sector. Developed in collaboration with Swarovski, this application includes an online shop as well as all the in-store interactions with NAO

```ruby
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.mycompany.oneretail"
    xmlns:tools="http://schemas.android.com/tools">
    <uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.CAMERA"/>

    <application
        android:label="OneRetail"
        tools:replace="android:label"
        android:icon="@mipmap/ic_launcher"
        android:requestLegacyExternalStorage="true">
```

### Server:
The repository in the [Sever](https://github.com/NaoNexus/ChallengeNao24/tree/main/coding/server) directory serves as the essential core of the project, offering a range of fundamental functionalities. The codebase is centered around a class called DB, which manages the connection to a PostgreSQL database and provides methods for operations such as retrieving information about customers and items, as well as handling carts and orders. Additionally, there is a CustomFormatter class and a configured logger to colorize log messages based on severity levels. The project also features a script that uses the requests library to send HTTP POST requests to a specific endpoint with predefined data. Introducing Flask into the mix, the project leverages this lightweight web framework for elegant web application development. Finally, two utility functions complete the picture, calculating elapsed time from a timestamp and reading a YAML file. In summary, this repository excels not only in database operations, meticulous log management, and adept HTTP communication but also harnesses Flask for powerful web development capabilities.
```ruby
from logging_helper import logger
from datetime import datetime
from decimal import Decimal
class DB:
    def __init__(self):
        import config_helper
        config_helper = config_helper.Config()

        try:
            self.connection = psycopg2.connect(host=config_helper.db_host, 
                                               database=config_helper.db_name,
                                               user=config_helper.db_user, 
                                               password=config_helper.db_password)
```
[decision_tree](https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/server/dialogo_decision_tree.py) contains the Python code where we coded the dialogue and decision tree and 2 possible dialogues.

- This Python code defines a function called recommend_jewelry that provides personalized jewelry recommendations based on customer information such as gender, age, budget, and the desired jewelry category. The function considers various conditions, including different age and budget ranges for specific jewelry categories like bracelets, necklaces, earrings, rings, and watches. The result of the function is a list of recommended jewelry IDs, and the code is structured with nested conditions to handle different scenarios and offer advice tailored to the customer's preferences.
```ruby
if gender == 'male': 
        if age > 60:
            return []
        elif age < 20: 
            if category == 'bracelet':
                if budget >= 155:
                    for item in product_info:
                        if item['gender'] == 'M' and item['age'] < 20 and item['category'] == 'bracelet' and item['prezzo'] >= 155:
                            gioielli_consigliati.append(item['id'])
                    return gioielli_consigliati
```
- The code implements an interactive dialogue between the user and a virtual assistant specializing in jewelry. The assistant guides the user in choosing personalized jewelry by asking for information about gender, age, budget, and preferences. Using the 'recommend_jewelry' function, it provides suggestions based on the user profile. During the dialogue, the user can add jewelry to the cart, receive advice on combinations, and complete the purchase. The dialogue ends with a thank-you message from Naonecsus team 
```ruby
print("Buongiorno "+nome_utente['nome']+" "+nome_utente['cognome']+", sono peara, il nao del team naonecsus.")

    print("Come posso aiutarti? Anche se sono un robot di gioielli ne so un bel po")
    risposta1 = input()
    regalo = estrai_regalo(risposta1)
```
### Sequence Diagram:

This folder [sequence_diagram](https://github.com/NaoNexus/ChallengeNao24/tree/main/coding/sequence_diagram) contains the flowcharts of the entire project.

- The NaoNexus 2024 project orchestrates a seamless shopping experience, uniting physical and online interactions. Customers, represented by CLIENTE, can use a web application (WEB-APP) to access a catalog (CATALOGO) and make product selections. In the physical store, NEGOZIO engages in a dialogue with the NAO robot, which adds chosen products to the shopping cart (CARRELLO). Payment is processed through PAGAMENTO, and a digital receipt is generated. Similarly, in the online scenario, clients access WEB-APP, interact with CATALOGO, and select items added to the online CARRELLO. The payment process is handled by PAGAMENTO, and clients receive purchased products and information online. This integrated approach enhances the shopping journey for NaoNexus in 2024.
- [Diagramma Dialogo](https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/sequence_diagram/Diagramma%20dialogo.svg) illustrates an online shopping dialogue between the customer (CLIENTE) and NAO. Two purchasing scenarios are considered: buying as a gift and personal purchase. Using a decision tree, the assistant suggests compatible jewelry based on the customer's profile. The dialogue involves loops to gather complete information and make product selections. The interaction continues until the customer completes the purchase or decides not to add more items. Subsequently, a courtesy message is sent, and both the customer and the assistant are deactivated, concluding the dialogue. 
<div align="center">
  <img src="https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/sequence_diagram/sequence%20diagram.png" width="500" height="400" /><img src="https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/sequence_diagram/Diagramma%20dialogo.png"  width="250" height="400" >
</div>

## Social

### Logos

This folder [logos](https://github.com/NaoNexus/ChallengeNao24/tree/main/social/logos) contains the logos of the project

<div align="center">
<img src="https://github.com/NaoNexus/ChallengeNao24/blob/main/social/logos/logo/logo_comp.png" width="600" height="350"/>
</div>

### Merch

The folder [merch](https://github.com/NaoNexus/ChallengeNao24/tree/main/social/merch/felpa_2024) contains the images specifically curated for the production of the team's merchandise line, ensuring high-quality designs and branding consistency across all products.

### Website

The [website](https://github.com/NaoNexus/ChallengeNao24/tree/main/social/sito/NaoNexus) folder constitutes the central repository of our web project, containing all the necessary source code for the construction and functioning of our site. Here, all files are stored, organized neatly according to development conventions, defining the appearance, behavior, and functionality of our website. Every component of the site, from HTML pages to backend logic, is present and accessible within this folder.


## Wiki
The "[wiki](https://github.com/NaoNexus/ChallengeNao24/tree/main/wiki)" folder contains the .md source files for our wiki

* [Main page](https://naonexus.altervista.org/wiki/index.php?title=Main_Page)
* [NAO Challenge 2022](https://naonexus.altervista.org/wiki/index.php?title=Nao_CHALLENGE_2022&action=edit&redlink=1)
* [NAO Challenge 2023](https://naonexus.altervista.org/wiki/index.php?title=NAO_Challenge_2023&action=edit&redlink=1)
* [EcoTide 2023](https://naonexus.altervista.org/wiki/index.php?title=EcoTide_2023&action=edit&redlink=1)
* [NAO Challenge 2024](https://naonexus.altervista.org/wiki/index.php?title=NAO_Challenge_2024&action=edit&redlink=1)

## Time-table
This [image](https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/NAO_time.png) provides a clear overview of the project timeline table, offering a detailed representation of the start and completion phases for each individual task. This visualization is essential for monitoring the overall project progress and ensuring adherence to established deadlines.
<div align="center">
<img src="https://github.com/NaoNexus/ChallengeNao24/blob/main/coding/NAO_time.png" width="600" height="350"/>
</div>

## Authors

Suggest us new ideas at:

* socialnaonexus@gmail.com (NAONEXUS)

## Social

* [YouTube](https://www.youtube.com/channel/UCGr9x7Fr44V628GJXwMe4Pg/videos)
* [Instagram](https://www.instagram.com/naonexus/)
* [TikTok](https://www.tiktok.com/@naonexus)
* [LinkedIn](https://www.linkedin.com/in/nao-nexus-95b929208/?originalSubdomain=it)

## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.html)
