# Define the chatbot's greeting and database
bot_name = "CryptoBuddy"
greeting = f"Hey there! I'm {bot_name} 🤖💰 — your friendly crypto sidekick. Let's find the best coin for you today!"

crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8
    }
}

# Function to process user input and return responses
def analyze_query(user_query):
    user_query = user_query.lower()

    if "sustainable" in user_query:
        best = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"🌱 Go with {best}! It's eco-friendly and long-term ready with a sustainability score of {crypto_db[best]['sustainability_score']}/10."

    elif "trending" in user_query or "growth" in user_query:
        trending_coins = [
            coin for coin, data in crypto_db.items()
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]
        ]
        if trending_coins:
            return f"🚀 For growth, consider: {', '.join(trending_coins)}."
        else:
            return "📉 Hmm... No rising coins with good market cap right now."

    elif "energy" in user_query:
        low_energy = [coin for coin, data in crypto_db.items() if data["energy_use"] == "low"]
        return f"🔋 Low energy coins: {', '.join(low_energy)}"

    elif "recommend" in user_query or "buy" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f"💡 Try {coin}! It’s booming and has a high market cap."
        return "🤔 I can't recommend a coin with strong growth signals at the moment."

    else:
        return "❓ Sorry, I didn't understand that. Try asking about trends, sustainability, or energy use."

# Run chatbot interaction
def run_chatbot():
    print(greeting)
    print("⚠️ Disclaimer: Crypto is risky — always do your own research before investing!")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print(f"{bot_name}: Catch you later! 🚀 Stay crypto-smart!")
            break
        response = analyze_query(user_input)
        print(f"{bot_name}: {response}")

# Start chatbot
if __name__ == "__main__":
    run_chatbot()
