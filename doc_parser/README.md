# doc_parser
Parse Fillable Form from Word Documents

#### Usage:
##### command-line
```console
	$ python doc_parser.py sample_doc.docx
```
##### python
```python
	from doc_parser import DocParser
	docparser = DocParser('sample_doc.docx')
	question_answers = docparser.parse_question_answers()
```
