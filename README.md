# planetelegram

Telegram bot supporting Planetarion alliance group chats.

## Setup

1. Install required packages with `pip`
2. Set ENV variables (see below)
3. Add current round stats XML to `/stats` in root
4. Run:

```bash
python main.py
```

## Environment variables

|Name|Description|
|---|---|
|CURRENT_ROUND|An integer representing the current round|
|TG_TOKEN|Your Telegram bot token|
|CHAT_ID|The ID of the chat where the bot will operate|

## Usage

```
/att             list current attacks
/att add x y z   add attack (x=target, y=landing tick, z=ships to send)
/att remove x    remove attack (x=ID)
/eff x y         calculate efficiency of ships (x=number, y=name)
/song            get current battle song
/song x          set current battle song (x=youtube link)
/tick            get current tick
```

