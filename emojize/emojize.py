def main():
    emojis = {
        ":1st_place_medal:": "🥇",
        ":money_bag:": "💰",
        ":smile_cat:": "😸",
        ":thumbs_up:": "👍",
        ":thumbsup:": "👍",
        ":heart:": "❤️",
        ":sunglasses:": "😎",
        ":rocket:": "🚀",
        ":earth_asia:": "🌏",
        ":candy:": "🍬",
        ":ice_cream:": "🍨"
    }

    user_input = input().strip()

    for code, emoji in emojis.items():
        user_input = user_input.replace(code, emoji)
        print(user_input, end='')

if __name__ == "__main__":
    main()
