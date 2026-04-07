def parent(name):
    def hello():
        return "Hello "+name
    def gm():
        return "Good morning "+name
    def gn():
        return "Good Night "+name
    return gm, gn, hello
def main():
    a,b,c = parent("shravani")
    print(a())
    print(b())
    print(c())

    



if(__name__ == "__main__"):
    main()

