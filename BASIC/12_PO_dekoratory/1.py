def uppercase_decorator(text):
    def up_text():
        return text().upper()
    return up_text

@uppercase_decorator
def text_ran():
    return 'nothing matter..'

print(text_ran())
