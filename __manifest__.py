{

    'name':'clinic managment',
    'version':'1.0',
    'category':'clinic',
    'auther':'yacine',
    'depends': ['base','hr'],
    'data':[ 
        'security/ir.model.access.csv',
        'wizard/prescription_wizard.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'wizard/add_medicine_wizard_view.xml',
        'wizard/reset_medicines_wizard_view.xml',
        'views/prescription.xml',
        'views/appointment.xml',
        'views/medicine.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,

}