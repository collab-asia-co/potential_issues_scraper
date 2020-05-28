# Potential Issues Scraper

## Process

The scraper 
1) Opens up the potential issues page for each CMS 
2) Scrapes the Asset ID, issue type and days remaining 
3) Puts the output on "action_required" sheet of Action required Speadsheet 

## Documents 
Action required Speadsheet  - https://docs.google.com/spreadsheets/d/1rKpEu60UiuIpHsPqx3Dq36b_uPzCVnzfOJ5BJ6CqgEA/edit#gid=349689069

## Setup 
1) Clone repo locally 
2) Download a chromedriver instance, and put it into the file, naming it chromedriver
3) Run potential_issues.py 

## Final product
1) Email to talent manager and country manager when a new issue occurs
2) Email to talent manager and country manager when new issue is expiring  
3) Excel and data studio dashboard that tracks metrics such as time taken to turn an issue around, number of issues etc, for easy porting into KPI tracking

## To-do list 
1) Host and run scraper
2) Find a data source to link Asset ID to talent manager and country manager respectively. The use of the "Asset channel ID" field in reports is insufficient. 
2) Create program that checks current issues and either adds, updates  or deletes a potential issue, then clears "addition" sheet 
   a) Add - insert insertion date  
   b) Update - update days remaining
   c) Delete - Delete row, add into completed claims instead 
3) Create alert functionality - email, slack etc. 
