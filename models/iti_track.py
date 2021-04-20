from odoo import models,fields

class ItiTrack(models.Model):
    _name="iti.track"
    _description="track"
   # _rec_name="name"default name if your model already have a coulmn its name is name
    #if you dont have name record its name will be (iti.track,1)
    #and if ypu want to show any field else just make _rec_name="your field name"
    name=fields.Char()
    capacity=fields.Integer()
    is_open=fields.Boolean()
    student_ids=fields.One2many("iti.student", "track_id")