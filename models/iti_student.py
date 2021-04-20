from odoo import models,fields,api
class ItiStudent(models.Model):
    _name="iti.student"

    name=fields.Char()
    age=fields.Integer()
    height=fields.Float()
    is_accepted=fields.Boolean()
    birth_date=fields.Date()
    interview_appointement=fields.Datetime()
    gender=fields.Selection([
        ("M","Male"),
        ("F","Female")
    ])
    image=fields.Image(max_width=400,max_height=400,verify_resolution=True)
    cover_letter=fields.Html()
    info=fields.Text()
    cv=fields.Binary()
    state=fields.Selection([
        ("new","New"),
        ("1st","First Interview"),
        ("2st","Second Interview"),
    ])
    track_capacity=fields.Integer(related="track_id.capacity")
    track_id=fields.Many2one(comodel_name="iti.track")
    skills_ids = fields.Many2many("iti.skills")

    skill_ids = fields.One2many("student.skill.line","student_id")


    def pass_first_interview(self):
        self.state="1st"


    @api.onchange('name')
    def onchange_name(self):
        if self.name:
            self.info= "my name is {}".format(self.name)
        else:
            self.name=""
        return {
            "warning":{
                "title":"Take Care",
                "message":"you have changed the name "
            }
        }
    @api.onchange('gender')
    def onchange_gender(self):
        if self.gender=='M':
            track_domain=[('is_open','=',True)]
        else:
            track_domain=[]
        return {
            "domain":{
               "track_id":track_domain

            }
        }



class StudentSkillLine(models.Model):
    _name="student.skill.line"
    _description="skill line"


    student_id = fields.Many2one("iti.student")
    skill_id = fields.Many2one("iti.skills")

    grade = fields.Char()



