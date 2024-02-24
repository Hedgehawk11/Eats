from discord_webhook import DiscordWebhook

def send(content):
    webhook = DiscordWebhook(' https://discord.com/api/webhooks/1210833320582184980/cjss_mbqSw-lFZsHgH_ah3JxCuSEWmeh-R4NT6HLBv973iQRIJRQ307S6rlelSX1eXrG', content=content)
    webhook.execute()