# SA:MP Discord Webhooks API

a simple api, which allows to send webhooks to a specific discord channel, through a proxy, since samp does not support https. it was developed for use in Astro Roleplay (besta samp server).

# Run (on development)

1. Clone repository

   ```git clone https://github.com/vendder5/samp-discord-api.git```

2. Navigate to the repository directory

   ```cd samp-webhooks-api```

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
Discord_SendWebhookMessage(const message[], const webhook_username[] = "samp-webhooks");
Discord_SendWebhookEmbed(const title[], const description[], const color[], const webhook_username[] = "samp-webhooks");
```

# Examples
```pawn
#include <a_samp>
#include <samp-discord-api>

main(){ return 0; }

public OnGameModeInit()
{
	Discord_SendWebhookEmbed("Server was started", "the server has been successfully started", .webhook_username = "test webhook");
	return 1;
}
```

![example](https://cdn.discordapp.com/attachments/1259707494897549452/1270500832676286504/image.png?ex=66b3ed9b&is=66b29c1b&hm=7c1bc0d6fc96a7588292d223f046bc9001a838af1799215b6e8994a686f9d836&)
