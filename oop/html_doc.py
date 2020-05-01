class Tag:
    def __init__(self, name, contents):
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)
        self.contents = contents

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__("!DOCTYPE html", "")
        self.end_tag = ""


class Head(Tag):
    def __init__(self):
        super().__init__("head", "")


class Body(Tag):
    def __init__(self):
        super().__init__("body", "")
        self._body_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.contents += str(tag)
        super().display(file=file)


class HtmlDoc:  # composed of three other classes here we have polimorphism
    def __init__(self):
        self._doc_type = DocType()
        self._head = Head()
        self._body = Body()

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display()
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    my_page = HtmlDoc()
    my_page.add_tag("h1", 'Main header')
    my_page.add_tag("h2", "sub header")
    my_page.add_tag("p", "some text in para")
    with open('test.html', 'w') as test:
        my_page.display(file=test)
