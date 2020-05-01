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
        self._head_contents = []

    def add_tag(self, name, contents):
        new_tag = Tag(name, contents)
        self._head_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._head_contents:
            self.contents += str(tag)
        super().display(file=file)


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


class HtmlDoc:  # rewritten with agregation
    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        self._body.add_tag(name, contents)

    def add_metadata(self, name, contents):
        self._head.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display()
        print("<html>", file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':

    new_body = Body()
    new_body.add_tag("h1", "Aggregasion")
    new_body.add_tag('p', 'unlike <strong>composition</strong> agregation used '
                          'exisiting instances of objects to build up another '
                          'object')
    new_body.add_tag('p', 'the composed object doesnt actually own the object '
                          'that it i scomposed of if it is destroyed those '
                          'obects continue to exist')
    new_doctype = DocType()
    new_header = Head()
    my_page = HtmlDoc(new_doctype, new_header, new_body)

    # give thw doucment enew coent by switching it's body

    my_page._body = new_body
    with open('test3.html', 'w') as test:
        my_page.display(file=test)
