# ☁️ Architecture

<div align = "center">

```
 ⏰ Event Bridge Scheduler
          │
          ▼
  ⚙️ AWS Lambda Function
          │
          ▼
  📣 Amazon SNS Topic
          │
          ▼
  📲 SMS/Email Notification
```
</div>

# 🧰 Tech Stack
| Layer	| Service |
| ----- | ------- |
| Scheduling	| Amazon EventBridge |
| Compute |	AWS Lambda |
| Notifications |	Amazon SNS |
| Infrastructure	| AWS Console / SAM |
| Frontend	| Static HTML Landing Page |

# 🔁 Application Flow
1. EventBridge triggers on a scheduled interval
2. Lambda function executes automatically
3. Lambda publishes a notification message to SNS
4. SNS sends reminder notification to subscribed endpoint
5. User receives reminder to enter HGTV sweepstakes

# ⏰ Event Bridge Configuration
Amazon EventBridge was configured with a daily cron schedule using UTC time. The rule was set to run once per day.
<div align="center">

```txt
cron(0 9 * * ? *)
```
</div>

# 🌐 Frontend Page
The frontend consists of a simple static HTML page hosted via Amazon S3.

# 🧠 Architect Design Decisions
This project was designed using a lightweight event-driven serverless architecture in order to minimize operational overhead while still demonstrating real-world AWS integration patterns.

Amazon EventBridge was selected to handle scheduling responsibilities because it provides a simple and fully managed method for triggering automated workflows on a recurring interval.

AWS Lambda was used as the compute layer to avoid maintaining persistent infrastructure. Since the application only executes once per day, a serverless execution model was more cost effective and operationally efficient than provisioning dedicated resources.

Amazon SNS was chosen as the notification service due to its native integration with Lambda and ability to distribute notifications across multiple delivery channels such as SMS and email.

The frontend was intentionally kept minimal and hosted statically in Amazon S3 to reduce complexity while still demonstrating lightweight cloud hosting concepts.

Overall, the system was intentionally designed around simplicity, scalability, and low-cost automation principles while remaining easy to understand and reproduce.

# 🔎 Observations & Design Tradeoffs
## Reminder System vs Automated Entry
The system was intentionally designed as a reminder workflow rather than a fully automated submission bot. Automating contest entries could violate sweepstakes rules and potentially result in disqualification. The reminder-based approach keeps the user responsible for the final submission action while still reducing the likelihood of missed entries.

## SMS vs Email Notification Tradeoffs
Amazon SNS supports both SMS and email delivery methods. SMS notifications were initially considered for immediacy and visibility; however, direct SMS delivery introduces additional considerations such as:
* regional messaging restrictions
* carrier filtering
* higher operational costs
* sandbox/testing limitations

Email notifications were ultimately preferred during initial testing due to simplicity, reliability, and lower cost overhead. So to achieve SMS we did an email to text using carrier emails. This caused delays, but it was acceptable as the core purpose was to setup a daily reminder.
