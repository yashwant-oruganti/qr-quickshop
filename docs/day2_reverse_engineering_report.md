\# QR QuickShop — Development Report



\## Day 2 — Reverse Engineering and Understanding Existing Architecture



Date: 21 June 2026



\---



\# Objective



The objective of Day 2 was not to build new features.



The objective was:



\* Run the existing project successfully

\* Understand the complete architecture

\* Reverse engineer code generated earlier

\* Learn how frontend and backend communicate

\* Prepare the project for future REST API migration



Project:



QR QuickShop



Status:



From:

Unknown inherited code



To:

Understandable working application



\---



\# Initial Situation



At the beginning of Day 2:



\* Project was generated earlier and not fully understood

\* Architecture was unclear

\* Flask application was not running

\* Git workflow had already been prepared during Day 1



Decision:



Do not abandon project.



Rebuild and understand it.



\---



\# Step 1 — Architecture Investigation



Reviewed project files:



backend/



server.py



models.py



templates/



static/



requirements.txt



Goal:



Identify:



\* Application entry point

\* Database layer

\* Frontend logic

\* Request flow



Finding:



Application starts from:



server.py



\---



\# Step 2 — Backend Analysis



File:



server.py



Purpose identified:



Acts as:



\* Flask Application

\* Route Controller

\* Authentication Handler

\* Cart Controller

\* Checkout Processor

\* QR Generator



Major routes identified:



/



/items



/add\_to\_cart



/cart



/update\_cart



/checkout



/orders



/auth



/dashboard



Concept Learned:



Route → Function → Response



Example:



GET /items



↓



get\_items()



↓



jsonify()



\---



\# Step 3 — Database Analysis



File:



models.py



Identified database models:



User



Fields:



id

name

email

mobile

password

role



Favourite



Fields:



id

item\_name

price

user\_id



Order



Fields:



id

order\_uid

items

total

status



Concept Learned:



SQLAlchemy ORM



Flow:



Python Object



↓



ORM



↓



SQL



↓



SQLite



\---



\# Step 4 — Dependency Resolution



Problem:



ModuleNotFoundError



No module named:



flask\_sqlalchemy



Root Cause:



Dependency missing.



Resolution:



Installed package.



Concept Learned:



requirements.txt



↓



pip install



↓



import



Dependencies are declarations.



Installation is separate.



\---



\# Step 5 — Application Execution



Command executed:



python backend/server.py



Result:



Application launched successfully.



Observed:



GET /



GET /items



POST /add\_to\_cart



GET /cart



Meaning:



Frontend and backend communication works.



Concept Learned:



HTTP Request Lifecycle



\---



\# Step 6 — API Exploration



Visited:



/items



Observed JSON:



\[

{

"id":1,

"name":"Apple"

}

]



Conclusion:



Current project already partially behaves like an API.



Concept Learned:



GET Request



JSON Response



Serialization



\---



\# Step 7 — Frontend Analysis



Files analyzed:



index.html



script.js



base.html



Understanding:



HTML



↓



JavaScript



↓



fetch()



↓



Flask



↓



Database



↓



JSON



↓



DOM Update



Concept Learned:



Client–Server Communication



\---



\# Step 8 — Cart Flow Analysis



Action:



Click Add To Cart



Observed:



POST /add\_to\_cart



↓



GET /cart



Backend Process:



Receive JSON



↓



Update cart



↓



Return response



↓



Refresh UI



Concept Learned:



State Management



\---



\# Step 9 — Template Inheritance



Analyzed:



base.html



index.html



Found:



{% extends "base.html" %}



Meaning:



base.html



↓



inject content



↓



render final page



Concept Learned:



Template Inheritance



Reusable Layouts



\---



\# Step 10 — Search and Navigation Understanding



Observed:



Search Form



↓



GET /search



↓



Render Results



Observed:



Dynamic login/logout using:



session\["user"]



Concept Learned:



Server-side Rendering



Sessions



\---



\# Architectural Observations



Current Architecture:



Browser



↓



HTML + CSS



↓



JavaScript



↓



fetch()



↓



Flask



↓



SQLAlchemy



↓



SQLite



↓



JSON



↓



UI Update



Architecture Type:



Monolithic Flask Application



Server Rendered + AJAX



\---



\# Major Technical Findings



Strengths:



✓ Working Flask application



✓ JSON communication



✓ Session authentication



✓ QR checkout



✓ Database integration



✓ Dashboard flow



Weaknesses:



✗ Hardcoded products



✗ Global cart



✗ Inline CSS



✗ Inline JavaScript



✗ Large server.py



✗ Mixed frontend/backend concerns



\---



\# Learning Outcomes



Git:



Repository workflow understanding



Backend:



Flask routes



Frontend:



fetch()



API:



GET



POST



JSON



Database:



ORM



Architecture:



Request lifecycle



\---



\# Deliverables Completed



Completed:



✓ Project successfully executed



✓ Architecture identified



✓ Database understood



✓ Frontend analyzed



✓ API flow traced



✓ Request lifecycle understood



✓ Refactor plan prepared



\---



\# Next Steps — Day 3



Goals:



Create first REST endpoint



Move toward:



/api/products



Separate:



UI



↓



API



↓



Business Logic



↓



Database



Expected Learning:



REST



HTTP Methods



Postman



Cloud-ready architecture



