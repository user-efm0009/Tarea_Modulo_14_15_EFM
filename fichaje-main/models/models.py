from odoo import models, fields, api

class FichajeAsistencia(models.Model):
    _name = 'fichaje.asistencia'
    _description = 'Registro de Fichajes de DAM'

    # Odoo usa el campo 'name' por defecto para mostrar registros
    name = fields.Char(string='Referencia', compute='_compute_name')
    
    employee_id = fields.Many2one('res.users', string='Empleado', default=lambda self: self.env.user)
    fecha_fichaje = fields.Datetime(string='Fecha y Hora', default=fields.Datetime.now)
    tipo_accion = fields.Selection([
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('descanso', 'Descanso')
    ], string='Accion', required=True)

    # Esto rellena el nombre automáticamente para que no falle el XML
    @api.depends('employee_id', 'fecha_fichaje')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.employee_id.name} - {record.fecha_fichaje}"

    def registrar_fichaje(self):
        self.create({
            'employee_id': self.env.user.id,
            'fecha_fichaje': fields.Datetime.now(),
            'tipo_accion': 'entrada'
        })