{

    'name':'clinic managment',
    'version':'1.0',
    'category':'clinic',
    'auther':'yacine',
    'depends': ['base','hr'],
    'data':[ 
        'security/ir.model.access.csv',
        'views/prescription_wizard.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/prescription.xml',
        'views/appointment.xml',
        'views/medicine.xml',
    ],
    'installable':True,
    'application':True,
    'auto_install':False,

}