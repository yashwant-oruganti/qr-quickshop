\# QR QuickShop — Development Log



\## Day 1 — Repository Cleanup \& Portfolio Preparation



Date: 20 June 2026



\---



\# Objective



Prepare the existing QR QuickShop project for:



\* Professional Git workflow

\* Portfolio presentation

\* Future REST API migration

\* Cloud deployment

\* Recruiter visibility



The focus of Day 1 was not feature development.



The focus was creating a clean engineering foundation.



\---



\# Initial Project State



Project:

QR QuickShop



Current Stack:



\* Frontend → HTML, CSS, JavaScript

\* Backend → Flask

\* Database → SQLite

\* ORM → SQLAlchemy



Observed Issues:



\* Generated QR files tracked in Git

\* Repository lacked proper ignore rules

\* Development happening directly on main

\* Portfolio structure not prepared



\---



\# Step 1 — Verify Repository Status



Command:



git status



Purpose:

Shows:



\* Current branch

\* Modified files

\* Untracked files

\* Commit status



Observed Output:



\* Repository active

\* Changes detected



Concept Learned:

Git Working Tree



\---



\# Step 2 — Create Development Branch



Command:



git checkout -b portfolio-upgrade



Purpose:

Create isolated development branch.



Why:

Avoid making experimental changes directly on main.



Result:

New branch created:



portfolio-upgrade



Concept Learned:

Git Branching



\---



\# Step 3 — Verify Branch



Command:



git branch



Purpose:

List available branches.



Result:



main

portfolio-upgrade



Concept Learned:

Branch isolation



\---



\# Step 4 — Create Git Ignore Rules



Created:



.gitignore



Purpose:

Prevent unnecessary files entering repository.



Added Rules:



venv/

.venv/



\*\*pycache\*\*/



\*.pyc



\*.db



.env



.vscode/



hackathon/qr-quickshop/backend/static/qrcodes/



Concept Learned:

Repository hygiene



\---



\# Step 5 — Remove Generated QR Images



Command:



git rm --cached hackathon/qr-quickshop/backend/static/qrcodes/\*.png



Purpose:

Remove generated files from Git tracking.



Important:

\--cached removes from Git only.

Files remain locally.



Result:

QR images no longer tracked.



Concept Learned:

Generated assets should not be committed.



\---



\# Step 6 — Stage Repository Changes



Command:



git add .



Purpose:

Move changes into staging area.



Concept Learned:

Git Staging Area



Workflow:



Working Directory

↓



Staging Area



↓



Commit



\---



\# Step 7 — Verify Staged Changes



Command:



git status



Purpose:

Confirm expected files are staged.



Result:

Repository ready for commit.



Concept Learned:

Always review before commit.



\---



\# Step 8 — Create Professional Commit



Command:



git commit -m "chore: prepare repository for portfolio development"



Purpose:

Create project snapshot.



Commit Style:



type(scope): description



Used:

chore → repository maintenance



Concept Learned:

Conventional Commits



\---



\# Step 9 — Push to GitHub



Command:



git push



Purpose:

Upload local commits.



Result:

Branch synchronized:



origin/portfolio-upgrade



Concept Learned:

Local vs Remote repositories



\---



\# Step 10 — Final Verification



Command:



git status



Final Output:



nothing to commit, working tree clean



Meaning:



\* Local changes saved

\* Repository synchronized

\* Clean development state



Concept Learned:

Clean Working Tree



\---



\# Deliverables Completed



Completed:

✓ Created development branch

✓ Added .gitignore

✓ Removed generated QR files

✓ Cleaned repository

✓ Created professional commit

✓ Pushed changes to GitHub



\---



\# Engineering Concepts Learned



Git:



\* status

\* branch

\* checkout

\* add

\* commit

\* push

\* ignore

\* cached removal



Software Engineering:



\* Branch-based development

\* Repository cleanup

\* Portfolio preparation

\* Asset management



\---



\# Next Phase (Day 2)



Goal:

Convert current Flask project into REST architecture.



Target:



Frontend

↓



REST API



↓



Flask Backend



↓



Database



Planned Endpoints:



GET /api/products



POST /api/cart



GET /api/orders



Expected Learning:



\* HTTP

\* JSON

\* REST

\* API Design

\* Postman



