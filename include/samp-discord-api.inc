#if defined _samp_discord_api_included
	#endinput
#endif
#define _samp_discord_api_included

#if !defined DISCORD_WEBHOOK_URL
	#define DISCORD_WEBHOOK_URL "YOUR_DISCORD_TOKEN"
#endif

const UNSAFE_STRING_LENGTH = 3072;
new UNSAFE_STRING[UNSAFE_STRING_LENGTH];

#include <a_samp>
#include <a_http>

stock SendDiscordWebhookMessage(const message[], const webhook_username[] = "samp-webhooks")
{
	format(UNSAFE_STRING, UNSAFE_STRING_LENGTH, "{\"webhook_url\": \""DISCORD_WEBHOOK_URL"\", \"webhook_username\": \"%s\", \"message\": \"%s\"}", webhook_username, message);
	HTTP(0, HTTP_POST, "127.0.0.1:5000/api/webhook/send_message", UNSAFE_STRING, "");
	return 1;
}

stock SendDiscordWebhookEmbed(const title[], const description[], const color[] = "65C281", const webhook_username[] = "samp-webhooks")
{
	format(UNSAFE_STRING, UNSAFE_STRING_LENGTH, "{\"webhook_url\": \""DISCORD_WEBHOOK_URL"\", \"webhook_username\": \"%s\", \"embed\": {\"title\": \"%s\", \"description\": \"%s\", \"color\": \"%s\"}}", webhook_username, title, description, color);
	HTTP(0, HTTP_POST, "127.0.0.1:5000/api/webhook/send_embed", UNSAFE_STRING, "");
	return 1;
}