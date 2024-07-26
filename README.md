# SA:MP Discord Webhooks API

a simple api, which allows to send webhooks to a specific discord channel, through a proxy, since samp does not support https. it was developed for use in Astro Roleplay (besta samp server).

# Run (on development)

1. Clone repository

   ```git clone https://github.com/vendder5/samp-discord-api.git```

2. Navigate to the repository directory

   ```cd samp-discord-api```

3. Create a virtual env

    Linux:
    
     ```python3 -m venv venv```

    Windows:
    
     ```virtualenv venv```

4. Access the virtual environment

    Linux:
    
     ```source venv/bin/activate```

    Windows:
    
     ```.\venv\Scripts\activate```

5. Install dependencies

    ```pip install -r requirements.txt```

6. Run api

    Linux:
    
     ```python3 app.py```

    Windows:
    
     ```py app.py```

# Functions
```pawn
// Webhooks
SendDiscordWebhookMessage(const message[], const webhook_username[] = "samp-webhooks");
SendDiscordWebhookEmbed(const title[], const description[], const color[], const webhook_username[] = "samp-webhooks");
```

# Examples
```pawn
#include <a_samp>
#include <samp-discord-api>

main(){ return 0; }

public OnGameModeInit()
{
	SendDiscordWebhookEmbed("Server was started", "the server has been successfully started", .webhook_username = "test webhook");
	return 1;
}
```
![example](https://cdn.discordapp.com/attachments/1261132422448156673/1264619571571331093/image.png?ex=669e8841&is=669d36c1&hm=17def04e5de25ea1f241740c81298d2faeb3860af3c69ee31cde80783a3d649c&)
