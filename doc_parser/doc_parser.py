import zipfile, sys
import lxml.etree as ET


class DocParser():

    def __init__(self, filename):
        NS_W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
        NS_W10 = '{http://schemas.microsoft.com/office/word/2010/wordml}'

        # XML tags in Word forms:
        self.TAG_FIELD          = NS_W+'sdt'
        self.TAG_FIELDPROP      = NS_W+'sdtPr'
        self.TAG_FIELDTAG       = NS_W+'tag'
        self.ATTR_FIELDTAGVAL   = NS_W+'val'
        self.TAG_FIELD_CHECKBOX = NS_W10+'checkbox'
        self.TAG_FIELDCHECKED   = NS_W10+'checked'
        self.TAG_FIELD_CONTENT  = NS_W+'sdtContent'
        self.TAG_RUN            = NS_W+'r'
        self.TAG_TEXT           = NS_W+'t'
        self.TAG_BREAK          = NS_W+'br'

        self.filename = filename

    def parse_multiline_text(self, field_content_elem):
        """
        parse an XML element containing a single or multiline text
        field
        """
        if field_content_elem is None:
            return ''
        value = ''
        # iterate over all children elements
        for elem in field_content_elem.getiterator():
            # extract text:
            if elem.tag == self.TAG_TEXT:
                value += elem.text
            # and line breaks:
            elif elem.tag == self.TAG_BREAK:
                value += '\n'
        return value

    def parse_question_answers(self):
        """
        parse elements containing tags and group them as questions and answers
        parse checkboxes and retrieve checked value
        """
        output = {}
        zfile = zipfile.ZipFile(self.filename)
        form = zfile.read('word/document.xml')
        xmlroot = ET.fromstring(form)
        for field in xmlroot.getiterator():
            field_tag = field.find(self.TAG_FIELDPROP+'/'+self.TAG_FIELDTAG)
            if field_tag is None:
                continue
            tag = field_tag.get(self.ATTR_FIELDTAGVAL, None)
            value = self.parse_multiline_text(field.find(self.TAG_FIELD_CONTENT))
            _id = self.tag_to_id(tag)
            if _id and _id not in output:
                output[_id] = {}
            if self.is_question(tag):
                output[_id]['question'] = value
            elif self.is_answer(tag):
                if self.is_multianswer(tag):
                    # Check if it's a checkbox
                    field_checkbox = field_tag.getparent().find(self.TAG_FIELD_CHECKBOX)
                    if field_checkbox is not None:
                        output.pop(_id, None)
                        parent_id = self.get_parent_id(_id)
                        output[parent_id] = output[parent_id] if parent_id in output else {}
                        output[parent_id]['answer'] = []
                        output[parent_id]['options'] = output[parent_id]['options'] if 'options' in output[parent_id] else []
                        output[parent_id]['options'].append(self.get_checkbox_label(field_checkbox))
                        if self.is_checked(field_checkbox):
                            output[parent_id]['answer'].append(self.get_checkbox_label(field_checkbox))
                    else:
                        # Must be additional text if no checkbox found
                        output.pop(_id, None)
                        parent_id = self.get_parent_id(_id)
                        output[parent_id] = output[parent_id] if parent_id in output else {}
                        output[parent_id]['additional_text'] = value
                else:
                    # Single answer
                    output[_id]['answer'] = value
        zfile.close()
        return self.dict_to_arr(output)

    def tag_to_id(self, label):
        if label[0] not in ['Q', 'A']:
            return None
        return label[1:]

    def get_parent_id(self, _id):
        return _id.split('_')[0]

    def get_answer_label(self, _id):
        return 'A' + _id

    def get_question_label(self, _id):
        return 'Q' + _id

    def is_question(self, label):
        return label[0] == 'Q'

    def is_answer(self, label):
        return label[0] == 'A'

    def is_multianswer(self, label):
        # if it has 1.1_a, 1.1_b like labels, then it's multi answer
        return label[0] == 'A' and '_' in label

    def get_value(self, label):
        pass

    def output_dict_to_arr(self, output_dict):
        return 

    def get_checkbox_label(self, checkbox_ele):
        field_content = checkbox_ele.getparent().getparent().getparent()
        return self.parse_multiline_text(field_content).strip('☐').strip()

    def is_checked(self, checkbox_ele):
        checked = checkbox_ele.find(self.TAG_FIELDCHECKED)
        val = checked.get(self.ATTR_FIELDTAGVAL, None)
        return bool(val)

    def dict_to_arr(self, output):
        output_arr = []
        for key in output.keys():
            item = output[key]
            item['id'] = key
            output_arr.append(item)

        return output_arr

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        docparser = DocParser(filename)
        question_answers = docparser.parse_question_answers()
        print(question_answers)

