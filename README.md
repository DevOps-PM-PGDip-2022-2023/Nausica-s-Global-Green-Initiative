
# Table of Contents

# Scrum Master
Week 1 and 2 so far Dean has taken this on - We do plan to rotate to give everyone the opportunity  Rotating scrum master so that everyone gets to experience the role once.

# Product Owner
Pauric Dawson

# Rockstars
- Aidan Corley
- Anuradha Goli
- Dean Moore
- Goran Kraljic(withdrew)
- Julian Fitzsimons(No Input)
- Kehinde/Rotimi Awoniran
- Samantha Toner

# Project Deadline
23 March 2023

# Project Specification
Clean and simple design
User access levels (client, administrator)
Includes at least one self developed api and one webservice
To be run over <specify platform>

# Frameworks
We will be using MongoDB for our database
Database persistence technology
Define the buisness Requirements
Named queries and database triggers for security
Regex for cleansing and validation of data before sending to the database.

# Useful Links
 - Project Slack: https://atudevops.slack.com/archives/C04ETS0CLJV
 - GitHub: https://github.com/DevOps-PM-PGDip-2022-2023/Nausicaas-Global-Green-Initiative
EasyRetro | Improve your team with fun sprint retrospectives https://easyretro.io/publicboard/4dbxdGABPHeYondyMoldWXrgJRP2/e910232b-de78-41bb-8e6e-fa662582aa68
JIRA - https://l00177576-devops.atlassian.net/jira/software/projects/GGI/boards/3
Home - Confluence (atlassian.net) https://l00177576-devops.atlassian.net/wiki/home 


# Section	Description
Process	Describes the companies process
Project Log	Log of project activities
Costings	Overview of the project cost
Architecture	Outlines the architecture
Environments	Overview of the environment set-up
DR Plan	Disaster Recovery Plan and procedures
Requirements	Overview of the requirements for the project
SLAs	Service level agreements
Risk Management	How we manage risk
Security	Overview of security
Project Log	Team log for the project

# Risk Register
These are the current Risks on the project, re-aligned on a weekly basis
Team Members leaving the Course
Team Members Unavailable due to sickness or other commitments


# Tenants of Design
The code framework to be used will be <<>>, we will be programming using the IDE Visual Studio

# Security:
Security Testing:
Test the system's login and authentication mechanisms to ensure that only authorized users can access the system.
Test the system's response to SQL injection, cross-site scripting, and other common security vulnerabilities.
Session based security (if the system does not recognise you as a user the ability to view information is restricted 
Front end User validation (user details that do not exist restrict what pages are viewable) 
Ports being locked down (can only access the system on a specific port e.g., 5000 
AWS VPC 
AWS security groups- within the VPC 
AWS guard duty a threat detection service that continuously monitors for malicious activity and anomalous behaviour 
AWS Sheild - defends against most common, frequently occurring network and transport layer DDoS attacks that target your website or applications 

# Testing:
Identify the Requirements and confirm they are Testable
Boundary Analysis Tests 
Test Case for Teto – Valid 1 to 10000 Invalid 0,-1, 10001 –
Ensure admin can edit details –
Ensure users that are not admin cannot edit details –
Ensure grant applicant cannot change details once submitted
Selenium is planned to be used for automated testing
Functional Testing:
Verify that the system allows end customers to create an account and log in with valid credentials.
Test that end customers can submit their grant application details, including personal information and funding requirements.
Verify that the system can map customer details to the appropriate grant and display available grants, including the Teto grant of up to €10,000.
Test that the system provides a single box for special award applications and allows end customers to add additional funding requirements.
Verify that the system prevents grant applicants from editing their application details once submitted.
Test that the system allows administrators to access detailed information about grant applicants and edit as appropriate.
Performance Testing:
Test the system's response time and scalability by simulating a large number of grant applications and users.
Verify that the system can handle high traffic and usage without significant delays or downtime.
Compatibility Testing:
Test the system's compatibility with different web browsers and devices, including desktop and mobile devices.
Verify that the system displays correctly and functions properly on different screen sizes and resolutions.
Regression Testing:
Test the system after any updates or changes to ensure that it still functions as expected and that previous features remain intact.
Usability Testing:
Conduct usability testing to ensure that the system is user-friendly and meets the end customer's needs and expectations.
Accessibility Testing:
Test the system's accessibility features to ensure that it is compliant with accessibility standards and can be used by people with disabilities.
Integration Testing:
Test the system's integration with other applications and databases to ensure that it can communicate and exchange data correctly.
Disaster Recovery and Business Continuity Testing:
Test the system's backup and recovery mechanisms to ensure that it can recover from any data loss or system failure.
    
# Environments:
    staging and production
    tight configuration management for consistency and reproducibility
    automated creation and deployments
    integrated and automated pipeline (commit -> test -> deploy)

# Github version control:
    branches used
    version/release management

# Agile project management methods/principles (jira)
JIRA Project and Kanban Board https://l00177576-devops.atlassian.net/jira/software/projects/GGI/boards/3
Confluence Page https://l00177576-devops.atlassian.net/wiki/spaces/SD/overview?homepageId=229464
Sprint Retros available (https://easyretro.io/publicboard/4dbxdGABPHeYondyMoldWXrgJRP2/e910232b-de78-41bb-8e6e-fa662582aa68)
Agile Sprints of 2 week duration took place
Stand Ups conducted as part of tue Lecture plus every Thursday and on a few occassions on a Sunday evening, this will continue until the end of the Project
# Social Contract
    Mobile phones be left on silent during sprint sessions and class time.
    Be on time for team meetings and class, if you are running late let the group know by sending a message into the Slack channel.
    Everyone has an equal voice and valuable contribution.
    When you are assigned a job, take ownership of it and keep it up to date, do not be afraid to ask others for help, always be honest about your work.
    Do not speak over someone when they are expressing a point, everyone has an equal voice.
    No blame culture.
    Do not be afraid to ask for help, we are all learning.
    No invisble work. - Dean has been assist Aidan with the Virtual Box Terminal Issues
    Ask questions to make sure you understand the task given to you.
    Try have some fun, team work makes the dream work.
    Use Agile methodoligies in the project at all times. User Stories identified from the Project brief, the user stories were created and prioritised based on the brief after initial questions were asked

# Meetings
Stand-ups will occur on Every Tue at the end of class and Thursday at 6:30. Two per week. These also took place on Sunday evenings
The order that people give their updates will be decided by Scrum Master. The team decided this and mostly Dean as he was proactive in setting up Zoom calls
Updates will be in the form: What I've done, Impediments, What I plan to do.
Sprint planning will occur at <<date/time>> every week.
Please add and update items within <<issue management tool>> a prior to the sprint planning session.
Sprint retro will at the end of our sprint on <<Date/Time>> (timebox retro for 15 minutes, to be organised by the scrum master).
The order that people present their sprint retro updates will be based on The Team 1 list in the Assign_BSc_DevOps_2022.pdf file on blackboard of those present at the meeting.
Points raised in the sprint retro will be noted and posted on the slack channel by the Scrum Master. The Scrum Master is rotated per team member every week.
Backlog refinement will happen on <<date/time>> during our sprint.
Task estimation will be done using << >>. 
Come prepared to meetings.
Be on time for Stand Ups and meetings.
Mobile phones on silent.
Everyone has equal voice and valuable contribution.
Keep your language and tone professional at all times.
Be honest.

# Communication
Slack is the preferred method of communication.
Communication in this order: <<Slack, Microsoft Teams, E-Mail>> *Note that if the lecturers can't see the communications we cannot grade it!
If a demonstration is required use Zoom, record the session and upload to the Slack channel.
No Slack communications between <<time and time>>.
Raise a problem as soon as you see it.
Respect each other and understand differences in knowledge.
All team documents are to be created using Markdown language and shared on GitHub.
There are no silly questions, if you don’t understand, ask.
Share success stories.
Focus on the positives.
Don’t make assumptions.
Don’t interrupt and cut another person off while they are talking.
Listen when someone is talking, don’t interject.
Zero tolerance for bullying.

# Agile way of working.
If are assigned a job, take ownership of it and keep it up to date.
Stick to your agreed working patterns. Let the team know when you are late or going early.
Keep JIRA board updated at all times.
Update the Scrum Board as you progress the story i.e. don’t update at standup.
Don't be afraid to ask for help.
Don't be afraid to give constructive criticism, as long as it is constructive.
Solve roadblocks within the team. If the impediment can’t be solved within the team then give it to the Scrum Master.
Other
Sprints will start after the stand up that happens at the start of class each week.
The Scrum Master role rotates each week, the schedule is available on the on the process section
Poker Planner will be used for task management and planning.
Each member of the team will work approximitely 3 hours per week, unless they are on vacation.
Our branching stategy will start with gh then the issue number followed by wip

# Estimating Story Points
The teams team's velocity is calculated by <<Team decides>>.
The Team is familiar with estimating 

The teams current story point velocity is "N/A".
Velocity will be useful if team members remain the same or as close to the same as possible throughout the Project

# Definition of Ready
<<List criteria that are common here>>
User Story created
Acceptance Criteria created
Estimated
3 Amigos between BA/Test/Dev

# Definition of Done
Acceptance Criteria delivered and confirmed
Demoed to the Customer
Signed Off by the Customer
Signed Off by the Customer
