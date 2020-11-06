import csv
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
        
        self.b_title, self.b_authors, self.b_citation = False, False, False
        self.b_section_heading, self.b_page_number, self.b_text = False, False, False
        
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


class KindleCsvTextBuilder(object):
    def __init__(self):
        self.csv_string = []

    def write(self, row):
        self.csv_string.append(row)

def process(filepath, filetype):

    # Create KindleBook and KindleQuotations objects 
    kindle_book = None 
    kindle_quotations = None

    # Read in XML file, store data in KindleBook and KindleQuotations objects 
    with open(filepath, 'r', encoding='utf-8') as file:        
        file_text = file.read()

        parser = KindleParser()
        parser.feed(file_text)
        
        kindle_book = parser.kindle_book
        kindle_quotations = parser.list_of_quotations
        file.close() 

    # Write KindleBook and KindleQuotations into a CSV text builder; return CSV text builder 
    if filetype == 'csv':         
        csvfile = KindleCsvTextBuilder() 
        writer = csv.writer(csvfile)
        writer.writerow(["title", "authors", "citation", "page_number", "text", "section_heading"])
        for quotation in kindle_quotations: 
            writer.writerow([kindle_book.title, kindle_book.authors, kindle_book.citation, 
            quotation.page_number, quotation.text, quotation.section_heading])        
        csv_string = csvfile.csv_string    
        return ''.join(csv_string) 
        
    elif filetype == 'json': 
        kindle_dict = [] 
        for quotation in kindle_quotations: 
            kindle_dict.append({ "title": kindle_book.title, "authors": kindle_book.authors,
            "citation": kindle_book.citation, "page_number": quotation.page_number, 
            "text": quotation.text, "section_heading": quotation.section_heading})             
        return kindle_dict
    return '' 





     

    