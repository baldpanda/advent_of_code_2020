from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Range, OneOf, Regexp

VALID_EYE_COLOURS = ["amb", "blu", "brn", "gry", "grn", "hzl","oth"]

def validate_height(height):
    if "cm" in height and (150 > int(height.strip("cm")) or int(height.strip("cm")) > 193):
        raise ValidationError("Height must be between 150cm and 190cm")
    if "in" in height and (59 > int(height.strip("in")) or int(height.strip("in")) > 76):
        raise ValidationError("Height must be between 59inches and 76inches")
    if ("in" not in height) and ("cm" not in height):
        raise ValidationError("Height must be between 59inches and 76inches")

class PassportSchema(Schema):
    ecl = fields.Str(required=True, validate=OneOf(VALID_EYE_COLOURS))
    eyr = fields.Integer(validate=Range(min=2020, max=2030), required=True)
    pid = fields.Str(required=True, validate=Regexp(r"[0-9]{9}$"))
    hcl = fields.Str(required=True, validate=Regexp(r"#[a-f0-9]{6}$"))
    byr = fields.Integer(validate=Range(min=1920, max=2002), required=True)
    iyr = fields.Integer(validate=Range(min=2010, max=2020), required=True)
    cid = fields.Str(required=False)
    hgt = fields.Str(required=True, validate=validate_height)