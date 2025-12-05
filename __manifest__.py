{

    'name':'clinic managment',
    'version':'1.0',
    'category':'clinic',
    'auther':'yacine',
    'depends': ['base','hr'],
    'data':[ 
        'security/clinic_security.xml',
        'security/ir.model.access.csv',
        'wizard/prescription_wizard.xml',
        'views/medicalfile.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'wizard/add_medicine_wizard_view.xml',
        'wizard/reset_medicines_wizard_view.xml',
        'views/prescription.xml',
        'views/appointment.xml',
        'views/medicine.xml',
        'views/hr_employee_inherit_view.xml',
        'reports/ordonnance.xml',
        'reports/ordonnance_template.xml',
        'reports/ordonnance_with_photo.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,

}