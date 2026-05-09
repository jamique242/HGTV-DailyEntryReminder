# 🏡HGTV-DailyEntryReminder
## Overview
This project demonstrates a lightweight, event-driven AWS reminder system designed to automate daily reminder notifications for HGTV sweepstakes entries. The application follows a serverless architecture using core AWS services with minimal operational overhead. The goal of the project is to showcase:
* Event-driven cloud architecture
* Scheduled automation workflows
* Serverless compute patterns
* Notification integrations
* Infrastructure-as-code concepts
The project intentionally avoids unnecessary complexity and focuses on beginner-friendly cloud engineering concepts.

## How it works
Each day at 9:00 AM, an automated trigger is executed to send reminder texts and emails to a subscriber list. These messages direct users to a webpage hosted in an Amazon S3 bucket, which contains direct links to both the HGTV and Food Network sweepstakes entry pages.
