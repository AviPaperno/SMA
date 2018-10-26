from wtforms.compat import string_types, text_type
from wtforms.validators import StopValidation

class DataRequired(object):
    field_flags = ('required', )

    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if not field.data or isinstance(field.data, string_types) and not field.data.strip():
            if self.message is None:
                message = field.gettext('This field is required.')
            else:
                message = self.message

            field.errors[:] = []
            raise StopValidation(message)


class KeyRequired(object):
    field_flags = ('required', )

    def __init__(self, message=None, current_list = []):
        self.message = message
        self.current_list = current_list

    def __call__(self, form, field):
        if field.data not in self.current_list:
            if self.message is None:
                message = field.gettext('Этот ключ.')
            else:
                message = self.message

            field.errors[:] = []
            raise StopValidation(message)