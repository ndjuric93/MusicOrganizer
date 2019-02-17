from marshmallow import fields


class LeadingZerosIntegerField(fields.Integer):

    def __init__(self, zeros_count, *args, **kwargs):
        super(LeadingZerosIntegerField, self).__init__(*args, **kwargs)
        self.zeros_count = zeros_count

    def _format_num(self, value):
        if value is None:
            return None
        return str(value).zfill(self.zeros_count)
