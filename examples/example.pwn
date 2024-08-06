#include <a_samp>

#define DISCORD_WEBHOOK_URL "YOUR_WEBHOOK_URL.."
#include <samp-discord-api>

main(){ return 0; }

public OnGameModeInit()
{
	Discord_SendWebhookEmbed("Server was started", "the server has been successfully started", .webhook_username = "test webhook");
	return 1;
}