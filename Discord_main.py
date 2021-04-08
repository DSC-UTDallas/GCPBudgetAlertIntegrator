import base64
import json
#discord-webhook>=0.13.0
from discord_webhook import DiscordWebhook, DiscordEmbed

def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/821559497147416617/cKmxC5uKk1iTm0_H7Fp7GD3JQevzW2m1GknYu7BTGfk330xE3Z8tzDaCy4OJrMEgF7H-', content='<@&656976951143301166> :money_with_wings: ')
    response = webhook.execute()

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    alert = json.loads(pubsub_message)

    webhook = DiscordWebhook(url='https://discord.com/api/webhooks/821559497147416617/cKmxC5uKk1iTm0_H7Fp7GD3JQevzW2m1GknYu7BTGfk330xE3Z8tzDaCy4OJrMEgF7H-')
    embed = DiscordEmbed(title=':bangbang: GCP Budget Alert Threshold Exceeded :bangbang:')
    embed.set_footer(text='GCP Billing Alerts', icon_url='https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png')
    embed.add_embed_field(name='Budget Name:', value=alert["budgetDisplayName"])
    embed.add_embed_field(name="Current Spend:", value=str(alert["costAmount"]))
    embed.add_embed_field(name="Budget Amount Exceeded:", value=str(alert["budgetAmount"]))
    embed.add_embed_field(name="Alert Threshold:", value=str(alert["alertThresholdExceeded"] * 100)+"%")
    embed.add_embed_field(name="Currency Type:", value=alert["currencyCode"])
    embed.add_embed_field(name="Budget Start Date:", value=alert["costIntervalStart"])
    embed.set_timestamp()

    webhook.add_embed(embed)
    response = webhook.execute()
