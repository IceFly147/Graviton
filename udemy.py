import asyncio, json
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

async def main():
    bot = await Chatbot.create() # Passing cookies is "optional", as explained above
    response = await bot.ask(prompt="Hello world", conversation_style=ConversationStyle.precise, simplify_response=True)
    print(json.dumps(response, indent=2)) # Returns
    await bot.close()

if __name__ == "__main__":
    asyncio.run(main())