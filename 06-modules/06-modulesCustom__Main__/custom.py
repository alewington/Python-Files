# custom module

def uptext(text) -> str:
    text = text.upper()
    return text


if __name__ == "__main__":
    print(uptext("hello world!"))
    print(uptext("Stuart"))
    print(uptext("Gru"))

# this won't run in the main program main.py
