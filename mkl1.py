bad_words = ["Dangerous", "Dirty", "Disaster"]

with open("mkl.txt", "a") as file:
    while True:
        text = input("Type something (Ctrl+C to stop): ")
        words = text.lower().split()

        for word in words:
            if word in bad_words:
                file.write(f"Flagged word detected: {word}\n")
                file.flush()   # ensures it saves immediately
                print("⚠ Warning: inappropriate word detected!")