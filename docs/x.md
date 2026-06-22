\# QR QuickShop — Development Log



\## Day 3 — Introduction to REST APIs and Frontend Integration



Date: 22 June 2026



Project:

QR QuickShop



Branch:

day3-rest-api



\---



\# Objective



The objective of Day 3 was:



\* Learn what REST APIs are

\* Create the first intentional API endpoint

\* Understand GET requests

\* Test APIs without browser dependency

\* Connect frontend to REST architecture

\* Move one step closer to production architecture



This was the first day focused on backend engineering concepts.



\---



\# Starting State



Current system architecture before Day 3:



Browser



↓



HTML



↓



JavaScript



↓



Flask



↓



SQLite



Frontend was calling:



/items



Response:



\[

products

]



This worked but was not structured for future scaling.



Goal:



Convert to REST style.



\---



\# Step 1 — Understanding API Requests



Experiment:



Attempted to execute:



GET /api/products



inside PowerShell.



Result:



Command not recognized.



Learning:



GET is not a terminal command.



GET is an HTTP method.



Correct tools:



Browser



curl



Invoke-RestMethod



Postman



Concept learned:



Commands ≠ HTTP Requests



\---



\# Step 2 — Running First API Test



Command executed:



Invoke-RestMethod http://127.0.0.1:5000/items



Observed:



Structured output:



id

name

price



Learned:



PowerShell automatically converts JSON.



Request flow:



Client



↓



HTTP GET



↓



Flask



↓



JSON



↓



Response



Concept learned:



API Testing



\---



\# Step 3 — Designing First REST Endpoint



File Modified:



backend/server.py



Old endpoint:



@app.route("/items")



Target:



@app.route("/api/products")



Implemented:



@app.route("/api/products", methods=\["GET"])

def get\_products():

return jsonify({

"success": True,

"count": len(store\_items),

"products": store\_items

})



Design decisions:



success



Used for future error handling.



count



Used for pagination and metadata.



products



Contains actual business data.



Concept learned:



REST Response Structure



\---



\# Step 4 — First Backend Error



Error Encountered:



NameError



Error Message:



name 'data' is not defined



Root Cause:



Dictionary key written without quotes.



Wrong:



{

data: store\_items

}



Correct:



{

"data": store\_items

}



Resolution:



Converted key to string.



Concept learned:



Python Dictionary Keys



Traceback Reading



Debugging Workflow



\---



\# Step 5 — Server Restart and Verification



Commands executed:



python backend/server.py



Observed:



QR QuickShop is running



PC:

http://127.0.0.1:5000



API test:



Invoke-RestMethod http://127.0.0.1:5000/api/products



Response:



count

products



Verification:



REST endpoint successfully returned JSON.



Concept learned:



Server Lifecycle



\---



\# Step 6 — Frontend Migration



File Modified:



backend/templates/index.html



Old frontend call:



fetch("/items")



New frontend call:



const res = await fetch("/api/products");



const response = await res.json();



const items = response.products;



Concept learned:



Frontend should consume APIs.



Architecture improvement:



Before:



Frontend



↓



/items



↓



Array



After:



Frontend



↓



/api/products



↓



Structured JSON



\---



\# Step 7 — Browser Validation



Opened:



http://127.0.0.1:5000



Observed:



Products still rendered.



Cart loaded.



API requests executed.



Server logs:



GET /



GET /api/products



GET /cart



Meaning:



Frontend integration successful.



Concept learned:



End-to-End Testing



\---



\# Final Architecture After Day 3



Browser



↓



index.html



↓



JavaScript



↓



fetch("/api/products")



↓



Flask REST Endpoint



↓



get\_products()



↓



JSON



↓



UI Rendering



Architecture Style:



Server Rendered + REST Integration



\---



\# Technical Concepts Learned



Backend:



REST APIs



Frontend:



fetch()



HTTP:



GET



JSON:



Structured Responses



Debugging:



Traceback Analysis



Testing:



Invoke-RestMethod



Architecture:



Frontend → API → Backend



\---



\# Commands Executed



API Test:



Invoke-RestMethod http://127.0.0.1:5000/items



Run Server:



python backend/server.py



REST Test:



Invoke-RestMethod http://127.0.0.1:5000/api/products



Git:



git checkout -b day3-rest-api



\---



\# Deliverables Completed



✓ First REST endpoint created



✓ Endpoint tested



✓ JSON response structured



✓ Frontend migrated



✓ Application verified



✓ Debugging completed



\---



\# Day 3 Outcome



Before:



I could run the project.



After:



I can explain:



How browser calls backend



How backend returns JSON



How REST endpoints work



How frontend consumes APIs



\---



\# Next Session — Day 4



Target:



POST /api/cart



Topics:



POST



Request Body



JSON Input



Mutating Application State



Goal:



Create first data-changing REST API.

