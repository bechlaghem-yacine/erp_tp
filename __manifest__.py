{

    'name':'clinic managment test',
    'version':'1.0',
    'category':'clinic',
    'auther':'yacine',
    'depends': ['base'],
    'data':[ 
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/doctor.xml',
        'views/prescription.xml',
        # 'views/appointment.xml',
        # 'views/medicine.xml',



    ],
    'installable':True,
    'application':True,
    'auto_install':False,

}