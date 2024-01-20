# La carte Scolaire - School affiliation map
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/leafletjs/leafletjs-ar21.png" alt="leaflet" width="100" /> </a>
## Introduction
Project which concluded 3 months training with python. 

The main goal was to collect, clean and transform data in order to produce statistical visual tool. This project was made in two weeks and there is still a lot of work to improve : see above
We worked around the School map in France. The issue was about middle school affiliation regarding your home adress. It is an administrative and educationnal stress or the parents. 

## What type of analyse could we do
We were able to acknowledge the middle school students in France  
<img src="./assets/repartition_eleves.png" alt="Student repartition in France" width="800"/>  

Evaluate the proportion of student in private or public middle schools  
<img src="./assets/repartition_pub_priv.png" alt="Public or private middle school repartition" width="800"/>  


## What does it show
For this project, we worked with GEO JSON files to be able to represent France regions delimitation and target a living area. The user chooses a university area, chooses a school and have informations about it :
* Middle school name
* Number of students
* Success ratio
* IPS (indice de position sociale) : gives an indeication about family context influencing on education
* List of streets affiliated to this school


## What to improve next
* automatically show school when clicking ang zooming on an academic area
* Hide the list of adresses when it is too long and scroll down to see the rest
* showing street numbers affiliated to each area
* search bar for an adress to directly show the middle school affiliated
