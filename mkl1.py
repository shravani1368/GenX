import datetime

def main():

    bad_words = ["dangerous", "dirty", "disaster"]  

    with open("mkl.txt", "a") as file:
        while True:
            text = input("Type something (Ctrl+C to stop): ")
            words = text.lower().split()

            for word in words:  
                if word in bad_words:
                    file.write(f"{datetime.datetime.now()} - Flagged word: {word}\n")
                    file.flush()
                    print("⚠ Warning: inappropriate word detected!")

if __name__ == "__main__":
    main()                  