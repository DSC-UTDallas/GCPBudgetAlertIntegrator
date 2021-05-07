# Note
This is the python version for Discord made based on https://github.com/wapfel20/GCPBudgetAlertIntegrator

# Using the Functions
To use these Cloud Function scripts to integrate GCP Budget Alerts, a user must first have created a GCP Budget in the billing console, configured it to post to a pub/sub topic, and created a webhook in the target collaboration evironment. They would then need to configure the cloud function to trigger on the pub/sub topic and push to the webhook.

For step-by-step guidance on setting up and using these functions, see my article here: https://medium.com/@wapfel20/kill-unexpected-cloud-costs-integrate-gcp-budget-alerts-with-slack-microsoft-teams-hangouts-b1db306db080
