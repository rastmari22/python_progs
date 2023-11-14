FIO="Иванов И.И."
job_title="инженер"
divisions="отдел маркетинга"
phone_number="354"



kl=[FIO,
                                             ]
zn=[(job_title,divisions,phone_number)]

kl_zn=list(zip(kl,zn))
directory=dict(kl_zn)
print(directory)