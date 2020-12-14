import csv, json
from html.parser import HTMLParser
from flask import make_response



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


class KindleHTMLParser(HTMLParser):

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


class KindleIO: 
    def __init__(self, upload_file): 
        parser = KindleHTMLParser()
        parser.feed(upload_file) 
        self.kindle_book = parser.kindle_book
        self.kindle_quotations = parser.list_of_quotations

    ''' 
    returns a string representation of a csv file
    ''' 
    def process_csv(self): 
        csvfile = KindleCsvTextBuilder() 
        writer = csv.writer(csvfile)
        writer.writerow(["title", "authors", "citation", "page_number", "text", "section_heading"])
        for self.quotation in self.kindle_quotations: 
            writer.writerow([self.kindle_book.title, self.kindle_book.authors, self.kindle_book.citation, 
            self.quotation.page_number, self.quotation.text, self.quotation.section_heading])        
        csv_string = csvfile.csv_string    
        return ''.join(csv_string) 

    '''
    returns a list of dictionaries 
    '''
    def process_json(self): 
        kindle_dict = [] 
        for self.quotation in self.kindle_quotations: 
            kindle_dict.append({ "title": self.kindle_book.title, "authors": self.kindle_book.authors,
            "citation": self.kindle_book.citation, "page_number": self.quotation.page_number, 
            "text": self.quotation.text, "section_heading": self.quotation.section_heading})             
        return kindle_dict
    
    '''
    generates json response 
    '''
    def get_json(self, data): 
        content_disposition = "attachment; filename="
        content_disposition += self.kindle_book.title + ".json"
        response = make_response(json.dumps(data, indent=2)) 
        response.headers["Content-Disposition"] = content_disposition
        response.mimetype = 'application/json' 
        return response
    
    ''' 
    generates csv data
    ''' 
    def get_csv(self, data): 
        response = make_response(data)
        content_disposition = "attachment; filename="
        content_disposition += self.kindle_book.title + ".csv"
        response.headers["Content-Disposition"] = content_disposition
        response.headers["Content-type"] = "text/csv"
        response.mimetype='text/csv'
        return response        


def download_json(upload_file): 
    kind_io = KindleIO(upload_file) 
    data = kind_io.process_json() 
    return kind_io.get_json(data)


def download_csv(upload_file): 
    kind_io = KindleIO(upload_file) 
    data = kind_io.process_csv()     
    return kind_io.get_csv(data)


def temp_csv(upload_file): 
    kind_io = KindleIO(upload_file) 
    data = kind_io.process_csv()     
    print(data)


     


    