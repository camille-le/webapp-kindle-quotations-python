"""
Program to transform an XML document into a Python object
* super().__init__() allows you to build classes that easily extend the functionality of previous built classes
without implementing their functionality again
* __str__ is a special method, like __init__, that returns a string representation of the object
* __init__ is a method, similar to constructions in C++ and Java, which is used to initialize the object's
state
"""

from html.parser import HTMLParser


class KindleBook:
    def __init__(self, title, authors, citation):
        self.title = title
        self.authors = authors
        self.citation = citation

    def __str__(self):
        return self.title + "\n" + self.authors + "\n" + self.citation


class KindleQuotation:
    def __init__(self, page_number, text, section_heading):
        self.page_number = page_number
        self.text = text
        self.section_heading = section_heading

    def __str__(self):
        return self.section_heading + " " + self.page_number + "\n" + self.text


class KindleParser(HTMLParser):

    kindle_book = None
    list_of_quotations = []

    def __init__(self):
        super().__init__()
        # Boolean Flags to handle parsing
        self.b_title, self.b_authors, self.b_citation = False, False, False
        self.b_section_heading, self.b_page_number, self.b_text = False, False, False

        # Default values as empty until they are found
        self.title, self.authors, self.citation = "", "", ""
        self.section_heading, self.curr_page_number = "(empty)", ""

    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            div_class = attrs[0][1]
            if div_class == 'bookTitle':
                self.b_title = True
            elif div_class == 'authors':
                self.b_authors = True
            elif div_class == 'citation':
                self.b_citation = True
            elif div_class == 'noteHeading':
                self.b_page_number = True
            elif div_class == 'sectionHeading':
                self.b_section_heading = True
            elif div_class == 'noteText':
                self.b_text = True

    def handle_endtag(self, tag):
        if tag == 'div' and self.b_page_number:
            new_kindle_quotation = KindleQuotation(self.process_page_number(), "", self.section_heading)
            self.list_of_quotations.append(new_kindle_quotation)
            self.b_page_number = False

    def process_page_number(self):
        return self.curr_page_number.split()[-1]

    def handle_data(self, data):
        data = data.strip()
        if self.b_title:
            self.title = data
            self.b_title = False
        elif self.b_authors:
            self.authors = data
            self.b_authors = False
        elif self.b_citation:
            self.citation = data
            self.kindle_book = KindleBook(self.title, self.authors, self.citation)
            self.b_citation = False
        elif self.b_section_heading:
            self.section_heading = data
            self.b_section_heading = False
        elif self.b_page_number:
            self.curr_page_number = data
        elif self.b_text:
            last_book = self.list_of_quotations[-1]
            last_book.text = data
            self.b_text = False


def process():
    book1 = "../notebooks/On Earth We're Briefly Gorgeous - Notebook.xml"
    book2 = "../notebooks/The Art of Communicating - Notebook.xml"
    book3 = "../notebooks/The Life-Changing Magic of Tidying Up - Notebook.xml"
    book4 = "../notebooks/The Power of Habit - Notebook.xml"
    with open(book4, 'r') as file:
        file_text = file.read()
        parser = KindleParser()
        parser.feed(file_text)

        print(parser.kindle_book,"\n")
        for quotation in parser.list_of_quotations:
            print(quotation, "\n")





    